/******************************************************************************
*
* Copyright (C) 2008 - 2014 Xilinx, Inc.  All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* Use of the Software is limited solely to applications:
* (a) running on a Xilinx device, or
* (b) that interact with a Xilinx device through a bus or interconnect.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* XILINX  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
* WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
* OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
*
* Except as contained in this notice, the name of the Xilinx shall not be used
* in advertising or otherwise to promote the sale, use or other dealings in
* this Software without prior written authorization from Xilinx.
*
******************************************************************************/

#ifndef __PLATFORM_H_
#define __PLATFORM_H_

#include "platform_config.h"

#define freqsLength 3
//int freqs[] = {100, 10000, 1000000};
int freqs[] = {10000, 100000, 1000000};

#define TYPES_OF_CABLES 5
int MAPPING_33_TO_45[64] = {17, 16, 19, 18, -1, -1, 21, 20, -1, -1, 23, 22, -1, -1, 25, 24, 1, 0, 3, 2, 7, 6, 11, 10, 15, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int MAPPING_17_TO_45_M1[64] = {23, 22, 17, 16, -1, -1, 19, 18, -1, -1, -1, -1, -1, -1, -1, -1, 3, 2, 7, 6, -1, -1, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int MAPPING_17_TO_45_M2_T3[64] = {-1, -1, -1, -1, -1, -1, -1, -1, 23, 22, 19, 18, -1, -1, 17, 16, 15, 14, 11, 10, -1, -1, 9, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int MAPPING_17_TO_45_M2_T4[64] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17, 16, 23, 22, 19, 18, 11, 10, 15, 14, -1, -1, 13, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int MAPPING_17_TO_45_M3[64] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 34, 33, 36, 35, -1, -1, 32, 31, -1, -1, -1, -1, -1, -1, -1, 23, 22, 17, 16, 19, 18, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};

enum wires {CMD_P, CMD_N, DATA0_P, DATA0_N, DATA1_P, DATA1_N, DATA2_P, DATA2_N, DATA3_P, DATA3_N};
int WIRES_33_TO_45[64] = {1, 0, 3, 2, -1, -1, 5, 4, -1, -1, 7, 6, -1, -1, 9, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int WIRES_17_TO_45_M1[64] = {1, 0, 3, 2, -1, -1, 5, 4, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int WIRES_17_TO_45_M2_T3[64] = {-1, -1, -1, -1, -1, -1, -1, -1, 1, 0, 5, 4, -1, -1, 3, 2, 2, 3, 4, 5, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int WIRES_17_TO_45_M2_T4[64] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, 2, 1, 0, 5, 4, 2, 3, 4, 5, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
int WIRES_17_TO_45_M3[64] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2, 3, 4, 5, -1, -1, 0, 1, -1, -1, -1, -1, -1, -1, -1, 1, 0, 3, 2, 5, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};

void init_platform();
void cleanup_platform();

#endif
