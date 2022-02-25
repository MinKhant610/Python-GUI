from tkinter import * 
from tkinter import ttk 

root = Tk () 
notebook = ttk.Notebook (root)
notebook.pack()
frame1 = ttk.Frame (notebook)
frame2 = ttk.Frame (notebook)
frame3 = ttk.Frame (notebook)
ttk.Button(frame1, text='Click Me').pack()
notebook.add (frame1, text='One')
notebook.add (frame2, text='Two')
notebook.insert (1, frame3, text='Three')
root.mainloop()
