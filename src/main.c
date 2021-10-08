#include <stdio.h>
#include <stdlib.h>
#include "platform.h"
#include "xil_printf.h"
#include <xgpio.h>
#include "xparameters.h"
#include "sleep.h"

XGpio gpio;
int* map = MAPPING_33_TO_45;
int* wire_map = WIRES_33_TO_45;

u32 gpio_read(u32 channel);
void gpio_write(u32 channel, u32 data);
void getStartChar();
void run();
int freqTest(char s[]);
void sweep(int Hz, int r[]);
int printError(int r, int channel, char s[]);
const char* getWire(int channel);

int main()
{
    // Setup
    srand((unsigned) 69);
    XGpio_Initialize(&gpio, XPAR_GPIO_0_DEVICE_ID);
    init_platform();
    // Main Loop: begin
    while (1) {
        // Ask user to initialize program.
        // Note: use 'y' as flag to run
        // There were issues in clearing characters and only using enter
        // Do not enter characters after 'y' due to cable type bug
        getStartChar();

        sleep(1); // sleep to give GUI time to read beginning of test
        printf("\nStarting continuity test\n");
        run();
    }
    // Main Loop: end

    // Cleanup
    cleanup_platform();
    return 0;
}

// Bits set to 0 are output/write and bits set to 1 are input/read.

u32 gpio_read(u32 channel) {
    XGpio_SetDataDirection(&gpio, 1, XGpio_GetDataDirection(&gpio, 1) | (1 << channel));
    return (XGpio_DiscreteRead(&gpio, 1) & (1 << channel)) >> channel;
}

void gpio_write(u32 channel, u32 data) {
    XGpio_SetDataDirection(&gpio, 1, XGpio_GetDataDirection(&gpio, 1) & ~(1 << channel));
    XGpio_DiscreteWrite(&gpio, 1, (0 | (data << channel)));
}

// get character from user to begin
void getStartChar() {
    char c;
    printf("Enter 'y' to begin continuity test: ");
    c = getchar();
    while (c != 'y') {
        c = getchar();
    }
}

void run() {
    // Setup
    u32 read_mask = 0xFF << 6;
    XGpio_SetDataDirection(&gpio, 2, read_mask);
    u8 result = (u8)(XGpio_DiscreteRead(&gpio, 2) >> 6);

	// User indicates type of cable to test
	// WARNING: there is a bug of an infinite loop if non integer is entered, e.g. 'a'
	int cableType = 0;
	while (cableType < 1 || cableType > TYPES_OF_CABLES) {
		printf("Types of Cables: \n");
		printf("(1) E-link Type 1: (33pin - 45pin)\n");
		printf("(2) E-link Module 1: (17pin - 45pin)\n");
		printf("(3) E-link Module 2 (Type 3): (17pin - 45pin)\n");
		printf("(4) E-link Module 2 (Type 4): (17pin - 45pin)\n");
		printf("(5) E-link Module 3: (17pin - 45pin)\n");
		printf("================\n");
		printf("Select which kind of cable is being tested (1-%d): ", TYPES_OF_CABLES);
		scanf("%d", &cableType);
		sleep(1);
		printf("You have selected (%d)\n", cableType);
	}

	switch (cableType) {
		case 1:
			map = MAPPING_33_TO_45;
			wire_map = WIRES_33_TO_45;
			break;
		case 2:
			map = MAPPING_17_TO_45_M1;
			wire_map = WIRES_17_TO_45_M1;
			break;
		case 3:
			map = MAPPING_17_TO_45_M2_T3;
			wire_map = WIRES_17_TO_45_M2_T3;
			break;
		case 4:
			map = MAPPING_17_TO_45_M2_T4;
			wire_map = WIRES_17_TO_45_M2_T4;
			break;
		case 5:
			map = MAPPING_17_TO_45_M3;
			wire_map = WIRES_17_TO_45_M3;
			break;
		default:
			printf("Error: invalid cable type.\n");
			return;
	}

	char reports[280];
	int f = freqTest(reports);
	printf("%d faults found\n%s", f, reports);
}

int freqTest(char s[]) {
    sprintf(s, "================\n");

    static int** results;
    results = (int **)malloc(sizeof(int *)*freqsLength);
    for(int i = 0; i < freqsLength; i++) {
        results[i] = (int *)malloc(sizeof(int)*64);

        // Initialize results[i] to 0
        for(int j = 0; j < 64; j++) {
        	results[i][j] = 0;
        }
    }

    for (int i = 0; i < freqsLength; i++) {
        printf("Starting sweep at %d Hz\n", freqs[i]);
        sweep(freqs[i], results[i]);
    }

    // Print results
    int faults = 0;
    for (int i = 0; i < 64; i++) {
        int diff = 0;
        for (int j = 1; j < freqsLength; j++) {
            if (results[0][i] != results[j][i]) {
                diff += 1;
            }
        }

        char tmp[140];
        if (diff != 0) {
            sprintf(tmp, "Capacitive Coupling detected at wire %s!\n", getWire(i));
            strcat(s, tmp);

            for (int j = 0; j < freqsLength; j++) {
                sprintf(tmp, "\tAt %d Hz: ", freqs[j]);
                strcat(s, tmp);
                if (printError(results[j][i], i, s) == 0) {
                    strcat(s, "No faults detected.\n");
                };
                results[j][i] = 0; // Clear results
            }

            faults += 1;
        } else {
            faults += printError(results[0][i], i, s);

            // Clear results
            //printf("Before clearing results\n");
            for (int j = 0; j < freqsLength; j++) {
                results[j][i] = 0;
            }
            //printf("After clearing results\n");
        }

    }
    if (faults == 0) {
        sprintf(s, "================\nCable is fault-free!\n");
    }
    printf("End of freqTest(): Faults = %d\n", faults);
    return faults;
}

void sweep(int Hz, int r[]) {

    for (int channel = 0; channel < 64; channel++) {
        // Skips unused / already tested GPIO registers
        if (map[channel] < channel) {
            continue;
        }
        printf("testing channel %d-%d\n", channel, map[channel]);

        u32 errors_low = 0; u32 errors_high = 0; // Bits are 1 where there are errors
        u32 output_low = 0; u32 output_high = 0; // Determines if error is short or open circuit

        //// ================================================ ////
        //// ================================================ ////
        //// ================================================ ////
        //// !!!! REMEMBER SWAP p BACK TO 512 iterations !!! ////
        //// !!!! REMEMBER SWAP data BACK TO random function (see comment) !!! ////
        //// ================================================ ////
        //// ================================================ ////
        //// ================================================ ////
        for (int p = 0; p < 1; p++) { // 512-bit test pattern index
            int data = 1; //rand() % 2; // Actual bit to write per index
            //(pattern & (1 << (p%16))) >> (p%16);

            // Clears and writes to GPIO
            XGpio_SetDataDirection(&gpio, 1, 0x0);
            XGpio_SetDataDirection(&gpio, 2, 0x0);
            XGpio_DiscreteWrite(&gpio, 1, data << channel);
            XGpio_DiscreteWrite(&gpio, 2, data << (channel-32));

            //printf("Wrote low (%d) high (%d)\n", (int)(data << channel), (int)(data << (channel-32)));

            // Create read mask
            u32 mask_lower = 0x0; u32 mask_upper = 0x0;// Default: don't read anything
            for (int m = 0; m < 64; m++) {
                if (map[m] >= 0) {
                    mask_lower |= (1 << m); // Read from valid input reg
                    mask_upper |= (1 << (m-32)); // Read from valid input reg

                    // Read from valid output reg
                    mask_lower |= (1 << map[m]);
                    mask_upper |= (1 << (map[m]-32));
                }
                mask_lower &= ~(1 << channel); // Don't read from bit we wrote to.
                mask_upper &= ~(1 << (channel-32)); // Don't read from bit we wrote to.
            }

            //printf("Mask-l: %d, Mask-h: %d\n", (int)mask_lower, (int)mask_upper);

            if (Hz > 0) {
                usleep(1000000 * (1.0/Hz)); // Delay according to frequency
            }

            // Reads GPIO
            XGpio_SetDataDirection(&gpio, 1, mask_lower);
            XGpio_SetDataDirection(&gpio, 2, mask_upper);

            // Results pulled from GPIO
            u32 result_low = XGpio_DiscreteRead(&gpio, 1);
            u32 result_high = XGpio_DiscreteRead(&gpio, 2);

            // Finds expected values from read
            u32 expected_low = (data << channel) | (data << (map[channel]));
            u32 expected_high = (data << (channel-32)) | (data << (map[channel]-32));

            // error => XOR operator => If result is different from expected for a bit, then there is error at bit
            // result & error => if short, output is 1, if break output is 0 at a bit with an error
            // 		(Result is 1 at bit where something is detected, 0 where it isn't.
            // 		& operator filters out only the bits where an error is detected!


            errors_low |= (result_low  ^ expected_low );
            output_low  |= result_low  & (result_low  ^ expected_low );

            errors_high |= (result_high ^ expected_high);
            output_high |= result_high & (result_high ^ expected_high);

//            printf("Low: Expected %d, Got %d; map[%d] = %d\n", (int)expected_low, (int)result_low, (int)channel, (int)map[channel]);
//            printf("High: Expected %d, Got %d; map[%d] = %d\n", (int)expected_high, (int)result_high, (int)channel, (int)map[channel]);
        }

        // Writes errors if they exist
        if (errors_low != 0 || errors_high != 0) {
            for (int c = 0; c < 64; c++) {
            	// Returns proper error for particular GPIO
                u32 errors = c < 32 ? errors_low : errors_high;
                u32 output = c < 32 ? output_low : output_high;

//                printf("Errors: %d\n", (int)errors);
//                printf("Output: %d\n", (int)output);

                int c_mod = c % 32;
                if ((errors & (1 << c_mod)) >> c_mod == 1) { // 1 if there is an error at that channel
                    // See printError function to explain this
                	if ((output & (1 << c_mod)) >> c_mod == 1) {
                        r[c] += 10; // Short
//                        printf("Short at %d\n", c);
                    } else { // Break
                        r[c] += 1;
//                        printf("Break at %d\n", c);
                    }
                }

//                printf("Wrote %d to results bit %d\n", r[c], c);

            }
        }
    }
}

// r is used to denote the specific type of error.
// Shorts and breaks can happen simultaneously (both == wire swap)
// Shorts are denoted by adding 10, breaks by adding 1.
// => If r >= 10, a short is def present
// => If r is odd, a break is def present
// => If both, wires are swapped.
int printError(int r, int channel, char s[]) {
    char tmp[140];
    printf("Running printError() for channel %d; result = %#x\n", channel, r);
    if (r != 0) {
        if (r % 2 == 1 && r >= 10) {
            sprintf(tmp, "Wire %s is swapped with another wire\n", getWire(channel));
            strcat(s, tmp);
        } else {
            if (r % 2 == 1) {
                sprintf(tmp, "Break at wire %s\n", getWire(channel));
                strcat(s, tmp);
            }

            if (r >= 10) {
                sprintf(tmp, "%d short(s) at wire %s\n", r/10, getWire(channel));
                strcat(s, tmp);
            }
        }
        return 1;
    }
    fflush(stdout);
    return 0;
}

const char* getWire(int channel) {
    printf("Running getWire() for channel %d: maps to %d\n", channel, wire_map[channel]);

    switch (wire_map[channel]) {
        case CMD_P:
            return "CMD+";
            break;
        case CMD_N:
            return "CMD-";
            break;
        case DATA0_P:
            return "D0+";
            break;
        case DATA0_N:
            return "D0-";
            break;
        case DATA1_P:
            return "D1+";
            break;
        case DATA1_N:
            return "D1-";
            break;
        case DATA2_P:
            return "D2+";
            break;
        case DATA2_N:
            return "D2-";
            break;
        case DATA3_P:
            return "D3+";
            break;
        case DATA3_N:
            return "D3-";
            break;
        default:
//            printf("Error: Invalid wire for channel %d\n", channel);
            return "Error: invalid wire.";
    }
}
