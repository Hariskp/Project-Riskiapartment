from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def get_date():
    date = cal.get_date()
    date_label.config(text=date.strftime("%d/%m/%Y"))

root = Tk()
root.title("Calendar Demo")

cal = Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy")
cal.pack(pady=20)

date_label = Label(root, text="")
date_label.pack(pady=10)

btn = ttk.Button(root, text="Select", command=get_date)
btn.pack(pady=10)

root.mainloop()
