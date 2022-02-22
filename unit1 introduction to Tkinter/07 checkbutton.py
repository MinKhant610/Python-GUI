#use terminal for this program

from tkinter import *
from tkinter import ttk

root = Tk () 

label = ttk.Label (root, text = 'welcome')
check_but = ttk.Checkbutton (root, text='Python')
check_but.pack()
python_var = StringVar ()
python_var.set('Python Programming') # for default value
check_but.config (variable=python_var, onvalue='learning python',offvalue='not learing python ')
#an call python_var.get() when on vale => result = learning python 
root.mainloop()