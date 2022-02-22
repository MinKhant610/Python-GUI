from tkinter import * 
from tkinter import ttk

root = Tk () 
button = ttk.Button (root , text = 'Click Me')
button.pack()
img = PhotoImage (file = '//home//minkhant//Python GUI//images//bird.png')
small_img = img.subsample(4,4)
button.config (image = small_img, compound = LEFT)
root.mainloop()