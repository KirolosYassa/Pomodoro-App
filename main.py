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
WORKING_TIMES = [1, 3, 5, 7]
BREAKING_TIMES = [2, 4, 6]
LONG_BREAK = [8]
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer", foreground=GREEN)
    checkMark.config(text="")
    canvas.itemconfig(timer_init, text=f"00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    print(f"Reps = {reps}")
    if reps <= 8:
        # Long Break
        if reps % 8 == 0:
            title_label.config(text="Take a long break", foreground=RED)
            count_down(long_break_sec)
        # Short Break
        elif reps % 2 == 0:
            title_label.config(text="Take a short break", foreground=PINK)
            count_down(break_sec)
        # Working time
        else:
            title_label.config(text="Leave me alone!", foreground=GREEN)
            count_down(work_sec)
    else:
        reset()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = math.floor(count/60)
    seconds = count%60

    if seconds < 10:
        seconds = f"0{str(seconds)}"

    canvas.itemconfig(timer_init, text=f"{minutes}:{seconds}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps in WORKING_TIMES:
            mark = "✔"
            totalMarks = checkMark["text"]
            checkMark.config(text=totalMarks+mark)
        start_timer()


def start():
    start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(width=300, height=200, padx=150, pady=50, bg=YELLOW)
# window.geometry("500x500")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_file = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_file)
timer_init = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=2)


# Timer
title_label = Label(text="Timer")
title_label.config(text="Timer", bg=YELLOW, font=(FONT_NAME, 28, "bold"), foreground=GREEN)
title_label.grid(row=0, column=2)

# Check Mark
checkMark = Label(text="", bg=YELLOW, font=(FONT_NAME, 18), foreground=GREEN)
checkMark.grid(row=4, column=2)


#calls action() when pressed
startBtn = Button(text="Start", command=start)
startBtn.grid(row=3, column=1)


#calls action() when pressed
resetBtn = Button(text="Reset", command=reset)
resetBtn.grid(row=3, column=4)

window.mainloop()