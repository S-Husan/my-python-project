import tkinter as tk
from tkinter import ttk

# Создаем главное окно
window = tk.Tk()
window.title("Converter App")
window.geometry("400x300")

# 10 #create a label
# 11 
label = ttk.Label(window, text="Welcome to the Convertor App", font=("Helvetica", 16))
# 12 
label.pack(pady=20)

# 14 #create input frame
# 15 
input_frame = ttk.Frame(window)
# 16 
input_frame.pack(pady=10)

# 18 #create a label and entry
# 19 
input_label = ttk.Label(input_frame, text="Enter value to convert:")
# 20 
input_label.pack(side=tk.LEFT, padx=5)
# 21 
input_entry = ttk.Entry(input_frame)
# 22 
input_entry.pack(side=tk.LEFT, padx=5)

# 24 #create button
# 25 
calculate_button = ttk.Button(input_frame, text="Calculate")
# 26 
calculate_button.pack()

# Запуск приложения
window.mainloop()