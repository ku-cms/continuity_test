# gui.py

from tkinter import *
from client import Client

class GUI():
    
    def __init__(self, root, client):
        self.root = root
        self.client = client
        self.setColors()
        self.run()

    def setColors(self):
        self.color_label_fg  = "gray95"
        self.color_label_bg  = "gray45"
        self.color_button_fg = "gray10"

    def run(self):
        button_padx = 10
        button_pady = 10
        # Frames
        self.frame_top = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100
        )
        self.frame_middle = Frame(
            self.root,
            bg=self.color_label_bg,
            height=100
        )
        self.frame_bottom = Frame(
            self.root,
            bg=self.color_label_bg,
            height=200
        )
        self.frame_top.pack(side=TOP,    fill=BOTH, expand=True)
        self.frame_middle.pack(side=TOP, fill=BOTH, expand=True)
        self.frame_bottom.pack(side=TOP, fill=BOTH, expand=True)
        # Widgets
        self.cable_types = [
            "Type 1",
            "Type 2",
            "Type 3",
            "Type 4",
            "Type 5"
        ]
        self.cable_type = StringVar(self.root)
        self.cable_type.set(self.cable_types[0])
        self.cable_type_menu = OptionMenu(
            self.frame_middle,
            self.cable_type,
            *self.cable_types
        )
        self.cable_type_menu.config(font=("Arial", 20))
        self.label_title = Label(
            self.frame_top,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=40
        )
        self.label_cable_number = Label(
            self.frame_middle,
            text="Cable Number",
            font=("Arial", 20),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=20
        )
        self.label_output = Label(
            self.frame_bottom,
            text="Output",
            font=("Arial", 30),
            fg=self.color_label_fg,
            bg=self.color_label_bg,
            height=1,
            width=40
        )
        self.button_read = Button(
            self.frame_middle,
            text="Read",
            font=("Arial", 20),
            command=self.read,
            fg=self.color_button_fg,
            bg="gold"
        )
        self.button_start = Button(
            self.frame_middle,
            text="Start",
            font=("Arial", 20),
            command=self.start,
            fg=self.color_button_fg,
            bg="SpringGreen3"
        )
        self.button_clear = Button(
            self.frame_middle,
            text="Clear",
            font=("Arial", 20),
            command=self.clear,
            fg=self.color_button_fg,
            bg="firebrick1"
        )
        self.button_select = Button(
            self.frame_middle,
            text="Select Cable",
            command=self.select,
            font=("Arial", 20),
            fg=self.color_button_fg,
            bg="deep sky blue"
        )
        self.entry_cable_number = Entry(
            self.frame_middle,
            font=("Arial", 20)
        )
        self.text_box = Text(
            self.frame_bottom,
            font=("Arial", 14),
            height=20,
            width=80
        )
        
        # Frame
        self.label_title.grid(           row=1, column=1)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_top.grid_rowconfigure(0,       weight=1)
        self.frame_top.grid_rowconfigure(2,       weight=1)
        self.frame_top.grid_columnconfigure(0,    weight=1)
        self.frame_top.grid_columnconfigure(2,    weight=1)
        # Frame
        self.label_cable_number.grid(    row=1, column=1, padx=button_padx, pady=button_pady)
        self.entry_cable_number.grid(    row=1, column=2, padx=button_padx, pady=button_pady)
        self.button_read.grid(           row=2, column=1, padx=button_padx, pady=button_pady)
        self.button_start.grid(          row=3, column=1, padx=button_padx, pady=button_pady)
        self.button_clear.grid(          row=3, column=2, padx=button_padx, pady=button_pady)
        self.button_select.grid(         row=4, column=1, padx=button_padx, pady=button_pady)
        self.cable_type_menu.grid(       row=4, column=2, padx=button_padx, pady=button_pady)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_middle.grid_rowconfigure(0,       weight=1)
        self.frame_middle.grid_rowconfigure(5,       weight=1)
        self.frame_middle.grid_columnconfigure(0,    weight=1)
        self.frame_middle.grid_columnconfigure(3,    weight=1)
        # Frame
        self.label_output.grid(          row=1, column=1)
        self.text_box.grid(              row=2, column=1, padx=20, pady=20)
        # center grid using surrounding empty rows/columns as padding to fill space
        self.frame_bottom.grid_rowconfigure(0,       weight=1)
        self.frame_bottom.grid_rowconfigure(3,       weight=1)
        self.frame_bottom.grid_columnconfigure(0,    weight=1)
        self.frame_bottom.grid_columnconfigure(2,    weight=1)

    def checkCableNumber(self):
        # Require that cable number is a positive integer
        try:
            value = self.entry_cable_number.get()
            n = int(value)
            if n > 0:
                return True
            else:
                return False
        except ValueError:
            return False
    
    def getCableNumber(self):
        return int(self.entry_cable_number.get())

    def write(self, data):
        print(data)
        self.text_box.insert(END, data + "\n")

    def read(self):
        self.write("READ")
        data = self.client.read(timeout=15, nbytes=100000)
        self.write(data)
        return

    def start(self):
        # first check if cable number is valid
        valid_number = self.checkCableNumber()
        if valid_number:
            self.cable_number = self.getCableNumber()
            self.write("START: Cable number {0}".format(self.cable_number))
            x = "\n"
            self.client.write(timeout=1, data=x)
            self.read()
            return
        else:
            self.write("ERROR: Please enter a cable number (must be a positive integer).")
            return
    
    def clear(self):
        self.write("CLEAR")
        # delete cable number entry
        self.entry_cable_number.delete(0, END)
        # delete data in text box
        self.text_box.delete("1.0", END)
        return
    
    def select(self):
        cable_type = str(self.cable_type.get())
        self.write("SELECT {0}".format(cable_type))
        x = str(cable_type) + "\n"
        self.client.write(timeout=1, data=x)
        self.read()
        return

def main():
    port        = '/dev/ttyACM0'
    baudrate    = 115200 
    root        = Tk()
    client      = Client(port, baudrate)
    app         = GUI(root, client)
    root.mainloop()

if __name__ == "__main__":
    main()

