# three type of geometry manager 
# pack , place , grid 
# pack and grid cannot use at the same time 


from tkinter import * 
from tkinter import ttk

root = Tk () 

pack_but = ttk.Button(root, text = 'pack geo')
#grid_but = ttk.Button (root, text = 'grid geo')
place_but = ttk.Button (root, text = 'place geo')

pack_but.pack (side = RIGHT) # or side = 'right'
#grid_but.grid (row = 0 , column = 8)
place_but.place (x = 50, y = 70)
root.mainloop()