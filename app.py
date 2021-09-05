
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk, Image

from datetime import datetime
dt = datetime.today()



############## HELPER FUNCTIOn ################

### resizes a picture into a certain width and height 
def editPic(image, width, height):
    img = Image.open(image)
    img = img.resize((width, height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

# def click(workout, routines):
#     routines.append(workout)
    

##############################################
WIDTH = 414
HEIGHT = 736
count = 0


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mainPage= None
        self.allPages = dict()
        self.switch(Home)
        self.count = 0
        self.routines = set()
        self.txt = ""
        self.createT = ""
        self.hey = ""

    def switch(self, page):

        if self.mainPage:
            self.mainPage.pack_forget()

        canvas = self.allPages.get(page, False)

        if canvas == False:
            canvas = page(self)
            self.allPages[page] = canvas

        canvas.pack()
        self.mainPage = canvas
        
    
    
    def click(self, canvas, workout):
        canvas.delete(self.hey)
        self.txt = ""
        if self.count < 3:
            self.routines.add(workout)
            
        self.count+=1
            
        if self.count == 3:
            for r in self.routines:
                self.txt += r + ", "
            self.createT = canvas.create_text(50, HEIGHT, anchor = "sw", text =self.txt, font = ("Purisa", 20))
    
    def erase(self, canvas):
        canvas.delete(self.createT)
        self.routines = set()
        self.txt = ""
        self.count = 0
        
        
            
            
    
        
class Home(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self, bg="white",width = WIDTH, height = HEIGHT)
    
        self.routine_image = editPic("dumbell.png", WIDTH,WIDTH)
        self.calendar_image = editPic("routine.png", WIDTH,WIDTH)
        
        routine = ttk.Button(self,image = self.routine_image,
              command=lambda: master.switch(Routine))
        routine.pack(fill="x")
        
        calendar = ttk.Button(self, image=self.calendar_image,
              command=lambda: master.switch(Routine2))
        
        
        routine_window = self.canvas.create_window(WIDTH//2, 0,anchor = "n", window=routine)
        calendar_window = self.canvas.create_window(WIDTH//2,HEIGHT//2, anchor = "n", window=calendar)
        
        
    
        self.image = editPic("workout_pic.png", WIDTH, WIDTH)
        self.canvas.create_image(0,0, image=self.image, anchor="nw")
        
        self.canvas.pack(expand=False, fill="both")

        

class Routine(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self,width = WIDTH, height = HEIGHT)
        
        
        ###buttons####
        
        

        self.home_image = editPic("home_icon.png", 50, 50)
        # self.routine_image = editPic("routine_icon.png", 50,50)
        self.calendar_image = editPic("routine.png", 50,50)
        
        self.canvas.create_rectangle(0,0, WIDTH,HEIGHT, fill='white')
        
        # routine = ttk.Button(self, image = self.routine_image,
        #       command=lambda: master.switch(Routine))
        
        calendar = ttk.Button(self, image=self.calendar_image,
              command=lambda: master.switch(Routine2))
        
        home = ttk.Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        clear = ttk.Button(self, text="clear",
              command=lambda: master.erase(self.canvas))
        
        confirm = ttk.Button(self, text="next",
              command=lambda: master.switch(Routine2))
        
        ##########bicep###############
        
        self.bicep = editPic("bicep.png", WIDTH//2, WIDTH//2)
        
        bicep = ttk.Button(self, image = self.bicep,
             command=lambda: master.click(self.canvas, "bicep"))
        
        
        bicep_window = self.canvas.create_window(0,60,anchor="nw", window=bicep)
        
        ##########chest###############
        self.chest = editPic("chest_workout.png", WIDTH//2, WIDTH//2)
        
        chest = ttk.Button(self, image = self.chest,
             command=lambda: master.switch(Chest))
        
        
        chest_window = self.canvas.create_window(WIDTH//2,60,anchor="nw", window=chest)
        
        ##########shoulder############
        self.shoulder = editPic("shoulder.png", WIDTH//2, WIDTH//2)
        
        shoulder = ttk.Button(self, image = self.shoulder,
             command=lambda: master.click(self.canvas, "shoulder"))
        
        
        shoulder_window = self.canvas.create_window(0,WIDTH//2+70,anchor="nw", window=shoulder)
        ##########leg############
        self.leg = editPic("leg.png", WIDTH//2, WIDTH//2)
        
        leg = ttk.Button(self, image = self.leg,
             command=lambda: master.click(self.canvas, "leg"))
        
        
        leg_window = self.canvas.create_window(WIDTH//2,WIDTH//2+70,anchor="nw", window=leg)
        ##########tricep############
        self.tricep = editPic("tricep.png", WIDTH//2, WIDTH//2)
        
        tricep = ttk.Button(self, image = self.tricep,
             command=lambda: master.click(self.canvas, "tricep"))
        
        
        tricep_window = self.canvas.create_window(0,2*WIDTH//2+70,anchor="nw", window=tricep)
        ##########abs############
        self.abs = editPic("abs.png", WIDTH//2, WIDTH//2)
        
        abs = ttk.Button(self, image = self.abs,
             command=lambda: master.click(self.canvas, "abs"))
        
        
        abs_window = self.canvas.create_window(WIDTH//2,2*WIDTH//2+70,anchor="nw", window=abs)
        ##############################
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        # routine_window = self.canvas.create_window(60,0,anchor="nw", window=routine)
        calendar_window = self.canvas.create_window(60,0,anchor="nw", window=calendar)
        clear_window = self.canvas.create_window(240, 0, anchor="nw", window=clear)
        confirm_window = self.canvas.create_window(300,0, anchor="nw", window=confirm)
        
        self.canvas.pack(expand=False, fill="both")


class Chest(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self,width = WIDTH, height = HEIGHT)
        ###buttons####
        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine.png", 50,50)
        
        self.canvas.create_rectangle(0,0, WIDTH,HEIGHT, fill='white')
        
        routine = ttk.Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        home = ttk.Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(60,0,anchor="nw", window=routine)
        
        #####################################
        self.benchpress = editPic("chest_workout.png", WIDTH//2,WIDTH//2)
        
        benchpress = ttk.Button(self, image = self.benchpress)
        
        benchpress_window = self.canvas.create_window(0,50, anchor="nw", window=benchpress)
        ########
        self.dumbellpress = editPic("dumbell_press.png", WIDTH//2,WIDTH//2)
        
        dumbellpress = ttk.Button(self, image = self.dumbellpress)
        
        dumbellpresss_window = self.canvas.create_window(0,50+WIDTH//2, anchor="nw", window=dumbellpress)
        ########
        self.dumbellfly = editPic("dumbell_fly.png", WIDTH//2,WIDTH//2)
        
        dumbellfly = ttk.Button(self, image = self.dumbellfly)
        
        dumbellfly_window = self.canvas.create_window(0,50+WIDTH, anchor="nw", window=dumbellfly)
        ########
        self.incline = editPic("incline_bench.png", WIDTH//2,WIDTH//2)
        
        incline = ttk.Button(self, image = self.incline)
        
        incline_window = self.canvas.create_window(WIDTH//2,50, anchor="nw", window=incline)
        ########
        
        self.canvas.pack(expand=False, fill="both")
          

class Routine2(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.canvas = Canvas(self,width = WIDTH, height = HEIGHT)
        ###buttons####

        self.home_image = editPic("home_icon.png", 50, 50)
        self.routine_image = editPic("routine.png", 50,50)
        
        self.canvas.create_rectangle(0,0, WIDTH,HEIGHT, fill='white')
        
        routine = ttk.Button(self, image = self.routine_image,
              command=lambda: master.switch(Routine))
        
        home = ttk.Button(self, image=self.home_image,
              command=lambda: master.switch(Home))
        
        
        
        home_window = self.canvas.create_window(0,0, anchor="nw", window=home)
        routine_window = self.canvas.create_window(60,0,anchor="nw", window=routine)
        
        
        self.canvas.pack(expand=False, fill="both")
        
        
        

        

if __name__ == "__main__":
    app = App()
    app.mainloop()