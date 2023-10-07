from tkinter import *

window = Tk()
window.geometry("500x400")



frame = Frame(window)
frame.pack()

leftframe = Frame(window)
leftframe.pack(side=LEFT)

rightframe = Frame(window)
rightframe.pack(side=LEFT)

btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT,)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

window.mainloop()