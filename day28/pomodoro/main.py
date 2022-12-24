import math
import tkinter

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 44, "bold"))
    count_pomodoro.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer = LONG_BREAK_MIN
        time_label.config(fg=RED, text="Long Break")
    elif reps % 2 != 0:
        timer = WORK_MIN
        time_label.config(fg=GREEN, text="Work Hard")
    else:
        timer = SHORT_BREAK_MIN
        time_label.config(fg=PINK, text="Short Break")
    count_down(timer * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = math.floor(count / 60)
    if count_minute < 10:
        count_minute = f"0{count_minute}"

    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "\N{check mark}"
        count_pomodoro.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=96, pady=50, bg=YELLOW)

time_label = tkinter.Label(
    bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 44, "bold")
)
time_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="day28/pomodoro/tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(
    102, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)

start_button = tkinter.Button(command=start_timer, text="Start")
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

count_pomodoro = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"))
count_pomodoro.grid(column=1, row=2)

window.mainloop()