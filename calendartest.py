from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

def get_date():
    date = cal.get_date()
    date_parts = date.split("/")
    formatted_date = date_parts[0] + "/" + date_parts[1] + "/" + date_parts[2]
    date_label.config(text=formatted_date)


root = Tk()
root.title("Calendar Demo")

cal = Calendar(root, selectmode="day", date_pattern="dd/mm/yyyy")
cal.pack(pady=20)

date_label = Label(root, text="")
date_label.pack(pady=10)

btn = ttk.Button(root, text="Select", command=get_date)
btn.pack(pady=10)

root.mainloop()