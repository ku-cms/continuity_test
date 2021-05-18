# gui.py

from tkinter import *

class GUI():
    
    def __init__(self, root):
        self.root = root
        self.setColors()
        self.run()

    def setColors(self):
        self.color_font         = "gray95"
        self.color_background   = "gray45"

    def run(self):
        button_padx = 10
        button_pady = 10
        # Frames
        frame_top = Frame(
            self.root,
            bg=self.color_background,
            height=100
        )
        frame_middle = Frame(
            self.root,
            bg=self.color_background,
            height=100
        )
        frame_bottom = Frame(
            self.root,
            bg=self.color_background,
            height=200
        )
        frame_top.pack(side=TOP,    fill=BOTH, expand=True)
        frame_middle.pack(side=TOP, fill=BOTH, expand=True)
        frame_bottom.pack(side=TOP, fill=BOTH, expand=True)
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
            frame_middle,
            self.cable_type,
            *self.cable_types
        )
        self.cable_type_menu.config(font=("Arial", 20))
        label_title = Label(
            frame_top,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=1,
            width=40
        )
        label_cable_number = Label(
            frame_middle,
            text="Cable Number",
            font=("Arial", 20),
            fg=self.color_font,
            bg=self.color_background,
            height=1,
            width=20
        )
        label_output = Label(
            frame_bottom,
            text="Output",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=1,
            width=40
        )
        button_start = Button(
            frame_middle,
            text="Start",
            font=("Arial", 20),
            command=self.start,
            fg="gray10",
            bg="SpringGreen3"
        )
        button_stop = Button(
            frame_middle,
            text="Stop",
            font=("Arial", 20),
            command=self.stop,
            fg="gray10",
            bg="firebrick2"
        )
        button_select = Button(
            frame_middle,
            text="Select Cable",
            command=self.select,
            font=("Arial", 20),
            fg="gray10",
            bg="deep sky blue"
        )
        entry_cable_number = Entry(
            frame_middle,
            font=("Arial", 20)
        )
        text_box = Text(
            frame_bottom,
            font=("Arial", 14),
            height=20,
            width=80
        )
        
        # Frame
        label_title.grid(           row=1, column=1)
        # center grid using surrounding empty rows/columns as padding to fill space
        frame_top.grid_rowconfigure(0,       weight=1)
        frame_top.grid_rowconfigure(2,       weight=1)
        frame_top.grid_columnconfigure(0,    weight=1)
        frame_top.grid_columnconfigure(2,    weight=1)
        # Frame
        label_cable_number.grid(    row=1, column=1, padx=button_padx, pady=button_pady)
        entry_cable_number.grid(    row=1, column=2, padx=button_padx, pady=button_pady)
        button_start.grid(          row=2, column=1, padx=button_padx, pady=button_pady)
        button_stop.grid(           row=2, column=2, padx=button_padx, pady=button_pady)
        button_select.grid(         row=3, column=1, padx=button_padx, pady=button_pady)
        self.cable_type_menu.grid(  row=3, column=2, padx=button_padx, pady=button_pady)
        # center grid using surrounding empty rows/columns as padding to fill space
        frame_middle.grid_rowconfigure(0,       weight=1)
        frame_middle.grid_rowconfigure(4,       weight=1)
        frame_middle.grid_columnconfigure(0,    weight=1)
        frame_middle.grid_columnconfigure(3,    weight=1)
        # Frame
        label_output.grid(          row=1, column=1)
        text_box.grid(              row=2, column=1, padx=20, pady=20)
        # center grid using surrounding empty rows/columns as padding to fill space
        frame_bottom.grid_rowconfigure(0,       weight=1)
        frame_bottom.grid_rowconfigure(3,       weight=1)
        frame_bottom.grid_columnconfigure(0,    weight=1)
        frame_bottom.grid_columnconfigure(2,    weight=1)


    def start(self):
        print("START")
    
    def stop(self):
        print("STOP")
    
    def select(self):
        print("SELECT {0}".format(self.cable_type.get()))

def main():
    root = Tk()
    app  = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

