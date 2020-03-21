# importing module tkinter as an object "tk"

from tkinter import *


class MyButton(Button):
    pass

# creating root frame
root = Tk()

button_1 = MyButton(root, text=("1"), height=4, width=8)
button_2 = MyButton(root, text=("2"), height=4, width=8)
button_3 = MyButton(root, text=("3"), height=4, width=8)
button_4 = MyButton(root, text=("4"), height=4, width=8)
button_5 = MyButton(root, text=("5"), height=4, width=8)
button_6 = MyButton(root, text=("6"), height=4, width=8)
button_7 = MyButton(root, text=("7"), height=4, width=8)
button_8 = MyButton(root, text=("8"), height=4, width=8)
button_9 = MyButton(root, text=("9"), height=4, width=8)
button_0 = MyButton(root, text=("0"), height=4, width=8)
button_add = MyButton(root, text=("+"), height=4, width=8)
button_subtract = MyButton(root, text=("-"), height=4, width=8)
button_equals = MyButton(root, text=("="), height=4, width=8)
button_clear = MyButton(root, text=("clear"))

button_1.grid(row=0, column=0, sticky=N+S+E+W)
button_2.grid(row=0, column=1, sticky=N+S+E+W )
button_3.grid(row=0, column=2, sticky=N+S+E+W )
button_4.grid(row=1, column=0, sticky=N+S+E+W )
button_5.grid(row=1, column=1, sticky=N+S+E+W )
button_6.grid(row=1, column=2, sticky=N+S+E+W )
button_7.grid(row=2, column=0, sticky=N+S+E+W )
button_8.grid(row=2, column=1, sticky=N+S+E+W )
button_9.grid(row=2, column=2, sticky=N+S+E+W )
button_0.grid(row=3, column=0, sticky=N+S+E+W )
button_add.grid(row=3, column=1, sticky=N+S+E+W )
button_subtract.grid(row=3, column=2, sticky=N+S+E+W )
button_clear.grid(row=4, column=0, sticky=N+S+E+W )
button_equals.grid(row=4, column=1, columnspan=2, sticky=N+S+E+W)

# putting the frame into mainlooping
root.mainloop()
