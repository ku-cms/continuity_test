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
        cable_types = [
            "Type 1",
            "Type 2",
            "Type 3",
            "Type 4",
            "Type 5"
        ]
        cable_type = StringVar(self.root)
        cable_type.set(cable_types[0])
        cable_type_menu = OptionMenu(
            frame_middle,
            cable_type,
            *cable_types
        )
        cable_type_menu.config(font=("Arial", 20))
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
            fg="gray10",
            bg="SpringGreen3"
        )
        button_stop = Button(
            frame_middle,
            text="Stop",
            font=("Arial", 20),
            fg="gray10",
            bg="firebrick2"
        )
        button_select = Button(
            frame_middle,
            text="Select Cable",
            font=("Arial", 20),
            fg="gray10",
            bg="deep sky blue"
        )
        text_box = Text(
            frame_bottom
        )
        
        label_title.pack(side=TOP)
        button_start.pack(side=LEFT)
        button_stop.pack(side=LEFT)
        button_select.pack(side=LEFT)
        cable_type_menu.pack(side=LEFT)
        label_output.pack(side=TOP)
        text_box.pack(side=TOP)

def main():
    root = Tk()
    app  = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

