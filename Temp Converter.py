import tkinter as tk
from tkinter import messagebox

def c_to_f():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        result_label.config(text=f"{c}°C = {f:.2f}°F")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")

def f_to_c():
    try:
        f = float(entry.get())
        c = (f - 32) * 5/9
        result_label.config(text=f"{f}°F = {c:.2f}°C")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")

root = tk.Tk()
root.title("Conversor de Temperatura")

tk.Label(root, text="Digite a temperatura:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Celsius → Fahrenheit", command=c_to_f).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Fahrenheit → Celsius", command=f_to_c).grid(row=0, column=1, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
