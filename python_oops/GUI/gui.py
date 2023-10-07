from tkinter import *


window=Tk()
window.title("Calculator")
window.minsize(600,500)
# window.maxsize(700,800)


#Button

def btn_click():
    print("7 number is clicked")



#Frame
def all_btn():

    frame=Frame(window)
    frame.pack()


    nine=Button(frame,text="7",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey",command=btn_click)
    nine.grid(row=1,column=0,padx=3,pady=2)

    nine=Button(frame,text="8",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    nine.grid(row=1,column=1,padx=3,pady=2)

    nine=Button(frame,text="9",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    nine.grid(row=1,column=2,padx=3,pady=2)

    nine=Button(frame,text=".",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    nine.grid(row=1,column=3,padx=3,pady=2)



    five=Button(frame,text="4",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    five.grid(row=2,column=0,padx=3,pady=2)

    six=Button(frame,text="5",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    six.grid(row=2,column=1,padx=3,pady=2)

    seven=Button(frame,text="6",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    seven.grid(row=2,column=2,padx=3,pady=2)

    eight=Button(frame,text="x",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    eight.grid(row=2,column=3,padx=3,pady=2)


    one=Button(frame,text="1",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    one.grid(row=3,column=0,padx=3,pady=2)

    two=Button(frame,text="2",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    two.grid(row=3,column=1,padx=3,pady=2)

    three=Button(frame,text="3",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    three.grid(row=3,column=2,padx=3,pady=2)

    four=Button(frame,text="/",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    four.grid(row=3,column=3,padx=3,pady=2)



    sub=Button(frame,text="-",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    sub.grid(row=4,column=0,padx=3,pady=2)

    zero=Button(frame,text="0",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    zero.grid(row=4,column=1,padx=3,pady=2)

    plus=Button(frame,text="+",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    plus.grid(row=4,column=2,padx=3,pady=2)

    equal=Button(frame,text="=",font=('Arial',10,'bold'),width=7,height=2,activebackground="lightgrey")
    equal.grid(row=4,column=3,padx=3,pady=2)

all_btn()
window.mainloop()