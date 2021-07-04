
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
            Frame.__init__(self, width=300, height=300, *args, **kwargs)
            home = Home(self)
            routine = Routine(self)
            calendar = Calendar(self)

            # buttonframeH = Frame(self)
            # buttonframeR = Frame(self)
            # buttonframeC = Frame(self)
            buttonframe = Frame(self)
            
            container = Frame(self)
            #buttonframeH.pack(side="top", anchor = "w", fill="x", expand=False)
            #buttonframeR.pack(side="left", anchor = "w", fill="x", expand=False)
            #buttonframeC.pack(side="bottom", anchor = "w", fill="x", expand=False)
            buttonframe.pack(side="top", fill="x", expand=False)
            
            container.pack(side="top", fill="both", expand=True)

            home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            routine.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            calendar.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

            b1 = Button(buttonframe, text="Home", font = FONT, command=home.switch)
            b2 = Button(buttonframe, text="Routine", font = FONT, command=routine.switch)
            b3 = Button(buttonframe, text="Calendar", font = FONT, command=calendar.switch)

            b1.pack(side="left")
            b2.pack(side="left")
            b3.pack(side="left")

            home.switch()

    root = Tk()
    app = App(root)
    app.pack(side="top", fill="both", expand=True)
    root.wm_geometry("%dx%d" % (width, height))
    root.mainloop()
    


run(512, 512)
