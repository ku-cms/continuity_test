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
        text_box = Text(
            frame_bottom
        )
        
        #label_title.pack(side=TOP)
        #button_start.pack(side=LEFT)
        #button_stop.pack(side=LEFT)
        #button_select.pack(side=LEFT)
        #self.cable_type_menu.pack(side=LEFT)
        #label_output.pack(side=TOP)
        #text_box.pack(side=TOP)
        
        label_title.grid()
        button_start.grid(          row=0, column=0)
        button_stop.grid(           row=0, column=1)
        button_select.grid(         row=0, column=2)
        self.cable_type_menu.grid(  row=0, column=3)
        label_output.grid(          row=0, column=0)
        text_box.grid(              row=1, column=0)

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

