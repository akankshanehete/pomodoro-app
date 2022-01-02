from tkinter import *
import time
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=str(count_min) + ":" + str(count_sec))
    if count > 0:
        window.after(1000, countdown, count - 1)
def start_timer():
    countdown(WORK_MIN*60)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)
window.config(padx=100, pady=50, bg=YELLOW)

header_lb = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'normal'))
header_lb.grid(row=1, column=2)

start_btn = Button(text='Start', width=7, highlightthickness=0, command=start_timer)
start_btn.grid(row=3, column=1)

reset_btn = Button(text='Reset', width=7, highlightthickness=0)
reset_btn.grid(row=3, column=3)

status_lb = Label(text='✅', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'normal'))
status_lb.grid(row=5, column=2)


window.mainloop()
