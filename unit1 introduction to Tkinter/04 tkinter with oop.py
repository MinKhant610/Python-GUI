from tkinter import * 
from tkinter import ttk
 
class HelloApp :
    def __init__(self, master) :
        self.lable = ttk.Label (master, text='My name is Tkinter')
        self.lable.grid (row=0, column=6, columnspan=2)

        self.button1 = ttk.Button (master, text='button1', command=self.name)
        self.button1.grid (row=1, column=4)

        self.button2 = ttk.Button (master, text='button2', command=self.name2)
        self.button2.grid (row=1, column=8)
        
    def name(self) :
        self.lable.config (text='My name is Jarvis')
    
    def name2(self) :
        self.lable.config (text='My name is Friday')

def main () :
    root = Tk()
    myapp = HelloApp (root)
    root.mainloop()

main ()