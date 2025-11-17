#TO DO: 
#Hacer que se pueda toca los numeros y las operaciones con el teclado 
#Cambiar colores
# añadir posicion del numero en la pila 

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Python_PolishKCalc')
root.geometry('400x700')
root.resizable(0, 0)

color_text = '#000000'
color_button = '#e0e0e0'
color_button_equal = '#4caf50'
color_button_clear = '#072323'

screen_text = tk.StringVar()
screen_label = tk.Label(root, textvariable=screen_text, font=('Arial', 20), bg='#ffffff', fg=color_text, anchor='e', padx=10)
screen_label.grid(row=1, column=0, columnspan=4, sticky='we', pady=5)

#Historial
history_text = tk.StringVar()
history_label = tk.Label(root, textvariable=history_text, font=('Arial', 18),
                         bg='#f5f5f5', fg=color_text, anchor='w', justify='left')
history_label.grid(row=0, column=0, columnspan=4, sticky='we', pady=(0,10), padx=5)

expression = ''

#Historial
history = [] 

def update_history():
    history_text.set("\n".join(history[-5:]))

def press(number):
    global expression
    expression += str(number)
    screen_text.set(expression)

def lenCheck():
    if len(history) >= 2:
        return 1
    else:
        return 0

def backCheck():
    if len(history) >= 1:
        return 1
    else:
        return 0


def clear():
    global expression
    global history
    screen_text.set('')
    expression = ''
    history = []
    update_history()

def back():
    global expression
    global history
    if backCheck() == 0:
        messagebox.showerror(title="ERROR 10", detail="No suficiente stack")
        clear()
    screen_text.set('')
    expression = ''
    history.reverse()
    history.pop(0)
    history.reverse()
    update_history()

def backsp():
    global expression
    expression = expression[:-1]
    screen_text.set(expression)

def equalpress():
    try:
        global expression
        result = str(expression)

        #historial
        history.append(f"{expression}")
        update_history()

        screen_text.set(0)
        expression = ''
    except Exception as e:
        messagebox.showerror(title="ERROR 1", detail="Tus muertos, pon un numero valido")
        #clear()
        screen_text.set('')
        expression = ''

def remops():
    history.reverse()
    history.pop(0)
    history.pop(0)
    history.reverse()

def lastnum():
    pos=len(history) -1
    numA = history[pos]
    return str(numA)

def plastnum():
    pos=len(history) -2
    numB = history[pos]
    return str(numB)

def slashpress():
    global expression
    if lenCheck() == 1:
        expression = plastnum() + '/' + lastnum()
        result = str(eval(expression))
        remops()
        #historial
        history.append(f"{result}")
        update_history()

        screen_text.set(result)
        expression = ''
    else:
        messagebox.showerror(title="ERROR 10", detail="No suficiente stack")
        clear()

def multpress():
    global expression
    if lenCheck() == 1:
        expression = plastnum() + '*' + lastnum()
        result = str(eval(expression))
        remops()
        #historial
        history.append(f"{result}")
        update_history()

        screen_text.set(result)
        expression = ''
    else:
        messagebox.showerror(title="ERROR 10", detail="No suficiente stack")
        clear()

def pluspress():
    global expression
    if lenCheck() == 1:
        expression = plastnum() + '+' + lastnum()
        result = str(eval(expression))
        remops()
        #historial
        history.append(f"{result}")
        update_history()

        screen_text.set(result)
        expression = ''
    else:
        messagebox.showerror(title="ERROR 10", detail="No suficiente stack")
        clear()

def minuspress():
    global expression
    if lenCheck() == 1:
        expression = plastnum() + '-' + lastnum()
        result = str(eval(expression))
        remops()
        #historial
        history.append(f"{result}")
        update_history()

        screen_text.set(result)
        expression = ''
    else:
        messagebox.showerror(title="ERROR 10", detail="No suficiente stack")
        clear()

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ('0', 5, 0), ('.', 5, 1),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16), bg=color_button, fg=color_text,
                         command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

slash_button = tk.Button(root, text='/', width=5, height=2, font=('Arial', 16), bg=color_button, fg='#000000', command=slashpress)
slash_button.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')

mult_button = tk.Button(root, text='*', width=5, height=2, font=('Arial', 16), bg=color_button, fg='#000000', command=multpress)
mult_button.grid(row=3, column=3, padx=5, pady=5, sticky='nsew')

plus_button = tk.Button(root, text='+', width=5, height=2, font=('Arial', 16), bg=color_button, fg='#000000', command=pluspress)
plus_button.grid(row=4, column=3, padx=5, pady=5, sticky='nsew')

minus_button = tk.Button(root, text='-', width=5, height=2, font=('Arial', 16), bg=color_button, fg='#000000', command=minuspress)
minus_button.grid(row=5, column=2, padx=5, pady=5, sticky='nsew')

equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 16), bg=color_button_equal, fg='#000000', command=equalpress)
equal_button.grid(row=5, column=3, padx=5, pady=5, sticky='nsew')

clear_button = tk.Button(root, text='AC', width=5, height=2, font=('Arial', 16), bg=color_button_clear, fg='#ffffff', command=clear)
clear_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

back_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 16), bg=color_button_clear, fg='#ffffff', command=back)
back_button.grid(row=6, column=2, columnspan=1, padx=5, pady=5, sticky='nsew')

backsp_button = tk.Button(root, text='<_', width=5, height=2, font=('Arial', 16), bg=color_button_clear, fg='#ffffff', command=backsp)
backsp_button.grid(row=6, column=3, columnspan=1, padx=5, pady=5, sticky='nsew')

for op in range(7):
    root.grid_rowconfigure(op, weight=1)
for op in range(4):
    root.grid_columnconfigure(op, weight=1)

root.mainloop()

# nums = []
# def lenCheck():
#     if len(nums) >= 2:
#         return 1
#     else:
#         return 0
# def lastnum():
#     pos=len(nums) -1
#     numA = nums[pos]
#     return float(numA)
# def plastnum():
#     pos=len(nums) -2
#     numB = nums[pos]
#     return float(numB)
# def remops():
#     nums.reverse()
#     nums.pop(1)
#     nums.pop(1)
#     nums.reverse()

# print("\n" * 1000)

# print("      ===================== ")
# print("     | ,-----------------. |")
# print("     | |    1.05459 e -34| |")
# print("     | `-----------------' |")
# print("     | [@ ] On/Off  ###### |")
# print("     |              ###### |")
# print("     | [7] [8] [9] [C] [AC]|")
# print("     |                     |")

# print("=====================================")
# print("         PYTHON POLISH KCALC         ")
# print("=====================================")

# print("Wellcome to the CLI python-based polish notation calculator\n\nMenu:\n\nEnter a number and add it to the stack\n\n+. Sum the 2 first numers of the stack\n\n-. Subtract the 2 first numers of the stack\n\n*. Multiply the 2 first numers of the stack\n\n/. Divide the 2 first numers of the stack\n\n^. Power the first number to the second number of the stack\n\ne. Delete a number of the stack\n\nr. Delete all the stack\n\nq. Quit\n\nStack: ")
# for op in nums:
#     print(op)
# definput = input("Choose an option:")
# try:
#     numtest = float(definput)
#     nums.append(definput)
# except:
#     if definput == "+":
#         if lenCheck() == 1:
#             nums.append(plastnum()+lastnum())
#             remops()
#     elif definput == "-":
#         if lenCheck() == 1:
#             nums.append(plastnum()-lastnum())
#             remops()
#     elif definput == "*":
#         if lenCheck() == 1:
#             nums.append(plastnum()*lastnum())
#             remops()
#     elif definput == "/":
#         if lenCheck() == 1:
#             nums.append(plastnum()/lastnum())
#             remops()
#     elif definput == "^":
#         if lenCheck() == 1:
#             nums.append(plastnum()**lastnum())
#             remops()
#     elif definput == "e" or definput == "E":
#         nums.reverse()
#         nums.pop(0)
#         nums.reverse()
#     elif definput == "r" or definput == "R":
#         nums = []
#     elif definput == "q" or definput == "Q":
#         print("Vuelve pronto!!")
#         break
#     else:
#         print("NULL VALUE")
#         break