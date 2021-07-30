
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image



############## HELPER FUNCTIOn ################

### resizes a picture into a certain width and height 
def editPic(image, width, height):
    img = Image.open(image)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def click(workout, routines):
    routines.append(workout)
    

##############################################
WIDTH = 414
HEIGHT = 736
routines = []


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
        self.canvas = Canvas(self, bg="white",width = WIDTH, height = HEIGHT)
    
        self.routine_image = editPic("workout_pic.png", WIDTH,WIDTH)
        self.calendar_image = editPic("calendar_icon.png", WIDTH,WIDTH)
        
        routine = ttk.Button(self,image = self.routine_image,
              command=lambda: master.switch(Routine))
        routine.pack(fill="x")
        
        calendar = ttk.Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        
        routine_window = self.canvas.create_window(WIDTH//2, 0,anchor = "n", window=routine)
        calendar_window = self.canvas.create_window(WIDTH//2,HEIGHT//2, anchor = "n", window=calendar)
        
        
    
        self.image = editPic("workout_pic.png", WIDTH, WIDTH)
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")


class Routine(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self,width = WIDTH, height = HEIGHT)

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("calendar_icon.png", 50,50)
        
        
        routine = ttk.Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        calendar = ttk.Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        home = ttk.Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        
        ##########body parts###############
        
        self.bicep = editPic("bicep.png", WIDTH//2, WIDTH//2)
        
        bicep = ttk.Button(self, image = self.bicep,
             command=lambda: click("bicep", routines))
        
        for routine in routines:
            self.canvas.create_text(50, 500, text=routine)
        
        bicep_window = self.canvas.create_window(0,60,anchor="nw", window=bicep)
        ###################################
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(60,0,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(120,0,anchor="nw", window=calendar)
        
        self.canvas.pack(expand=False, fill="both")
        
        
        

class Calendar(Frame): 
    def __init__(self, master, *args, **kwargs):
        
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self,width = WIDTH, height = HEIGHT)

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("calendar_icon.png", 50,50)
        
        
        routine = ttk.Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        calendar = ttk.Button(self, image=self.calendar_image,
              command=lambda: master.switch(Calendar))
        
        home = ttk.Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(0,60,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(0,120,anchor="nw", window=calendar)
        
        
        
        
        self.image = editPic("workout_pic.png", WIDTH, WIDTH)
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()