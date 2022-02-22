from tkinter import * 
from tkinter import ttk 

root = Tk () 

progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
value = DoubleVar()
progress_bar.config(mode = 'determinate', maximum=11.0)
progress_bar.config (variable=value)
progress_bar.pack()

scale = ttk.Scale (root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
scale.pack()

root.mainloop()