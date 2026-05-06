
import tkinter as tk
import tkinter as tk
from tkinter import ttk

def show_total():
   
    num1 = float(entry_aap.get())
    num2 = float(entry_m2.get())
    num3 = float(entry_dms.get())
    num4 = float(entry_oop.get())
    
    result = num1 + num2 + num3 + num4
    
  
    total_result_label.config(text=str(result))

def show_average():
    num1 = float(entry_aap.get())
    num2 = float(entry_m2.get())
    num3 = float(entry_dms.get())
    num4 = float(entry_oop.get())
    
    result = (num1 + num2 + num3 + num4) / 4
    
    avg_result_label.config(text=str(result))
    # total_result_label.config(text="")


window = tk.Tk()
window.title("SIUT")
window.geometry("500x800")


title_label = ttk.Label(window, text="Marks Calculator", font=("Arial", 20))
title_label.pack(pady=20)


ttk.Label(window, text="S-Number:", font=("Arial", 12)).pack()
entry_snum = ttk.Entry(window, width=30)
entry_snum.pack(pady=5)

ttk.Label(window, text="S-Name:", font=("Arial", 12)).pack()
entry_sname = ttk.Entry(window, width=30)
entry_sname.pack(pady=5)

ttk.Label(window, text="AAP-Marks:", font=("Arial", 12)).pack()
entry_aap = ttk.Entry(window, width=30)
entry_aap.pack(pady=5)

ttk.Label(window, text="M2 marks:", font=("Arial", 12)).pack()
entry_m2 = ttk.Entry(window, width=30)
entry_m2.pack(pady=5)

ttk.Label(window, text="DMS marks:", font=("Arial", 12)).pack()
entry_dms = ttk.Entry(window, width=30)
entry_dms.pack(pady=5)

ttk.Label(window, text="oop marks:", font=("Arial", 12)).pack()
entry_oop = ttk.Entry(window, width=30)
entry_oop.pack(pady=5)






total_button = ttk.Button(window, text="TOTAL", width=20, command=show_total)
total_button.pack(pady=10)

total_result_label = ttk.Label(window, text="", font=("Arial", 15, "bold"))
total_result_label.pack()


avg_button = ttk.Button(window, text="AVERAGE", width=20, command=show_average)
avg_button.pack(pady=10)

avg_result_label = ttk.Label(window, text="", font=("Arial", 15, "bold"))
avg_result_label.pack()






window.mainloop()   
