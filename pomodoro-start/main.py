from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None
min_type = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text='Timer')
    check_mark.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = int(WORK_MIN*60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    print(reps)
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
       # print('2nd ELIF')
        count_down(short_break_sec)
        title_label.config(text='Short Break', fg=PINK)
    else:
        #print('WORK SEC')
        count_down(work_sec)
        title_label.config(text='Work Now',fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    final_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=final_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        print(f'Number of work_sessions: {work_sessions}')
        for _ in range(work_sessions):
             marks += '✔'
        #marks = '✔'*work_sessions
        print(marks)
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=20, pady=20, bg=YELLOW)



title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=2, row=1)

canvas = Canvas(width=360, height=360, bg=YELLOW, highlightthickness=0) # 200, #224

#The PhotoImage class can get hold of and read an image at a particular path location
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 180, image=tomato_img) # 100, 112
canvas.grid(column=2, row=2)


timer_text = canvas.create_text(180, 180, text='00:00', fill='white', font=(FONT_NAME, 34, "bold")) #You need to specify x,y coordinates
#When you want edit Canvas properties, you must use itemconfig

start_button = Button(text='Start',command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=3, row=3) #3

check_mark = Label(fg=GREEN, bg=YELLOW, font=35)
check_mark.grid(column=2, row=4) #2



window.mainloop()