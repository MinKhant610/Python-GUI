from tkinter import * 
from tkinter import ttk
from tkinter.font import BOLD

root = Tk ()
label = ttk.Label (root, text='Hello My name is Min Khant')
label.pack()
label.config (font = ('Courier', 20, 'bold')) # ('',20,'')
label.config (wraplength = 100)
label.config (justify = CENTER)
label.config (foreground = 'blue', background = 'black')
root.mainloop()