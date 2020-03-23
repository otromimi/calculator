# importing module tkinter FULL
from tkinter import *

# creating root frame
root = Tk()
root.resizable(False, False)  # Making it of a fixed size
root.geometry("+1200+150")  # Setting the position of the window on the screen

f_num = 87


def on_click(num):
    input_field.insert(END, num)


def erase():
    input_field.delete(0, END)


def plus_func():
    global f_num
    num = int(input_field.get())
    f_num = num
    erase()


def less_func():
    global f_num
    num = int(input_field.get())
    f_num = -1 * num
    erase()


def equals_func():
    global f_num
    old_f_num = int(input_field.get())
    if f_num < 0:
        f_num = f_num * -1 - int(input_field.get())
        old_f_num = old_f_num * -1
    else:
        f_num += int(input_field.get())
    erase()
    input_field.insert(0, str(f_num))
    f_num = old_f_num




# calculator number buttons
button_1 = Button(root, text="1", height=3, width=8, command=lambda: on_click(1))
button_2 = Button(root, text="2", height=3, width=8, command=lambda: on_click(2))
button_3 = Button(root, text="3", height=3, width=8, command=lambda: on_click(3))
button_4 = Button(root, text="4", height=3, width=8, command=lambda: on_click(4))
button_5 = Button(root, text="5", height=3, width=8, command=lambda: on_click(5))
button_6 = Button(root, text="6", height=3, width=8, command=lambda: on_click(6))
button_7 = Button(root, text="7", height=3, width=8, command=lambda: on_click(7))
button_8 = Button(root, text="8", height=3, width=8, command=lambda: on_click(8))
button_9 = Button(root, text="9", height=3, width=8, command=lambda: on_click(9))
button_0 = Button(root, text="0", height=3, width=8, command=lambda: on_click(0))
# function buttons of the calculator
button_add = Button(root, text="+", height=3, width=8, command=plus_func)
button_subtract = Button(root, text="-", height=3, width=8, command=less_func)
button_equals = Button(root, text="=", command=equals_func)
button_clear = Button(root, text="clear", height=3, width=8, command=erase)
# input field for numbers
input_field = Entry(root, width=8 * 3, borderwidth=5)

# Adding to the main frame
input_field.grid(row=0, columnspan=3, sticky='nsew')

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_clear.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2, sticky=N + S + E + W)

# putting the frame into mainloop
root.mainloop()
