import re
from textwrap import fill
from tkinter import * 
from tkinter import ttk 

root = Tk () 
paned_window = ttk.PanedWindow (root, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)
frame1 = ttk.Frame (paned_window, width=100, height=200, relief=SUNKEN)
frame2 = ttk.Frame (paned_window, width=400, height=400, relief=SUNKEN)
frame3 = ttk.Frame (paned_window, width=50, height=400, relief=SUNKEN)
paned_window.add (frame1, weight=1)
paned_window.add (frame2, weight=2)
paned_window.insert (1, frame3) # add frame 3 like arry (1,frame3) => (index1,frame3)
# paned_window.forget(1)
# frame 3 has no weight so it is no responsive (expand)
root.mainloop()