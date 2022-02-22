#combo box or drop drown 

from tkinter import *
from tkinter import ttk 

root = Tk () 

programming = StringVar()
drop_down = ttk.Combobox (root, textvariable=programming)
drop_down.pack()
drop_down.config(values=('C','C++','Python','JavaScript'))
#drop_down.state (['readonly'])

root.mainloop()
