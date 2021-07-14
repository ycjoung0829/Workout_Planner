
from tkinter import *
from PIL import ImageTk, Image


############## HELPER FUNCTIOn ################

### resizes a picture into a certain width and height 
def editPic(image, width, height):
    img = Image.open(image)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

##############################################


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mainPage= None
        self.allPages = dict()
        self.switch(Home)

    def switch(self, page):

        if self.mainPage:
            self.mainPage.pack_forget()

        canvas = self.allPages.get(page, False)

        if canvas == False:
            canvas = page(self)
            self.allPages[page] = canvas

        canvas.pack()
        self.mainPage = canvas

        
        
class Home(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg="white",width = 512, height = 512)

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("calendar_icon.png", 50,50)
        
        
        routine = Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        calendar = Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        home = Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(0,60,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(0,120,anchor="nw", window=calendar)
        
        
        
        
        self.image = ImageTk.PhotoImage(file="barbell-512.png")
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")


class Routine(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg="blue",width = 512, height = 512)

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("calendar_icon.png", 50,50)
        
        
        routine = Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        calendar = Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        home = Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(0,60,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(0,120,anchor="nw", window=calendar)
        
        
        
        
        self.image = ImageTk.PhotoImage(file="barbell-512.png")
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")


class Calendar(Frame): 
    def __init__(self, master, *args, **kwargs):
        
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg="yellow",width = 512, height = 512)

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("calendar_icon.png", 50,50)
        
        
        routine = Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        calendar = Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        home = Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(0,60,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(0,120,anchor="nw", window=calendar)
        
        
        
        
        self.image = ImageTk.PhotoImage(file="barbell-512.png")
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()