from tkinter import *
from math import *

def input_into_entry(symbol, op = None):
    entry.insert(END, symbol)
    if (op != None):
        global operation
        operation = op
def clear_all():
    entry.delete(0, END)
def count_result():
    text = entry.get()
    if operation in text:
        splitted = text.split(operation)
        first = float(splitted[0])
        second = float(splitted[1])
        if operation == '+':
            clear_all()
            entry.insert(0, first+second)
        if operation == '-':
            clear_all()
            entry.insert(0, first-second)
        if operation == 'x':
            clear_all()
            entry.insert(0, first*second)
        if operation == '/':
            clear_all()
            entry.insert(0, first/second)
    elif operation == 'sqr':
        clear_all()
        entry.insert(0, float(text[:-2])**2)
    elif operation == 'sqrt':
        clear_all()
        entry.insert(0, sqrt(float(text[:-8])))
    elif operation == 'recip':
        clear_all()
        entry.insert(0, 1 / float(text[:-5]))
window = Tk()
window.title('Калькулятор')
window.geometry('600x600+700+100')

entry = Entry(window, width = 13, font = ('', 20))
entry.place(x = 100, y = 10)

button1 = Button(window, bg = 'black', fg = 'white', text = '7', command = lambda: input_into_entry('7'))
button1.place(x = 100, y = 100, width = 50, height = 50)

button2 = Button(window, bg = 'black', fg = 'white', text = '8', command = lambda: input_into_entry('8'))
button2.place(x = 150, y = 100, width = 50, height = 50)

button3 = Button(window, bg = 'black', fg = 'white', text = '9', command = lambda: input_into_entry('9'))
button3.place(x = 200, y = 100, width = 50, height = 50)

button4 = Button(window, bg = 'black', fg = 'white', text = '4', command = lambda: input_into_entry('4'))
button4.place(x = 100, y = 150, width = 50, height = 50)

button5 = Button(window, bg = 'black', fg = 'white', text = '5', command = lambda: input_into_entry('5'))
button5.place(x = 150, y = 150, width = 50, height = 50)

button6 = Button(window, bg = 'black', fg = 'white', text = '6', command = lambda: input_into_entry('6'))
button6.place(x = 200, y = 150, width = 50, height = 50)

button7 = Button(window, bg = 'black', fg = 'white', text = '1', command = lambda: input_into_entry('1'))
button7.place(x = 100, y = 200, width = 50, height = 50)

button8 = Button(window, bg = 'black', fg = 'white', text = '2', command = lambda: input_into_entry('2'))
button8.place(x = 150, y = 200, width = 50, height = 50)

button9 = Button(window, bg = 'black', fg = 'white', text = '3', command = lambda: input_into_entry('3'))
button9.place(x = 200, y = 200, width = 50, height = 50)

button0 = Button(window, bg = 'black', fg = 'white', text = '0', command = lambda: input_into_entry('0'))
button0.place(x = 150, y = 250, width = 50, height = 50)

button_clear_all = Button(window, bg = 'black', fg = 'white', text = 'C', command = clear_all)
button_clear_all.place(x = 100, y = 250, width = 50, height = 50)

button_dot = Button(window, bg = 'black', fg = 'white', text = '.', command = lambda: input_into_entry('.'))
button_dot.place(x = 200, y = 250, width = 50, height = 50)

button_plus = Button(window, bg = 'black', fg = 'white', text = '+', command = lambda: input_into_entry('+', '+'))
button_plus.place(x = 250, y = 200, width = 50, height = 50)

button_equal = Button(window, bg = 'black', fg = 'white', text = '=', command = count_result)
button_equal.place(x = 250, y = 250, width = 50, height = 50)

button_minus = Button(window, bg = 'black', fg = 'white', text = '-', command = lambda: input_into_entry('-', '-'))
button_minus.place(x = 250, y = 150, width = 50, height = 50)

button_times = Button(window, bg = 'black', fg = 'white', text = 'x', command = lambda: input_into_entry('x', 'x'))
button_times.place(x = 250, y = 100, width = 50, height = 50)

button_div = Button(window, bg = 'black', fg = 'white', text = '/', command = lambda: input_into_entry('/', '/'))
button_div.place(x = 250, y = 50, width = 50, height = 50)

button_square = Button(window, bg = 'black', fg = 'white', text = 'x^2', command = lambda: input_into_entry('^2', 'sqr'))
button_square.place(x = 200, y = 50, width = 50, height = 50)

button_squareroot = Button(window, bg = 'black', fg = 'white', text = 'x^(1/2)', command = lambda: input_into_entry('^(1/2)', 'sqrt'))
button_squareroot.place(x = 150, y = 50, width = 50, height = 50)

button_recip = Button(window, bg = 'black', fg = 'white', text = '1/x', command = lambda: input_into_entry('^(-1)', 'recip'))
button_recip.place(x = 100, y = 50, width = 50, height = 50)

window.mainloop()
