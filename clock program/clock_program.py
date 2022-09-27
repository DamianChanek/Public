from time import strftime
from tkinter import Tk, Label, N, S, PhotoImage


def updateClock():
    time_string = strftime('%H:%M:%S')
    time_label.config(text=time_string)

    date_string = strftime('%d %b %Y')
    date_label.config(text=date_string)

    window.after(1000, updateClock)


window = Tk()
window.resizable(width=False, height=False)

icon = PhotoImage(file='C:\\Users\\ChanekD\\PycharmProjects\\pythonProject\\practice\\pictures\\clock.png')
window.iconphoto(True, icon)
window.title("   Clock Program")

time_label = Label(window, font=('Helvetica', 50), fg="#D8998C", bg='black', padx=55)
time_label.pack(anchor=N)

date_label = Label(window, font=('Helvetica', 50), fg="#D8998C", bg='black')
date_label.pack(anchor=S)

updateClock()

window.mainloop()
