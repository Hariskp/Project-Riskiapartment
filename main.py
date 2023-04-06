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
    #MAIN
    global frm_left_login_entry_user, frm_left_login_entry_pass
    frm_main_login = Frame(root, bg='green')
    frm_main_login.place(x=0, y=0, width = w, height = h)
    frm_main_login.rowconfigure((0), weight=0)
    frm_main_login.columnconfigure((0,1), weight=1)
    bg = Label(frm_main_login, image=bg_login)
    bg.place(x=0,y=0,width=w,height=h) 

    #FRAME LEFT
    frm_left_login = Frame(frm_main_login, bg='white', bd=10)
    frm_left_login.rowconfigure((0,1,2,3,4), weight=1)
    frm_left_login.columnconfigure((0,1,2,3,), weight=1)
    frm_left_login.option_add("*font", "Verdana 16")
    frm_left_login.grid(column=0, row=1, sticky='news', ipadx=20, ipady=500)

    #FRAME RIGHT
    frm_right_login = Frame(frm_main_login, bg='#084235', bd=10)
    frm_right_login.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=0)
    frm_right_login.columnconfigure((0,1,2,3), weight=1)
    frm_right_login.grid(column=1, row=1, sticky='news')

    #LEFT
    Label(frm_left_login, text='Sign in to Riski Apartment', bg='white', font = 'Calibri 55 bold', fg='#60AC7F').grid(row=0, column=0, sticky='news')
    Label(frm_left_login, text='Username', bg='white', fg='#60AC7F', font = 'Calibri 20 ').grid(row=1, column=0,sticky='w', padx=200)
    Label(frm_left_login, text='Password', bg='white', fg='#60AC7F', font = 'Calibri 20 ').grid(row=2, column=0,sticky='w', padx=200)
    frm_left_login_entry_user = Entry(frm_left_login, width=10, bg='#E6E6E6')
    frm_left_login_entry_user.grid(row=1, column=0,sticky='e', ipadx=100, ipady=5)
    frm_left_login_entry_pass = Entry(frm_left_login, width=10, bg='#E6E6E6')
    frm_left_login_entry_pass.grid(row=2, column=0,sticky='e', ipadx=100, ipady=5)
    Button(frm_left_login, image=btn_login, bd=0, bg='white',command=home_fn).grid(row=3, column=0)
    
    #RIGHT
    Label(frm_right_login, image=img_rikilogo, bg='#084235').grid(row=0,column=1, sticky='n')
    Label(frm_right_login, text='Welcome Back!', font = 'Calibri 40 bold', bg='#084235', fg='white').grid(row=1,column=1, sticky='n')
    Label(frm_right_login, text='to keep connected with us please\n login your personal info', font = 'Calibri 20 bold', bg='#084235', fg='white').grid(row=2,column=1, sticky='n')
    Label(frm_right_login, text='contact', font = 'Calibri 20 bold', bg='#084235', fg='white').grid(row=3,column=1, sticky='n')
    Label(frm_right_login, image=img_phonenumber).grid(row=4,column=1, sticky='n')
    Label(frm_right_login, text='sutee.prodpran@gmail.com', font = 'Calibri 16 bold', bg='#084235', fg='white').grid(row=5,column=1, sticky='n')
    
def home_fn() :
    #MAIN
    global entry_user, entry_pwd 
    frm_main_home = Frame(root, bg='#084235')
    frm_main_home.place(x=0, y=0, width = w, height = h)
    frm_main_home.rowconfigure((0), weight=0)
    frm_main_home.columnconfigure((0,1), weight=1)
    bg = Label(frm_main_home, image=bg_login)
    bg.place(x=0,y=0,width=w,height=h)     

#Program resolution
w = 1920
h = 1080
root = mainwindow()
#Image import
img_rikilogo = PhotoImage(file='img/img_riskilogo.png')
img_phonenumber = PhotoImage(file='img/img_phonenumber.png')

#Button import
btn_login = PhotoImage(file='button/btn_login.png')

#Background
bg_login = PhotoImage(file = 'img/img_bglogin.png')
login_fn()
root.mainloop()