from tkinter import * 
from tkinter import ttk 

root = Tk () 

frame = ttk.Frame(root, width=300, height=400)
frame.config(relief=SOLID, padding=(20,40)) # (left/right,top/button)
frame.pack()
label = ttk.Label(frame, text='Hello Tkinter', foreground='blue')
label.config (padding=(10,10))
label.pack()
button = ttk.Button(frame, text='Click Me')
button.pack()
frame2 = ttk.LabelFrame (root, width = 100, height=100, text='Python')
frame2.pack()

root.mainloop()