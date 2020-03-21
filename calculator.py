# importing module tkinter as an object "tk"

from tkinter import *

# creating root frame
root = Tk()
root.resizable(False, False)

button_1 = Button(root, text=("1"), height=4, width=8)
button_2 = Button(root, text=("2"), height=4, width=8)
button_3 = Button(root, text=("3"), height=4, width=8)
button_4 = Button(root, text=("4"), height=4, width=8)
button_5 = Button(root, text=("5"), height=4, width=8)
button_6 = Button(root, text=("6"), height=4, width=8)
button_7 = Button(root, text=("7"), height=4, width=8)
button_8 = Button(root, text=("8"), height=4, width=8)
button_9 = Button(root, text=("9"), height=4, width=8)
button_0 = Button(root, text=("0"), height=4, width=8)
button_add = Button(root, text=("+"), height=4, width=8)
button_subtract = Button(root, text=("-"), height=4, width=8)
button_equals = Button(root, text=("="))
button_clear = Button(root, text=("clear"), height=4, width=8)

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=3, column=0)
button_add.grid(row=3, column=1)
button_subtract.grid(row=3, column=2)
button_clear.grid(row=4, column=0)
button_equals.grid(row=4, column=1, columnspan=2, sticky=N+S+E+W)

# putting the frame into mainlooping
root.mainloop()
