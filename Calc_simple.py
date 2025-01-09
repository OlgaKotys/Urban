import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "addition"
    entry.delete(0, tk.END)

def button_subtract():
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "subtraction"
    entry.delete(0, tk.END)

def button_multiply():
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "multiplication"
    entry.delete(0, tk.END)

def button_divide():
    global first_number
    global math_operation
    first_number = float(entry.get())
    math_operation = "division"
    entry.delete(0, tk.END)

def button_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(0, first_number + second_number)
    elif math_operation == "subtraction":
        entry.insert(0, first_number - second_number)
    elif math_operation == "multiplication":
        entry.insert(0, first_number * second_number)
    elif math_operation == "division":
        if second_number == 0:
            entry.insert(0, "Ошибка: деление на ноль")
        else:
            entry.insert(0, first_number / second_number)

def button_decimal():
    current = entry.get()
    if '.' not in current:
        entry.insert(tk.END, '.')

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('/', 4, 3),
    ('=', 5, 0, 4)
]

for button in buttons:
    text, row, col = button[:3]
    colspan = button[3] if len(button) == 4 else 1

    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=button_equal).grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, command=button_clear).grid(row=row, column=col, sticky="nsew")
    elif text == '+':
        tk.Button(root, text=text, padx=20, pady=20, command=button_add).grid(row=row, column=col, sticky="nsew")
    elif text == '-':
        tk.Button(root, text=text, padx=20, pady=20, command=button_subtract).grid(row=row, column=col, sticky="nsew")
    elif text == '*':
        tk.Button(root, text=text, padx=20, pady=20, command=button_multiply).grid(row=row, column=col, sticky="nsew")
    elif text == '/':
        tk.Button(root, text=text, padx=20, pady=20, command=button_divide).grid(row=row, column=col, sticky="nsew")
    elif text == '.':
        tk.Button(root, text=text, padx=20, pady=20, command=button_decimal).grid(row=row, column=col, sticky="nsew")
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda num=text: button_click(num)).grid(row=row, column=col, sticky="nsew")

root.mainloop()