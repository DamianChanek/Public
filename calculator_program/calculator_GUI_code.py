from tkinter import *
from tkinter import messagebox


# function to capture input from grid buttons
def enter_equation(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_screen.config(text=equation_text)


# function to reset input, bound to button 'C'
def delete_equation():
    global equation_text
    equation_text = ''
    equation_screen.config(text=equation_text)


# calculate input, except invalid inputs and zero division, bound to button '='
def calculate():
    global equation_text
    try:
        evaluated_text = eval(equation_text)
        equation_text = str(evaluated_text)
        equation_screen.config(text=equation_text)

    except SyntaxError:
        messagebox.showwarning(title='ERROR', message='Invalid input. Please try again.')
        delete_equation()

    except ZeroDivisionError:
        messagebox.showwarning(title='ERROR',
                               message='If I was your math teacher, I would be really disappointed right now... ('
                                       'divided by 0).')
        delete_equation()


# raise a window for the calculator, add icon
calc_window = Tk()
calc_window.title('Calculator')
calc_window.geometry('500x500')

calc_icon = PhotoImage(file='C:\\Users\\ChanekD\\PycharmProjects\\pythonProject\\practice\\'
                            'pictures\\calculator_png.png')
calc_window.iconphoto(True, calc_icon)

# string used to store equation inputted by the user
equation_text = ''
# label to present user input
equation_screen = Label(calc_window, textvariable=equation_text,
                        font=('consolas', 20), bg='white',
                        width=24, height=2)

equation_screen.pack()

# frame to hold the label and buttons
frame = Frame(calc_window)
frame.pack()

# row 1 buttons
button_1 = Button(frame, text='1', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(1))
button_1.grid(row=1, column=0)
button_2 = Button(frame, text='2', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(2))
button_2.grid(row=1, column=1)
button_3 = Button(frame, text='3', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(3))
button_3.grid(row=1, column=2)
button_subtract = Button(frame, text='-', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation('-'))
button_subtract.grid(row=1, column=3)

# row 2 buttons
button_4 = Button(frame, text='4', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(4))
button_4.grid(row=2, column=0)
button_5 = Button(frame, text='5', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(5))
button_5.grid(row=2, column=1)
button_6 = Button(frame, text='6', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(6))
button_6.grid(row=2, column=2)
button_add = Button(frame, text='+', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation('+'))
button_add.grid(row=2, column=3)

# row 3 buttons
button_7 = Button(frame, text='7', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(7))
button_7.grid(row=3, column=0)
button_8 = Button(frame, text='8', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(8))
button_8.grid(row=3, column=1)
button_9 = Button(frame, text='9', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(9))
button_9.grid(row=3, column=2)
button_multiply = Button(frame, text='x', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation('*'))
button_multiply.grid(row=3, column=3)

# row 4 buttons
button_0 = Button(frame, text='0', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation(0))
button_0.grid(row=4, column=0, columnspan=2, sticky='w')
button_dot = Button(frame, text='.', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation('.'))
button_dot.grid(row=4, column=1)
button_divide = Button(frame, text='/', bd=4, relief=RAISED, width=9, height=4, command=lambda: enter_equation('/'))
button_divide.grid(row=4, column=2)
button_equals = Button(frame, text='=', bd=4, relief=RAISED, width=9, height=4, command=calculate)
button_equals.grid(row=4, column=3)

# row 5 button
button_C = Button(frame, text='C', bd=4, relief=RAISED, width=20, height=4, command=delete_equation)
button_C.grid(row=5, column=1, columnspan=2, sticky='')

# call window to the screen
calc_window.mainloop()
