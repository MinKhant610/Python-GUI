from cProfile import label
from tkinter import * 
from tkinter import ttk

root = Tk () 
root.geometry('600x400')
root_label = ttk.Label (root, text='This is main window')
root_label.pack()

top = Toplevel ()
top.geometry('200x200')
top_label = ttk.Label (top, text='This is top level window')
top_label.pack()

root.mainloop()