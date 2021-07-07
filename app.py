from tkinter import *


FONT = ("Verdana", 30)
Hfont = ("Verdana", 30)
Htext = "Home"
Rfont = ("Verdana", 30)
Rtext = "Routine"
Cfont = ("Verdana", 30)
Ctext = "Calendar"


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def switch(self):
        self.lift()


class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text=Htext, font = Hfont)
        label.pack(side="top", fill="both", expand=True)


class Routine(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text=Rtext, font = Rfont)
        label.pack(side="top", fill="both", expand=True)


class Calendar(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text=Ctext, font = Cfont)
        label.pack(side="top", fill="both", expand=True)


def run(width=300, height=300):

    class App(Frame):
        def __init__(self, *args, **kwargs):
            Frame.__init__(self, *args, **kwargs)
            home = Home(self)
            routine = Routine(self)
            calendar = Calendar(self)

            buttonframe = Frame(self)
            
            container = Frame(self)
            
            buttonframe.pack(side="top", fill="none", expand=False)
            
            container.pack(side="top", fill="both", expand=True)

            home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            routine.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            calendar.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

            b1 = Button(buttonframe, text="Home", font = FONT, fg="white", bg='black', command=home.switch)
            b2 = Button(buttonframe, text="Routine", font = FONT, fg="white", bg='black', command=routine.switch)
            b3 = Button(buttonframe, text="Calendar", font = FONT, fg="white", bg='black', command=calendar.switch)

            b1.pack(side = "left", pady = 2)
            b2.pack(side = "left", pady = 2)
            b3.pack(side = "left", pady = 2)

            home.switch()

    root = Tk()
    root.geometry("%dx%d" % (width, height))
    img = PhotoImage(file="barbell-512.png")
    # label = Label(root, image = img)
    # label.place(x=0,y=0)
    canvas = Canvas(root, width = 512, height = 512)
    canvas.pack(fill="both")
    canvas.create_image(0,0,image=img, anchor="nw")
    app = App(canvas)
    app.pack(side="top", fill="both", expand=True)
    root.mainloop()
    


run(512, 512)