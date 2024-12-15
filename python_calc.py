from tkinter import *
from math import *
from time import sleep

def help_form(event=None):
    help_form = Toplevel(window)
    help_form.title('Справка')
    help_form.geometry("1000x300")
    label = Label(help_form, text="Текст")
    label.place(x = 20, y = 20)
    
def on_key_press(event):
    if event.char not in '0123456789':
        return "break"
    return True

def input_into_entry(symbol, op = None, tag = 'notnull'):
    global tag_last
    global op_count
    global for_empty_massiv

    for i in range(10, 17): #18 -> 17
        if (for_empty_massiv[i] == (entry.get() + symbol)):
            return
    for i in range(10):
        if (for_empty_massiv[i] == (entry.get() + symbol)):
                clear_all()

    for i in range(30):
        en = entry.get()
        if open_massiv[i] in (en+symbol):
            clear_all()
            entry.insert(0, en[:-1])
            op_count = 0
    if (op != None):
        global operation
        if ((op=="sqr") or (op=='sqrt') or (op=='recip')):
            entry.insert(END, symbol)
            operation = op
            count_result()
            print('!')
        
        elif (entry.get()=='') and(op == '-'):
            entry.insert(END, symbol)
        else:
            op_count += 1
            if op_count == 2:
                count_result()
                entry.insert(END, symbol)
                op_count = 1
            else: entry.insert(END, symbol)
            operation = op
    else: entry.insert(END, symbol)
    tag_last = tag
def clear_all():
    entry.delete(0, END)
    global op_count
    op_count = 0
    global tag_last
    #tag_last = 'empty'
def count_result():
    #global operation
    text = entry.get()
    if (operation is not None) and (operation in text):
        if not (text[0] == '-' and operation == '-'):
            splitted = text.split(operation)
            first = float(splitted[0])
            second = float(splitted[1])
        else:
            splitted = text[1:].split(operation)
            first = float('-' + splitted[0])
            second = float(splitted[1])
        clear_all()
        if operation == '+':
            if float(first+second)==int(first+second):
                entry.insert(0, int(float(first+second)))
            else:
                entry.insert(0, round((first+second), 4))
        if operation == '-':
            if float(first-second)==int(first-second):
                entry.insert(0, int(float(first-second)))
            else:
                entry.insert(0, round((first-second), 4))
        if operation == 'x':
            if float(first*second)==int(first*second):
                entry.insert(0, int(float(first*second)))
            else:
                entry.insert(0, round(first*second, 4))
        if operation == '/':
            if second == 0:
                entry.insert(0, "дел. на ноль")
                window.after(1500, clear_all)
            else:
                if float(first/second)==int(first/second):
                    entry.insert(0, int(float(first/second)))
                else:
                    entry.insert(0, round(first/second, 4))
    elif operation == 'sqr':
        clear_all()
        if float(text[:-2])**2==int(float(text[:-2])**2):
            entry.insert(0, int(float(text[:-2])**2))
        else:
            entry.insert(0, round((float(text[:-2]))**2, 4))
    elif operation == 'sqrt':
        clear_all()
        if sqrt(float(text[:-6]))==int(sqrt(float(text[:-6]))):
            entry.insert(0, int(sqrt(float(text[:-6]))))
        else:
            entry.insert(0, round(sqrt(float(text[:-6])), 4))
    elif operation == 'recip':
        clear_all()
        if float(text[:-5]) == 0:
            entry.insert(0, "дел. на ноль")
            window.after(1500, clear_all)
        else:
            if (1 / float(text[:-5]))==int((1 / float(text[:-5]))):
                entry.insert(0, int((1 / float(text[:-5]))))
            else:
                entry.insert(0, round(1 / float(text[:-5]), 4))
    global tag_last
    tag_last = 'notnull'

button_values_massiv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '+', '-', 'x', '/', '^(1/2)', '^(-1)', '^2']
global tag_last
global op_count
op_count = 0
global for_empty_massiv
for_empty_massiv = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '00', '+', 'x', '/', '^2', '^(1/2)', '^(-1)', '.'] #no '-'
global open_massiv
open_massiv = ['++', '--', 'xx', '//', '+-', '+x', '+/', '-+', '-x', '-/', 'x+', 'x-', 'x/', '/+', '/-', '/x', '..', '.+', '.-', '.x', './', '+.', '-.', 'x.', '/.', '+^', '-^', '/^', 'x^', '.^']

window = Tk()
window.title('Калькулятор')
window.geometry('220x350+700+100')
window.bind('<Shift-F11>', help_form)

entry = Entry(window, width = 13, font = ('', 20))
entry.place(x = 10, y = 10)
entry.bind("<KeyPress>", on_key_press)

button_help = Button(window, text="Справка     Shift-F11", command = help_form)
button_help.place(x = 10, y = 310, width = 200, height = 30)

button1 = Button(window, bg = 'black', fg = 'white', text = '7', command = lambda: input_into_entry('7'))
button1.place(x = 10, y = 100, width = 50, height = 50)

button2 = Button(window, bg = 'black', fg = 'white', text = '8', command = lambda: input_into_entry('8'))
button2.place(x = 60, y = 100, width = 50, height = 50)

button3 = Button(window, bg = 'black', fg = 'white', text = '9', command = lambda: input_into_entry('9'))
button3.place(x = 110, y = 100, width = 50, height = 50)

button4 = Button(window, bg = 'black', fg = 'white', text = '4', command = lambda: input_into_entry('4'))
button4.place(x = 10, y = 150, width = 50, height = 50)

button5 = Button(window, bg = 'black', fg = 'white', text = '5', command = lambda: input_into_entry('5'))
button5.place(x = 60, y = 150, width = 50, height = 50)

button6 = Button(window, bg = 'black', fg = 'white', text = '6', command = lambda: input_into_entry('6'))
button6.place(x = 110, y = 150, width = 50, height = 50)

button7 = Button(window, bg = 'black', fg = 'white', text = '1', command = lambda: input_into_entry('1'))
button7.place(x = 10, y = 200, width = 50, height = 50)

button8 = Button(window, bg = 'black', fg = 'white', text = '2', command = lambda: input_into_entry('2'))
button8.place(x = 60, y = 200, width = 50, height = 50)

button9 = Button(window, bg = 'black', fg = 'white', text = '3', command = lambda: input_into_entry('3'))
button9.place(x = 110, y = 200, width = 50, height = 50)

button0 = Button(window, bg = 'black', fg = 'white', text = '0', command = lambda: input_into_entry('0', None)) #no 'empty'
button0.place(x = 60, y = 250, width = 50, height = 50)

button_clear_all = Button(window, bg = 'black', fg = 'white', text = 'C', command = clear_all)
button_clear_all.place(x = 10, y = 250, width = 50, height = 50)

button_dot = Button(window, bg = 'black', fg = 'white', text = '.', command = lambda: input_into_entry('.'))
button_dot.place(x = 110, y = 250, width = 50, height = 50)

button_plus = Button(window, bg = 'black', fg = 'white', text = '+', command = lambda: input_into_entry('+', '+'))
button_plus.place(x = 160, y = 200, width = 50, height = 50)

button_equal = Button(window, bg = 'black', fg = 'white', text = '=', command = count_result)
button_equal.place(x = 160, y = 250, width = 50, height = 50)

button_minus = Button(window, bg = 'black', fg = 'white', text = '-', command = lambda: input_into_entry('-', '-'))
button_minus.place(x = 160, y = 150, width = 50, height = 50)

button_times = Button(window, bg = 'black', fg = 'white', text = 'x', command = lambda: input_into_entry('x', 'x'))
button_times.place(x = 160, y = 100, width = 50, height = 50)

button_div = Button(window, bg = 'black', fg = 'white', text = '/', command = lambda: input_into_entry('/', '/'))
button_div.place(x = 160, y = 50, width = 50, height = 50)

button_square = Button(window, bg = 'black', fg = 'white', text = 'x^2', command = lambda: input_into_entry('^2', 'sqr'))
button_square.place(x = 110, y = 50, width = 50, height = 50)

button_squareroot = Button(window, bg = 'black', fg = 'white', text = 'x^(1/2)', command = lambda: input_into_entry('^(1/2)', 'sqrt'))
button_squareroot.place(x = 60, y = 50, width = 50, height = 50)

button_recip = Button(window, bg = 'black', fg = 'white', text = '1/x', command = lambda: input_into_entry('^(-1)', 'recip'))
button_recip.place(x = 10, y = 50, width = 50, height = 50)

window.mainloop()
