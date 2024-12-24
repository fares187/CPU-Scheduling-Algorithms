from tkinter import Tk, Label, StringVar, OptionMenu, Button, Toplevel, Entry, Frame, PhotoImage, messagebox
from algorithms import Algorithms
from process import Process
        
def create_process_objects():
    """Create a list of Process objects from the GUI input"""
    processes = []
    is_priority = "Priority" in selected_option.get()
    
    for i, row in enumerate(process_rows):
        p_id = f"P{i+1}"
        arrival_time = int(row[2].get())
        burst_time = int(row[1].get())
        
        if is_priority:
            priority = int(row[3].get())
            process = Process(p_id, arrival_time, burst_time, priority)
        else:
            process = Process(p_id, arrival_time, burst_time)
            
        processes.append(process)
    
    return processes

<<<<<<< HEAD
def get_algorithm_details():
    """Get algorithm name and quantum value if applicable"""
    algo_name = selected_option.get()
    if "Round Robin" in algo_name:
        return [algo_name, int(quantum_entry.get())]
    return [algo_name, None]

=======
from tkinter import Tk, Label, StringVar, OptionMenu, Button, Toplevel, Entry, Frame, PhotoImage, messagebox
import tkinter as ttk
from algorithms import Algorithms
from random import randint, choice
class Process:
    def __init__(self, p_id, arrival_time, burst_time, priority=None):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.runs = []
        self.response_time = None
        self.waiting_time = None
        self.turnaround_time = None
        
def create_process_objects():
    """Create a list of Process objects from the GUI input"""
    processes = []
    is_priority = "Priority" in selected_option.get()
    
    for i, row in enumerate(process_rows):
        p_id = f"P{i+1}"
        arrival_time = int(row[2].get())
        burst_time = int(row[1].get())
        
        if is_priority:
            priority = int(row[3].get())
            process = Process(p_id, arrival_time, burst_time, priority)
        else:
            process = Process(p_id, arrival_time, burst_time)
            
        processes.append(process)
    
    return processes

def get_algorithm_details():
    """Get algorithm name and quantum value if applicable"""
    algo_name = selected_option.get()
    if "Round Robin" in algo_name:
        return [algo_name, int(quantum_entry.get())]
    return [algo_name, None]

>>>>>>> 653213cd8cd77cd818d6656b9c027788bfadfff1
def create_window():
    if validate_inputs():
        # Create the tuple with algorithm details and process objects
        algo_details = get_algorithm_details()
        processes = create_process_objects()
<<<<<<< HEAD

        algo=Algorithms()
        match algo_details[0]:
            case "First Come First Served (FCFS)":
                processes=algo.fcfs(processes)
            case "Non-Preemptive Shortest Job First (SJF)":
                processes=algo.sjf_nonpreemptive(processes)
            case "Preemptive Shortest Job First (SJF)":
                processes=algo.sjf_preemptive(processes)
            case "Round Robin (RR)":
                processes=algo.round_robin(processes, algo_details[1])
            case "Preemptive Priority Scheduling":
                processes=algo.priority_non_preemptive(processes)
            case "Non-Preemptive Priority Scheduling":
                processes=algo.premptive_priority(processes)
        
        print(algo.sort_runtimes(processes))
        
=======
        print(processes)
>>>>>>> 653213cd8cd77cd818d6656b9c027788bfadfff1
        # Create new window to display the created objects
        new_window = Toplevel(window)
        new_window.geometry("600x400")
        new_window.title("Process Details")
<<<<<<< HEAD
        
=======
       
>>>>>>> 653213cd8cd77cd818d6656b9c027788bfadfff1
        # Display algorithm details
        Label(new_window, text="Algorithm Details:", font=("Verdana", 16, "bold")).pack(pady=10)
        Label(new_window, text=f"Algorithm: {algo_details[0]}", font=("Verdana", 12)).pack()
        if algo_details[1]:
            Label(new_window, text=f"Time Quantum: {algo_details[1]}", font=("Verdana", 12)).pack()
        
        # Display process objects
        Label(new_window, text="\nProcess Objects:", font=("Verdana", 16, "bold")).pack(pady=10)
        process_frame = Frame(new_window)
        process_frame.pack(padx=20, pady=10)
<<<<<<< HEAD
        
=======
        ############################################################################################################################333
        Sfactor=6
        colors =["#D1263D","#61D126","#44D126","#D19B26","#264ED1"]

        spacing_Frame=Frame(new_window,width=100,height=100)
        main_frame = Frame(new_window, bg="#FF0000",height=40,width=1000)
        secondry_frame= Frame(new_window,bg="red")
        # Create main frame


        main_frame.pack(expand=True, padx=10, pady=10,anchor="n")
        # spacing_Frame.grid(row=0,column=1,sticky="nsew")
        # main_frame.grid(row=1,column=1,sticky="nsew")
        # secondry_frame.grid(row=2,column=1,rowspan=1000,sticky="nsew")
        # Create a canvas
        canvas = ttk.Canvas(main_frame, width=1000000, height=40)

        # Create horizontal scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient='horizontal', command=canvas.xview)
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



        ############################################################################################################################
        # Headers
        headers = ["Process ID", "Arrival Time", "Burst Time"]
        if "Priority" in algo_details[0]:
            headers.append("Priority")
            
        for col, header in enumerate(headers):
            Label(process_frame, text=header, font=("Verdana", 12, "bold")).grid(row=0, column=col, padx=10, pady=5)
        
        # Process details
        for row, process in enumerate(processes, start=1):
            Label(process_frame, text=process.p_id).grid(row=row, column=0, padx=10, pady=2)
            Label(process_frame, text=str(process.arrival_time)).grid(row=row, column=1, padx=10, pady=2)
            Label(process_frame, text=str(process.burst_time)).grid(row=row, column=2, padx=10, pady=2)
            if process.priority is not None:
                Label(process_frame, text=str(process.priority)).grid(row=row, column=3, padx=10, pady=2)
      
# Main window setup remains the same
window = Tk()
window.geometry("1000x600")
window.title("OS CPU")

# Set window icon
icon = PhotoImage(file="image.png")
window.iconphoto(True, icon)

# Add title label
Label(window, text="CPU Scheduling Algorithms", font=("Verdana", 35)).pack(pady=20)

# Dropdown menu
selected_option = StringVar()
selected_option.set("Select an Algorithm")  # Default value

options = [
    "First Come First Served (FCFS)",
    "Non-Preemptive Shortest Job First (SJF)",
    "Preemptive Shortest Job First (SJF)",
    "Round Robin (RR)",
    "Preemptive Priority Scheduling",
    "Non-Preemptive Priority Scheduling"
]

dropdown = OptionMenu(window, selected_option, *options)
dropdown.pack(pady=20)

# Quantum Frame for Round Robin
quantum_frame = Frame(window)
quantum_label = Label(quantum_frame, text="Time Quantum:", font=("Verdana", 10))
quantum_entry = Entry(quantum_frame, width=10, justify='center')

# Header frame
header_frame = Frame(window)
header_frame.pack()

# Header labels - Centered text with consistent width
Label(header_frame, text="Process", width=10, font=("Verdana", 10), anchor="w").grid(row=0, column=0, padx=5)
Label(header_frame, text="Burst Time", width=15, font=("Verdana", 10), anchor="center").grid(row=0, column=1, padx=5)
Label(header_frame, text="Arrival Time", width=15, font=("Verdana", 10), anchor="w").grid(row=0, column=2, padx=5)
priority_label = Label(header_frame, text="Priority", width=15, font=("Verdana", 10), anchor="w")

# Container for process rows
process_frame = Frame(window)
process_frame.pack(pady=10)

# Track process rows
process_rows = []

def validate_integer_input(value):
    """Validate if the input is a positive integer"""
    if value == "": # Allow empty field for user to type
        return True
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def create_entry():
    """Create a standardized Entry widget with validation"""
    vcmd = (window.register(validate_integer_input), '%P')
    entry = Entry(process_frame, width=15, justify='center', validate='key', validatecommand=vcmd)
    return entry

def create_hidden_button():
    """Create a truly invisible button that maintains spacing but can't be interacted with"""
    button = Label(process_frame, width=4)  # Using Label instead of Button
    button.grid_remove()  # Initially hidden
    return button

def update_process_labels():
    """Update process labels to ensure they're in numerical order"""
    for i, row in enumerate(process_rows):
        row[0].config(text=f"P{i + 1}")

def update_rows(*args):
    is_priority = "Priority" in selected_option.get()
    is_round_robin = "Round Robin" in selected_option.get()

    # Show or hide the Priority header
    if is_priority:
        priority_label.grid(row=0, column=3, padx=5)
    else:
        priority_label.grid_forget()

    # Show or hide the Quantum input
    if is_round_robin:
        quantum_frame.pack(after=dropdown, pady=10)
        quantum_label.pack(side='left', padx=5)
        quantum_entry.pack(side='left', padx=5)
    else:
        quantum_frame.pack_forget()

    # Update existing rows
    for row_index, row in enumerate(process_rows):
        if is_priority and (len(row) == 5 or len(row) == 4):
            priority_entry = create_entry()
            priority_entry.grid(row=row_index + 1, column=3, padx=5, pady=5)
            
            button_index = -2 if len(row) == 5 else -1
            row.insert(3, priority_entry)
            
            row[button_index].grid(row=row_index + 1, column=4, padx=5, pady=5)
            if len(row) > 5:
                row[-1].grid(row=row_index + 1, column=5, padx=5, pady=5)
                
        elif not is_priority and (len(row) == 7 or len(row) == 6):
            row[3].grid_forget()
            row.pop(3)
            
            button_index = -2 if len(row) == 5 else -1
            row[button_index].grid(row=row_index + 1, column=3, padx=5, pady=5)
            if len(row) > 4:
                row[-1].grid(row=row_index + 1, column=4, padx=5, pady=5)

def remove_process_row(row):
    for widget in row:
        widget.grid_forget()
    process_rows.remove(row)

    # Re-align remaining rows
    is_priority = "Priority" in selected_option.get()
    for row_index, row in enumerate(process_rows):
        for col_index, widget in enumerate(row):
            widget.grid(row=row_index + 1, column=col_index, padx=5, pady=5)
    
    update_process_labels()

def add_process_row():
    process_index = len(process_rows) + 1
    is_priority = "Priority" in selected_option.get()

    # Process label - Centered text
    process_label = Label(process_frame, text=f"P{process_index}", width=15, font=("Verdana", 12), anchor="center")
    process_label.grid(row=process_index, column=0, padx=5, pady=5)

    # Entry fields with centered text
    burst_entry = create_entry()
    burst_entry.grid(row=process_index, column=1, padx=5, pady=5)

    arrival_entry = create_entry()
    arrival_entry.grid(row=process_index, column=2, padx=5, pady=5)

    row = [process_label, burst_entry, arrival_entry]
    
    next_column = 3
    if is_priority:
        priority_entry = create_entry()
        priority_entry.grid(row=process_index, column=next_column, padx=5, pady=5)
        row.append(priority_entry)
        next_column += 1

    # Add and remove buttons with consistent width
    add_button = Button(process_frame, text="+", width=3)
    add_button.configure(command=add_process_row)
    add_button.grid(row=process_index, column=next_column, padx=5, pady=5)
    row.append(add_button)

    if process_index > 1:
        remove_button = Button(process_frame, text="-", width=3)
        remove_button.configure(command=lambda: remove_process_row(row))
        remove_button.grid(row=process_index, column=next_column + 1, padx=5, pady=5)
        row.append(remove_button)
    else:
        # Add hidden button for the first row to maintain spacing
        hidden_button = create_hidden_button()
        hidden_button.grid(row=process_index, column=next_column + 1, padx=5, pady=5)
        row.append(hidden_button)

    process_rows.append(row)

def validate_inputs():
    if selected_option.get() == "Select an Algorithm":
        messagebox.showerror("Error", "Please select an algorithm first!")
        return False
    
    is_priority = "Priority" in selected_option.get()
    is_round_robin = "Round Robin" in selected_option.get()

    # Validate quantum for Round Robin
    if is_round_robin:
        if not quantum_entry.get():
            messagebox.showerror("Error", "Please enter a Time Quantum value!")
            return False
        try:
            quantum = int(quantum_entry.get())
            if quantum <= 0:
                messagebox.showerror("Error", "Time Quantum must be a positive integer!")
                return False
        except ValueError:
            messagebox.showerror("Error", "Time Quantum must be a positive integer!")
            return False

    # Validate process inputs
    for row in process_rows:
        if not row[1].get() or not row[2].get():
            messagebox.showerror("Error", "Please fill all Burst Time and Arrival Time fields!")
            return False
        if is_priority and len(row) >= 4 and not row[3].get():
            messagebox.showerror("Error", "Please fill all Priority fields!")
            return False
        
        try:
            # Validate each field is a positive integer
            burst_time = int(row[1].get())
            arrival_time = int(row[2].get())
            
            if burst_time <= 0:
                messagebox.showerror("Error", "Burst Time must be a positive integer!")
                return False
            if arrival_time < 0:
                messagebox.showerror("Error", "Arrival Time must be a non-negative integer!")
                return False
                
            if is_priority and len(row) >= 4:
                priority = int(row[3].get())
                if priority <= 0:
                    messagebox.showerror("Error", "Priority must be a positive integer!")
                    return False
        except ValueError:
            messagebox.showerror("Error", "All input fields must be positive integers!")
            return False

    return True

# Setup quantum entry validation
quantum_vcmd = (window.register(validate_integer_input), '%P')
quantum_entry.configure(validate='key', validatecommand=quantum_vcmd)

# Add the first process row
add_process_row()

# Bind dropdown changes to update rows
selected_option.trace_add("write", update_rows)

# Add Next button
btn = Button(window, text="Next", command=create_window)
btn.pack(pady=20)

# Run the application
window.mainloop()

<<<<<<< HEAD
print()
=======
print()





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
>>>>>>> 653213cd8cd77cd818d6656b9c027788bfadfff1
