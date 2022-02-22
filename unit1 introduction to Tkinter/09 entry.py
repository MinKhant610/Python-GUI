#entry or text field 

from tkinter import *
from tkinter import ttk

root = Tk () 

text_area1 = ttk.Entry (root, width=30)
text_area1.pack()
text_area2 = ttk.Entry (root, width=30)
text_area2.pack()
text_area3 = ttk.Entry (root, width=30)
text_area3.pack()
text_area4 = ttk.Entry (root, width=30)
text_area4.pack()

#text_area2.state(['readonly'])
text_area3.state(['disabled'])
text_area4.config (show='*')
#we can get entry data using text_area1.get()
root.mainloop()