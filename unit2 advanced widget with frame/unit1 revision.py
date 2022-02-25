from tkinter import *
from tkinter import ttk

class App:
    def __init__ (self, master):
        master.title ('Python')
        self.label = ttk.Label (master, text='Hello Tkinter')
        self.label.pack()
        self.button = ttk.Button(master, text='Change')
        self.button.pack()
        self.button.config(command=self.changeName)
        self.checkBut(master)
        self.radioBut(master)
        self.entryBox(master)
        self.comboBox(master)
        self.spinBox(master)
        self.progressBar(master)
        self.image(master)

    def changeName (self):
        self.label.config(text='Hello Python')
        self.label.config(font=('',20,''), foreground='red', background='black')

    def checkBut(self, master):
        self.c_var = StringVar()
        self.cdub_var = StringVar()
        self.python_var = StringVar()
        self.check_box1 = ttk.Checkbutton(master, text='C', variable=self.c_var)
        self.check_box1.config(onvalue='choose C ',offvalue='not choose C')
        self.check_box2 = ttk.Checkbutton(master, text='C++', variable=self.cdub_var)
        self.check_box2.config(onvalue='choose C++',offvalue='not choose C++')
        self.check_box3 = ttk.Checkbutton(master, text='Python', variable=self.python_var)
        self.check_box3.config(onvalue='choose Python',offvalue='not choose python')
        self.check_box1.pack()
        self.check_box2.pack()
        self.check_box3.pack()
    
    def radioBut(self, master):
        self.radio_var = StringVar()
        self.radio_but1 = ttk.Radiobutton(master, text='C',
         variable=self.radio_var, value='C')  
        self.radio_but2 = ttk.Radiobutton(master, text='C++',
         variable=self.radio_var, value='C++')  
        self.radio_but3 = ttk.Radiobutton(master, text='Python',
         variable=self.radio_var, value='Python')
        self.radio_but1.pack()
        self.radio_but2.pack()
        self.radio_but3.pack() 

    def entryBox(self, master):
        self.text_field = ttk.Entry(master, width=50)
        self.text_field.pack()

    def comboBox(self, master):
        self.combo_var = StringVar()
        self.drop_down = ttk.Combobox(master, textvariable=self.combo_var, 
        values=('C','C++','Python'))
        self.drop_down.pack()
    
    def spinBox(self, master):
        self.spin_var = StringVar()
        self.spin_box = Spinbox(master, textvariable=self.spin_var,
        from_=0 ,to=10)
        self.spin_box.pack()

    def progressBar(self, master):
        self.progress_var = DoubleVar()
        self.progress_bar = ttk.Progressbar (master,
         orient=HORIZONTAL, length=200)
        self.progress_bar.config(mode = 'determinate',
         maximum=11.0, variable=self.progress_bar)
        self.scale = ttk.Scale (master, orient=HORIZONTAL,
         variable=self.progress_bar, length=400, from_=0.0, to=11.0)
        self.progress_bar.pack()
        self.scale.pack()
    
    def image(self, master):
        self.img = PhotoImage (file=r'/home/minkhant/Python GUI/images/bird.png')
        # self.small_img = self.img.subsample(3,3)
        self.lab = ttk.Label(master, image=self.img) #image = self.small_img
        self.lab.pack()
        
def main () :
    root = Tk()
    myapp = App (root)
    root.mainloop()

main()