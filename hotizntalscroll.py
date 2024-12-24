from tkinter import *
from random import randint, choice
from process import Process
from algorithms import Algorithms
Sfactor=6
colors =["#D1263D","#61D126","#44D126","#D19B26","#264ED1"]
processes = [
   Process(1, 0, 5, runs=[[1, 4],[12, 16]]),
   Process(2, 1, 3, runs=[[5, 6]]),
   Process(3, 2, 4, runs=[[7, 10]])
]
print(Algorithms(processes).sort_runtimes())

root = Tk()
root.geometry("1000x600")
root.title("Horizontal Scrollable Labels")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)

spacing_Frame=Frame(root,width=100,height=100)
main_frame = Frame(root, bg="#FF0000",height=40)
secondry_frame= Frame(root,bg="red")
# Create main frame


main_frame.pack(expand=True, padx=10, pady=10,anchor="n")
# spacing_Frame.grid(row=0,column=1,sticky="nsew")
# main_frame.grid(row=1,column=1,sticky="nsew")
# secondry_frame.grid(row=2,column=1,rowspan=1000,sticky="nsew")
# Create a canvas
canvas = Canvas(main_frame, width=1000000, height=40)

# Create horizontal scrollbar
scrollbar = Scrollbar(main_frame, orient='horizontal', command=canvas.xview)
scrollbar.pack(side='bottom', fill='x')

# Configure canvas
canvas.configure(xscrollcommand=scrollbar.set)
canvas.pack(expand=True, fill='both')

# Create frame inside canvas to hold labels
inner_frame = Frame(canvas)
inner_frame.rowconfigure(0,weight=1)
canvas.create_window((0, 0), window=inner_frame, anchor='nw')

# Add some sample labels
sample_texts = [f"Label {i}" for i in range(1, 21)]
labels = []

# for i, text in enumerate(sample_texts):
#     mm=randint(5,30)
#     inner_frame.columnconfigure(i,weight=mm)
#     label = Label(inner_frame,width= mm,
#                         background= choice(["#D1263D","#61D126","#44D126","#D19B26","#264ED1"]),
#                         height=2, text=mm)
#     # label.pack(side="right")
#     label.grid(column=mm,row=0)
#     labels.append(label)
####################################################################3
# kturn =-1
# for i in range((max(end_time for p in processes for start_time, end_time in p.runs))+1):
#     if(kturn>i):
#         continue
    
#     for p in Algorithms(processes).sort_runtimes():
#         if(i==p[1][0]):
#             inner_frame.columnconfigure(i,weight=(p[1][1]-p[1][0]))
#             kturn=p[1][1]
#             label = Label(inner_frame,width= (p[1][1]-p[1][0]),
#                         background= choice(["#D1263D","#61D126","#44D126","#D19B26","#264ED1"]),
#                         height=2, text="p"+str(p[0]))
#             inner_frame.columnconfigure(i,weight=(p[1][1]-p[1][0]))
#             label.grid(column=i,row=0,sticky="ew")
#             labels.append(label)
#             continue
    
#     inner_frame.columnconfigure(i,weight=1)
#     label = Label(inner_frame,width= (1),
#                         background= "#FFFFFF",
#                         height=2, text=" ")
#     inner_frame.columnconfigure(i,weight=1)
#     label.grid(column=i,row=0,sticky="ew")
#     labels.append(label)
#####################################################################################################333

kturn =-1
chooosed="#D19B26"
for i in range((max(end_time for p in processes for start_time, end_time in p.runs)+1)*Sfactor):
    if(kturn>i):
        continue
    try:
        for p in Algorithms(processes).sort_runtimes():
            if(i==p[1][0] *Sfactor   ):
                
                chooosed=choice([m for m in colors if m!=chooosed])
               # inner_frame.columnconfigure(i  ,weight=(p[1][1]-p[1][0])  *Sfactor )
                kturn=(p[1][1]+1)*Sfactor
                label = Label(inner_frame,width= (p[1][1]-p[1][0]) *Sfactor  ,
                            background=chooosed,
                            height=2, text="p"+str(p[0]))
                inner_frame.columnconfigure(i     ,weight=(1+(p[1][1]-p[1][0])) *Sfactor  )
                label.grid(column=i   *Sfactor,row=0,sticky="ew")
                labels.append(label)
                
                raise "asdfasdf"
        
        #inner_frame.columnconfigure(i  *Sfactor,weight=1*Sfactor    )
        label = Label(inner_frame,width= (1)   *(Sfactor),
                            background= "#FFFFFF",
                            height=2, text="")
        inner_frame.columnconfigure(i    ,weight=1   *(Sfactor) )
        label.grid(column=i  *(Sfactor),row=0,sticky="ew")
        labels.append(label)
    except Exception:
        continue












    # label.pack(side="right")
    

# Update scroll region after adding labels
inner_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'))

def on_mousewheel(event):
# Shift + MouseWheel for horizontal scrolling
    if event.state == 1:  # Shift is being held
        canvas.xview_scroll(int(-1 * (event.delta / 220)), 'units')
    else:
        canvas.xview_scroll(int(-1 * (event.delta / 220)), 'units')
# Bind mouse wheel for horizontal scrolling
canvas.bind('<MouseWheel>', on_mousewheel)
canvas.bind('<Shift-MouseWheel>', on_mousewheel)



root.mainloop()