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
    frm_main_login = Frame(root, bg='black')
    frm_main_login.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_login = Frame(root, bg='white')
    frm_left_login.place(x=0, y=0, width=1250, height=1080)

    #FRAME RIGHT
    frm_right_login = Frame(root, bg='#084235')
    frm_right_login.place(x=1251, y=0, width=669, height=1080)

    #LEFT
    Label(frm_left_login, text='Sign in to Riski Apartment', bg='white', font = 'Calibri 55 bold', fg='#60AC7F').place(x=180, y=60)
    Label(frm_left_login, text='Username', bg='white', fg='#60AC7F', font = 'Calibri 40').place(x=360, y=300)
    frm_left_login_entry_username = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0)
    frm_left_login_entry_username.place(x=380, y=400, height=50)
    Label(frm_left_login, text='Password', bg='white', fg='#60AC7F', font = 'Calibri 40').place(x=360, y=480)
    frm_left_login_entry_password = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0)
    frm_left_login_entry_password.place(x=380, y=580, height=50)
    Button(frm_left_login, image=btn_login, bd=0, bg='white', command=home_fn).place(x=480, y=680)

    #RIGHT
    Label(frm_right_login, image=img_riskilogo, bg='#084235').place(x=93, y=30)
    Label(frm_right_login, text='Welcome Back!', bg='#084235', fg='white', font = 'Calibri 50 bold').place(x=120, y=300)
    Label(frm_right_login, text='to keep connected with us please\n login your personal info', font = 'Calibri 20 bold', bg='#084235', fg='white').place(x=150, y=380)
    Label(frm_right_login, text='contact', font = 'Calibri 20 bold', bg='#084235', fg='white').place(x=300, y=700)
    Label(frm_right_login, image=img_phonenumber).place(x=240, y=750)
    Label(frm_right_login, text='sutee.prodpran@gmail.com', font = 'Calibri 16 bold', bg='#084235', fg='white').place(x=230, y=840)
    Label(frm_right_login, text='THA IT PAK KRET NONTHABURI 11120', font = 'Calibri 14 bold', bg='#084235', fg='white').place(x=200, y=900)

def home_fn() :
    #MAIN
    root.title("Riski Apartment : Home")
    frm_main_home = Frame(root, bg='black')
    frm_main_home.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_home = Frame(frm_main_home, bg='#084235')
    frm_left_home.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_home = Frame(frm_main_home, bg='white')
    frm_right_home.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_home, image=img_riskilogos, bg='#084235', command=home_fn, bd=0).place(x=30, y=30)
    Button(frm_left_home, image=btn_checkinout, bd=0, bg='#084235', command=checkinout_fn).place(x=180, y=180)
    Button(frm_left_home, image=btn_inforeport, bd=0, bg='#084235').place(x=180, y=280)
    Button(frm_left_home, image=btn_accmanage, bd=0, bg='#084235').place(x=180, y=380)
    Button(frm_left_home, image=btn_roommanage, bd=0, bg='#084235').place(x=180, y=480)
    Button(frm_left_home, image=btn_service, bd=0, bg='#084235').place(x=180, y=580)
    Button(frm_left_home, image=btn_signout, bd=0, bg='#084235', command=login_fn).place(x=30, y=900)

def checkinout_fn() : #โค้ดนี้กำลังแก้ไขโดย นัท 06/04/2023 เวลา 17:30
    #MAIN
    root.title("Riski Apartment : Check In/Out")
    frm_main_inout = Frame(root, bg='#084235')
    frm_main_inout.place(x=0, y=0, width = w, height = h)
    frm_main_inout.rowconfigure((0,1), weight=1)
    frm_main_inout.columnconfigure((0,1,2), weight=1)

    #FRAME LEFT
    frm_left_inout = Frame(frm_main_inout,bg='#084235',bd=10)
    frm_left_inout.rowconfigure((0,1,2,3,4,5,6), weight=0)
    frm_left_inout.columnconfigure((0,1), weight=1)
    frm_left_inout.grid(row=0, column=0,sticky='news', rowspan=2)

    #FRAME RIGHT
    frm_right_inout = Frame(frm_main_inout,bg='white',bd=10)
    frm_right_inout.rowconfigure((0,1,2,3,4,5,6), weight=1)
    frm_right_inout.columnconfigure((0,1), weight=1)
    frm_right_inout.grid(row=0, column=1,sticky='news', rowspan=3,columnspan=2)



#Program resolution
w = 1920
h = 1080
root = mainwindow()
#Image import
img_riskilogo = PhotoImage(file='img/img_riskilogo.png')
img_phonenumber = PhotoImage(file='img/img_phonenumber.png')
img_riskilogos = PhotoImage(file='img/img_riskilogo.png').subsample(2,2)



#Button import
btn_login = PhotoImage(file='button/btn_login.png')
btn_checkinout = PhotoImage(file='button/btn_check-in-out.png')
btn_inforeport = PhotoImage(file='button/btn_info-report.png')
btn_accmanage = PhotoImage(file='button/btn_accountmanage.png')
btn_roommanage = PhotoImage(file='button/btn_roommanage.png')
btn_service = PhotoImage(file='button/btn_service.png')
btn_signout = PhotoImage(file='button/btn_signout.png')


#Background
bg_login = PhotoImage(file = 'img/img_bglogin.png')
login_fn()
root.mainloop()