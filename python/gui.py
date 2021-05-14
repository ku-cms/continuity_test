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
        topFrame = Frame(self.root)
        topFrame.pack(side=TOP)
        middleFrame = Frame(self.root)
        middleFrame.pack(side=TOP)
        bottomFrame = Frame(self.root)
        bottomFrame.pack(side=TOP)
        # Widgets
        label1 = Label(
            topFrame,
            text="Cable Continuity Tester",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=5,
            width=50
        )
        label2 = Label(
            bottomFrame,
            text="Output",
            font=("Arial", 30),
            fg=self.color_font,
            bg=self.color_background,
            height=10,
            width=50
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
        
        label1.pack(side=TOP)
        button1.pack(side=TOP)
        button2.pack(side=TOP)
        label2.pack(side=TOP)

def main():
    root = Tk()
    app  = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

