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
        topFrame = Frame(
            self.root,
            bg=self.color_background,
            height=100
        )
        middleFrame = Frame(
            self.root,
            bg=self.color_background,
            height=100
        )
        bottomFrame = Frame(
            self.root,
            bg=self.color_background,
            height=200
        )
        topFrame.pack(side=TOP,    fill=BOTH, expand=True)
        middleFrame.pack(side=TOP, fill=BOTH, expand=True)
        bottomFrame.pack(side=TOP, fill=BOTH, expand=True)
        # Widgets
        label1 = Label(
            topFrame,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=1,
            width=40
        )
        label2 = Label(
            bottomFrame,
            text="Output",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=1,
            width=40
        )
        button1 = Button(
            middleFrame,
            text="Start",
            font=("Arial", 20),
            fg="gray10",
            bg="SpringGreen3"
        )
        button2 = Button(
            middleFrame,
            text="Stop",
            font=("Arial", 20),
            fg="gray10",
            bg="firebrick2"
        )
        text_box = Text(
            bottomFrame
        )
        
        label1.pack(side=TOP)
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        label2.pack(side=TOP)
        text_box.pack(side=TOP)

def main():
    root = Tk()
    app  = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

