import tkinter
from tkinter import ttk
from tkinter import Menu

class Gui():

    def __init__(self):

        # create window object
        self.window = tkinter.Tk()
        self.window.iconbitmap(r'Z:\development\python\python.ico')
        self.window.title('Strong Password')
        self.window.resizable(False, False)

        # adding a menu bar
        self.menu_bar = Menu(self.window)
        self.window.config(menu=self.menu_bar)

        # adding a file menu to menu bar
        self.psswd_menu = Menu(self.menu_bar, tearoff=0)
        self.psswd_menu.add_command(label='Generate')
        self.psswd_menu.add_separator()
        self.psswd_menu.add_command(label='Check')
        self.menu_bar.add_cascade(label="Password", menu=self.psswd_menu)

        # adding a second menu to menu_bar
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label='About')
        self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

        # create inner frame
        self.mighty = ttk.LabelFrame(self.window)
        self.mighty.grid(column=0, row=0, padx=8, pady=4)

        self.window.mainloop()


    # def home(self):
    #     # create a label
    #     homeLabel1 = ttk.Label(self.mighty, text="Enter a name:")
    #     homeLabel1.grid(column=0, row=0)



main = Gui()





