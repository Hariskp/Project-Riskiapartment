from tkinter import *
from tkcalendar import DateEntry

root = Tk()

def on_date_change(event):
    print(date_var.get())

date_var = StringVar()
cal = DateEntry(root, selectmode="day", date_pattern="dd/mm/yyyy", datevar=date_var)
cal.pack(pady=20)
date_var.trace_add('write', on_date_change)

print(date_var)

root.mainloop()
