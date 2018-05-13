import tkinter
from tkinter import ttk, Menu


class Main(tkinter.Tk):

    def __init__(self):

        tkinter.Tk.__init__(self) # container
        mighty = tkinter.Frame(self)
        mighty.grid(column=0, row=0, padx=10, pady=10)

        self.frames = {}

        for F in (HomePage, GeneratePage): # add a page here if you add a new one
            page = F(mighty, self)
            self.frames[F] = page
            page.grid(row=0, column=0, sticky = 'nsew')

        self.show_frame(HomePage)

    def show_frame(self, page): # method that changes the page
        frame=self.frames[page]
        frame.tkraise()


class HomePage(tkinter.Frame): # starting page

    def __init__(self, parent, controller):

        tkinter.Frame.__init__(self)

        label = tkinter.Label(self, text='Do you want to check your password or generate one?')
        label.grid(column=0 ,row=0, columnspan=3, padx=10, pady=10)

        btn1 = tkinter.Button(self, text="Generate",
                              command=lambda: controller.show_frame(GeneratePage)) # method that changes the page
        btn1.grid(column=0, row=1, padx=10, pady=30)

        btn2 = tkinter.Button(self, text="Create",
                              command=lambda: controller.show_frame(GeneratePage)) # method that changes the page
        btn2.grid(column=2, row=1, padx=10, pady=30)


class GeneratePage(tkinter.Frame): # second page

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self)
        label = tkinter.Label(self, text='Page One!!!')
        label.grid(column=0 ,row=0)


app = Main()
app.mainloop()




