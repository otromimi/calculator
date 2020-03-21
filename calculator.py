# importing module tkinter as an object "tk"

from tkinter import *


class Button(Button):
    def __init__(self, place, text):
        super(place, text=(text))


# creating root frame
root = Tk()

button_1 = Button(root, text=("1"))
button_2 = Button(root, text=("2"))
button_3 = Button(root, text=("3"))
button_4 = Button(root, text=("4"))
button_5 = Button(root, text=("5"))
button_6 = Button(root, text=("6"))
button_7 = Button(root, text=("7"))
button_8 = Button(root, text=("8"))
button_9 = Button(root, text=("9"))
button_0 = Button(root, text=("0"))
button_add = Button(root, text=("+"))
button_subtract = Button(root, text=("-"))
button_equals = Button(root, text=("="))
button_clear = Button(root, text=("clear"))

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1 )
button_3.grid(row=0, column=2 )
button_4.grid(row=1, column=0 )
button_5.grid(row=1, column=1 )
button_6.grid(row=1, column=2 )
button_7.grid(row=2, column=0 )
button_8.grid(row=2, column=1 )
button_9.grid(row=2, column=2 )
button_0.grid(row=3, column=0 )
button_add.grid(row=3, column=1 )
button_subtract.grid(row=3, column=2 )
button_clear.grid(row=4, column=0 )
button_equals.grid(row=4, column=1, columnspan=2)

# putting the frame into mainlooping
root.mainloop()
