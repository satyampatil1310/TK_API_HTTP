from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
xdis = 50
ydis = 300
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00", font=(FONT_NAME, 30, "bold"), fill="white")
    title.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global xdis, ydis
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Break", font=(FONT_NAME, 30, "bold"), fg=PINK, bg=YELLOW)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Break", font=(FONT_NAME, 30, "bold"), fg=RED, bg=YELLOW)
    else:
        count_down(WORK_MIN * 60)
        title.config(text="Work", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
        if reps > 1:
            checkmark = Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
            xdis += 30
            checkmark.place(x=xdis, y=ydis)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_minute = math.floor(count / 60)
    count_seconds = math.floor(count % 60)
    if count_seconds < 10:
        canvas.itemconfig(timer_text, text=f"{count_minute}:0{count_seconds}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Technique")
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(152, 112, image=tomato_img)
timer_text = canvas.create_text(150, 130, text=f"00:00", font=(FONT_NAME, 30, "bold"), fill="white")


start = Button(text="Start", command=start_timer, font=(FONT_NAME, 10, "bold"), bg=GREEN)
reset = Button(text="Reset", command=resettimer, font=(FONT_NAME, 10, "bold"), bg=GREEN )
start.place(x=0, y=250)
reset.place(x=250, y=250)

title = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.pack()
checkmark = Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
canvas.pack()


window.mainloop()