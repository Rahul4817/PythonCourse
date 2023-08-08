from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#25a5be"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("promodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#label
title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tamato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tamato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="dark blue",font=(FONT_NAME,34,"italic"))
canvas.grid(column=1,row=2)


start_button=Button(text="Start",command=start_timer)
start_button.grid(column=0,row=3)

# rest_button=Button(text="Reset",command=reset_timer)
# rest_button.grid(column=3,row=3)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)






window.mainloop()