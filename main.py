from tkinter import*
import sqlite3
from tkinter import ttk 
from tkinter import messagebox

#Create Main Window
def mainwindow() : 
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#EBFCE0')
    root.title("Riski Apartment : Login")
    root.option_add("*font", "Verdana 16 bold")
    #root.resizable(False, False)
    root.rowconfigure((0,1,2,3), weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def createconnection() : #Create Connection to sqlite3 (สร้างรอไว้ก่อน)
    global conn, cursor
    conn = sqlite3.connect('input database right here')
    cursor = conn.cursor()

def login_fn() :
    frm_login = Frame(root, bg='red')
    frm_login.place(x=0, y=0, width = w, height = h)
    frm_login.rowconfigure((0,1,2,3), weight=1)
    frm_login.columnconfigure((0,1,2,3), weight=1)
    bg = Label(frm_login, image=bg_login)
    bg.place(x=0,y=0,width=w,height=h)


#Program resolution
w = 1920
h = 1080
root = mainwindow()
#Image import

#Background
bg_login = PhotoImage(file = 'img/img_login.png')
login_fn()
root.mainloop()