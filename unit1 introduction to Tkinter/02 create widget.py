from tkinter import *
from tkinter import ttk

root = Tk()
lable = ttk.Label(root,text='Tkinter Label').pack()
button = ttk.Button(root, text='Click Me') #.pack() or button.pack()
button.pack()
#button.config(text = 'Press Me')
root.mainloop()