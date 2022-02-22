from tkinter import *


root = Tk ()

num = StringVar()
spin_box = Spinbox (root, textvariable=num)
spin_box.pack()
spin_box.config (from_=1, increment=2, to=10)

root.mainloop()