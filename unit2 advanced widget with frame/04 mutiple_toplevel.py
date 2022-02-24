from tkinter import * 
from tkinter import ttk

#This is code is not dry . But You can dry with OOP

def topLevel2():
    top2 = Toplevel()
    top2.title ('TOP2')
    top2.geometry('400x400')
    label = ttk.Label(top2, text='This is toplevel2 window').pack()
    button1 = ttk.Button (top2, text='Exit', command=top2.destroy)
    button1.pack()

def topLevel1():
    top1 = Toplevel()
    top1.title ('TOP1')
    top1.geometry('400x400')
    label = ttk.Label(top1, text='This is toplevel1 window').pack()
    button1 = ttk.Button (top1, text='Exit', command=top1.destroy)
    button1.pack()
    button2 = ttk.Button (top1, text='Open toplevel2', command=topLevel2).pack()

root = Tk () 
root.title ('Main Windoow')
root.geometry('600x400')
label = ttk.Label (root, text='This is main window').pack()
button = ttk.Button (root, text='Open toplevel 1', command=topLevel1)
button.pack()
root.mainloop()
