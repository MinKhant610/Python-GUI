from tkinter import * 
from tkinter import ttk
from typing import Tuple 

root = Tk ()

# command => state (eg) => (top_level.state('zoomed')) => zoomed,
# withdrawn, iconic, normal
# command => eg => top_level.iconify() => (like mini) => deiconify

top_level = Toplevel()
top_level.title ('TOP')
top_level.geometry('200x100')
top_level.lift(root)
# top_level.resizable(False,False)
top_level.maxsize(600,400)
top_level.minsize(200,200)
top_level.resizable (True, True) #(width, height)
top_level.mainloop()