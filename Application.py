import tkinter as tk
from tkinter import ttk

def convert(event=None):
    try:
        miles = float(username_entry.get())
        km = miles * 1.6
        output_label.config(text=f"{miles} miles = {km:.2f} km")
    except ValueError:
        output_label.config(text="Please enter a valid number for miles.")


def clear():
    username_entry.delete(0, tk.END)
    output_label.config(text="KM will be displayed here:")

# Creating a window
window = tk.Tk()

# Title
window.title("Milenia, The Blade of Miquella")

# Size
window.geometry("777x777")
# Create label  ====> to disolay a text
label = ttk.Label(window,text="Enter your UserName: ",font=("Arial", 20))
label.pack(pady=50)

# Create label  
label = ttk.Label(window,text="Enter your Password: ",font=("Arial", 20))
label.pack(pady=10)

# Frame input
input_frame=ttk.Frame(window)
input_frame.pack(pady=10)

# Input 
input_label = ttk.Label(input_frame,text = "Enter miles: ")
input_label.pack(side=tk.LEFT,padx=5)
username_entry = ttk.Entry(input_frame,font=("Arial",12))
username_entry.pack(side=tk.RIGHT,padx = 5)
username_entry.bind("<Return>", convert)

# Create the buttons
calculate_button = ttk.Button(input_frame,text="Calculate",command=convert)
calculate_button.pack(side=tk.LEFT, padx=5)
clear_button = ttk.Button(input_frame,text="Clear",command=clear)
clear_button.pack(side=tk.LEFT, padx=5)

# Output label
output_label = ttk.Label(window,text="KM will be displayed here: ", font = ("Helvetica", 14))
output_label.pack(pady = 20)

# Run application
window.mainloop()