from tkinter import * 

root = Tk () 
textbox = Text (root, width=50, height=20)
textbox.pack()
textbox.config (wrap = 'word')
# textbox.insert ('1.0 + 2 lines', 'insert message')
root.mainloop()