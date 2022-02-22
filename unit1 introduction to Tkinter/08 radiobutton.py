from tkinter import *
from tkinter import ttk

root = Tk ()

programming = StringVar ()
ttk.Radiobutton (root, text='C', variable=programming, value='C').pack()
ttk.Radiobutton (root, text='C++', variable=programming, value='C++').pack()
ttk.Radiobutton (root, text='Python', variable=programming, value='Python').pack()
ttk.Radiobutton (root, text='JavaScript', variable=programming, value='JavaScript').pack()

root.mainloop()
