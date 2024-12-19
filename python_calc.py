from tkinter import *
from math import *
from time import sleep
def help_form(event=None):
    help_form = Toplevel(window)
    help_form.title('Справка')
    help_form.geometry("1000x300")
    label = Label(help_form, text="Текст").place(x = 20, y = 20)    
def on_key_press(event):
    return "break" if event.char not in '0123456789' else True
def input_into_entry(symbol, op = None):
    global op_count
    open_massiv = ['++', '--', 'xx', '//', '+-', '+x', '+/', '-+', '-x', '-/', 'x+', 'x-', 'x/', '/+', '/-', '/x', '..', '.+', '.-', '.x', './', '+.', '-.', 'x.', '/.', '+^', '-^', '/^', 'x^', '.^']
    for_empty_massiv = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '00', '+', 'x', '/', '^2', '^(1/2)', '^(-1)', '.', '+00', '-00', 'x00', '/00', '+01', '+02', '+03', '+04', '+05', '+06', '+07', '+08', '+09', '-01', '-02', '-03', '-04', '-05', '-06', '-07', '-08', '-09', 'x01', 'x02', 'x03', 'x04', 'x05', 'x06', 'x07', 'x08', 'x09', '/01', '/02', '/03', '/04', '/05', '/06', '/07', '/08', '/09']
    global operation
    for i in range(10, 17): #18 -> 17
        if ((for_empty_massiv[i] == (entry.get() + symbol))): return
    for i in range(17, 57):
        if (for_empty_massiv[i] in (entry.get() + symbol)):
            entry.delete(len(entry.get()) - 1)
            entry.insert(len(entry.get()), symbol)
            return
    for i in range(10):
        if (for_empty_massiv[i] == (entry.get() + symbol)): clear_all()
    for i in range(30):
        en = entry.get()
        if open_massiv[i] in (en+symbol):
            clear_all()
            entry.insert(0, en[:-1])
            op_count = 0
    if (op != None):
        if ((op=="sqr") or (op=='sqrt') or (op=='recip')):
            entry.insert(END, symbol)
            operation = op
            count_result()
        elif (entry.get()=='') and (op == '-'): entry.insert(END, symbol)
        else:
            op_count += 1
            if op_count == 2:
                count_result()
                entry.insert(END, symbol)
                op_count = 1
            else: entry.insert(END, symbol)
            operation = op
    else: entry.insert(END, symbol)
def clear_all():
    entry.delete(0, END)
    global op_count
    op_count = 0
def count_result():
    text = entry.get()
    if (operation is not None) and (operation in text):
        if not (text[0] == '-' and operation == '-'):
            splitted = text.split(operation)
            print(splitted[1])
            first = float(splitted[0])
            second = float(splitted[1])
        else:
            splitted = text[1:].split(operation)
            first = float('-' + splitted[0])
            second = float(splitted[1])
        clear_all()
        if operation == '+': entry.insert(0, int(float(first+second))) if float(first+second)==int(first+second) else entry.insert(0, round((first+second), 4))
        if operation == '-': entry.insert(0, int(float(first-second))) if float(first-second)==int(first-second) else entry.insert(0, round((first-second), 4))
        if operation == 'x': entry.insert(0, int(float(first*second))) if float(first*second)==int(first*second) else entry.insert(0, round(first*second, 4))
        if operation == '/':
            if second == 0:
                entry.insert(0, "дел. на ноль")
                window.after(1500, clear_all)
            else: entry.insert(0, int(float(first/second))) if float(first/second)==int(first/second) else entry.insert(0, round(first/second, 4))
    elif operation == 'sqr':
        clear_all()
        entry.insert(0, int(float(text[:-2])**2)) if float(text[:-2])**2==int(float(text[:-2])**2) else entry.insert(0, round((float(text[:-2]))**2, 4))
    elif operation == 'sqrt':
        clear_all()
        entry.insert(0, int(sqrt(float(text[:-6])))) if sqrt(float(text[:-6]))==int(sqrt(float(text[:-6]))) else entry.insert(0, round(sqrt(float(text[:-6])), 4))
    elif operation == 'recip':
        clear_all()
        if float(text[:-5]) == 0:
            entry.insert(0, "дел. на ноль")
            window.after(1500, clear_all)
        else: entry.insert(0, int((1 / float(text[:-5])))) if (1 / float(text[:-5]))==int((1 / float(text[:-5]))) else entry.insert(0, round(1 / float(text[:-5]), 4))
button_values_massiv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', 'x', '/', '^(1/2)', '^(-1)', '^2']
global op_count
op_count = 0
window = Tk()
window.title('Калькулятор')
window.geometry('220x350+700+100')
window.bind('<Shift-F11>', help_form)
entry = Entry(window, width = 13, font = ('', 20))
entry.place(x = 10, y = 10)
entry.bind("<KeyPress>", on_key_press)
def create_uni_buttons():
    for i in range(18): button = Button(window, bg = 'black', fg = 'white', text = button_values_massiv[i], command = lambda i=i: input_into_entry(button_values_massiv[i], button_oper_massiv[i])).place(x = button_x_massiv[i], y = button_y_massiv[i], width = 50, height = 50)
button_values_massiv = ['0', '7', '8', '9', '4', '5', '6', '1', '2', '3', '.', '+', '-', 'x', '/', '^(1/2)', '^(-1)', '^2']
button_x_massiv = [60, 10, 60, 110, 10, 60, 110, 10, 60, 110, 110, 160, 160, 160, 160, 60, 10, 110]
button_y_massiv = [250, 100, 100, 100, 150, 150, 150, 200, 200, 200, 250, 200, 150, 100, 50, 50, 50, 50]
button_oper_massiv = [None, None, None, None, None, None, None, None, None, None, None, '+', '-', 'x', '/', 'sqrt', 'recip', 'sqr']
create_uni_buttons()
button_help = Button(window, text="Справка     Shift-F11", command = help_form).place(x = 10, y = 310, width = 200, height = 30)
button_clear_all = Button(window, bg = 'black', fg = 'white', text = 'C', command = clear_all).place(x = 10, y = 250, width = 50, height = 50)
button_equal = Button(window, bg = 'black', fg = 'white', text = '=', command = count_result).place(x = 160, y = 250, width = 50, height = 50)
window.mainloop()
