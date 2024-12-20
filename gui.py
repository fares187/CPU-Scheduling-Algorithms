
from tkinter import *

window = Tk()
window.geometry("1000x600")
window.title("OS CPU")
icon= PhotoImage(file="image.png")
window.iconphoto(True,icon)
Label(window, text="CPU Scheduling Algorithms", font=("Verdana", 35)).pack()
selected_option = StringVar()
selected_option.set("Select an Algorithm")  # Set default value

# Create the OptionMenu
options = [" First Come First Served (FCFS)", "Non-Preemptive Shortest Job First (SJF)",
            "Preemptive Shortest Job First (SJF)", "Round Robin (RR)",
            "Preemptive Priority Scheduling","Preemptive Priority Scheduling"
            ]
dropdown = OptionMenu(window, selected_option, *options).pack()

def create_window():
    new_Window = Toplevel()
    

btn = Button(window, text="Next",command=create_window).pack()
window.mainloop()





# LARGEFONT =("Verdana", 35)
  
# class tkinterApp(Tk):
     
#     # __init__ function for class tkinterApp 
#     def __init__(self): 
         
#         # __init__ function for class Tk
#         Tk.__init__(self)
         
#         # creating a container
#         container = Frame(self)  
#         container.pack(side = "top", fill = "both", expand = True) 
        
#         container.grid_rowconfigure(0, weight = 1)
#         container.grid_columnconfigure(0, weight = 1)
#         Label(container,text="ahmed fares").grid(row = 1, column = 0, sticky ="nsew")

  
#         # initializing frames to an empty array
#         self.frames = {}  
  
#         # iterating through a tuple consisting
#         # of the different page layouts
#         for F in (StartPage, Page1, Page2):
  
#             frame = F(container, self)
#                    #frame(contain, prore)
  
#             # initializing frame of that object from
#             # startpage, page1, page2 respectively with 
#             # for loop
#             self.frames[F] = frame 
  
#             frame.grid(row = 0, column = 0, sticky ="nsew")
  
#         self.show_frame(StartPage)
  
#     # to display the current frame passed as
#     # parameter
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()
  
# # first window frame startpage
  
# class StartPage(Frame):
#     def __init__(self, parent, controller): 
#         Frame.__init__(self, parent)
         
#         # label of frame Layout 2
#         label =  Label(self, text ="Startpage", font = LARGEFONT)
#         self.configure(bg="#FF0000")
#         # putting the grid in its place by using
#         # grid
#         label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
#         button1 = Button(self, text ="Page 1",
#         command = lambda : controller.show_frame(Page1))
     
#         # putting the button in its place by
#         # using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         ## button to show frame 2 with text layout2
#         button2 =  Button(self, text ="Page 2",
#         command = lambda : controller.show_frame(Page2))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# # second window frame page1 
# class Page1( Frame):
     
#     def __init__(self, parent, controller):
         
#         Frame.__init__(self, parent)
#         label =  Label(self, text ="Page 1", font = LARGEFONT)
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button1 = Button(self, text ="StartPage",
#                             command = lambda : controller.show_frame(StartPage))
     
#         # putting the button in its place 
#         # by using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button2 = Button(self, text ="Page 2",
#                             command = lambda : controller.show_frame(Page2))
     
#         # putting the button in its place by 
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# # third window frame page2
# class Page2( Frame): 
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = Label(self, text ="Page 2", font = LARGEFONT)
#         label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
#         # button to show frame 2 with text
#         # layout2
#         button1 = Button(self, text ="Page 1",
#                             command = lambda : controller.show_frame(Page1))
     
#         # putting the button in its place by 
#         # using grid
#         button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
#         # button to show frame 3 with text
#         # layout3
#         button2 = Button(self, text ="Startpage",
#                             command = lambda : controller.show_frame(StartPage))
     
#         # putting the button in its place by
#         # using grid
#         button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
# # Driver Code
# app = tkinterApp()
# app.mainloop()