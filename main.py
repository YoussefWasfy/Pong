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
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text='00:00')
    timer_label.config(text='Timer')
    checkmark_label.config(text='')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        timer_label.config(text='Short Break', fg=PINK)
        count_down(short_break_seconds)
    elif reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        count_down(long_break_seconds)
    else:
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    count_minutes = minutes
    count_seconds = seconds
    if minutes < 10:
        count_minutes = f'0{minutes}'

    if seconds < 10:
        count_seconds = f'0{seconds}'

    canvas.itemconfigure(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:

        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '✓'
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'normal'))
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text=f'00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkmark_label.grid(row=3, column=1)
window.mainloop()
