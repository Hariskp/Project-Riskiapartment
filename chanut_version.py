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

def login_fn() : #โค้ดนี้กำลังแก้ไขโดย ริส 06/04/2023 เวลา 11:30
    #MAIN
    global entry_user, entry_pwd 
    frm_main_login = Frame(root, bg='green')
    frm_main_login.place(x=0, y=0, width = w, height = h)
    frm_main_login.rowconfigure((0), weight=0)
    frm_main_login.columnconfigure((0,1), weight=1)
    bg = Label(frm_main_login, image=bg_login)
    bg.place(x=0,y=0,width=w,height=h) 

    #FRAME LEFT
    frm_left_login = Frame(frm_main_login, bg='white', bd=10)
    frm_left_login.rowconfigure((0,1,2,3,4), weight=1)
    frm_left_login.columnconfigure((0,1,2,3), weight=1)
    frm_left_login.option_add("*font", "Verdana 16")
    frm_left_login.grid(column=0, row=1, sticky='news', ipadx=20, ipady=500)

    #FRAME RIGHT
    frm_right_login = Frame(frm_main_login, bg='#084235', bd=10)
    frm_right_login.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1) #1
    frm_right_login.columnconfigure((0,1,2,3), weight=1)
    frm_right_login.grid(column=1, row=1, sticky='news')

    #LEFT
    Label(frm_left_login, text='Sign in to Riski Apartment', bg='white', font = 'Calibri 55 bold', fg='#60AC7F').grid(row=0, column=0, sticky='news', padx=150)
    Label(frm_left_login, text='Username', bg='white', fg='#60AC7F', font = 'Calibri 20 ').grid(row=1, column=0,sticky='w', padx=150)
    Label(frm_left_login, text='Password', bg='white', fg='#60AC7F', font = 'Calibri 20 ').grid(row=2, column=0,sticky='w', padx=150)
    frm_left_login_entry_user = Entry(frm_left_login, width=10, bg='#E6E6E6')
    frm_left_login_entry_user.grid(row=1, column=0, ipadx=100, ipady=5)
    frm_left_login_entry_pass = Entry(frm_left_login, width=10, bg='#E6E6E6')
    frm_left_login_entry_pass.grid(row=2, column=0, ipadx=100, ipady=5)
    Button(frm_left_login, image=btn_login, bd=0, bg='white', command=home_fn).grid(row=3, column=0)
    
    #RIGHT
    Label(frm_right_login, image=img_riskilogo, bg='#084235').grid(row=0,column=1, sticky='n', pady=30)
    Label(frm_right_login, text='Welcome Back!', font = 'Calibri 50 bold', bg='#084235', fg='white').grid(row=1,column=1, sticky='n')
    Label(frm_right_login, text='to keep connected with us please\n login your personal info', font = 'Calibri 20 bold', bg='#084235', fg='white').grid(row=2,column=1, sticky='n')
    Label(frm_right_login, text='contact', font = 'Calibri 20 bold', bg='#084235', fg='white').grid(row=3,column=1, sticky='n')
    Label(frm_right_login, image=img_phonenumber).grid(row=4,column=1, sticky='n')
    Label(frm_right_login, text='sutee.prodpran@gmail.com', font = 'Calibri 16 bold', bg='#084235', fg='white').grid(row=5,column=1, sticky='n')
    Label(frm_right_login, text='THA IT PAK KRET NONTHABURI 11120', font = 'Calibri 14 bold', bg='#084235', fg='white').grid(row=9,column=1, sticky='n')

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
    root.title("Riski Apartment : Home")
    frm_main_inout = Frame(root, bg='black')
    frm_main_inout.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_inout = Frame(frm_main_inout, bg='#084235')
    frm_left_inout.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_inout = Frame(frm_main_inout, bg='white')
    frm_right_inout.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_inout, image=img_riskilogos, bd=0 , bg='#084235').place(x=30, y=30)

    #LEFT
    Button(frm_left_inout, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_inout, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_inout, image=btn_checkout, bd=0, bg='#084235').place(x=198, y=380)
    Button(frm_left_inout, image=btn_home, bd=0, bg='#084235').place(x=30, y=900)

def checkin_fn() :
    #MAIN
    root.title("Riski Apartment : Home")
    frm_main_checkin = Frame(root, bg='black')
    frm_main_checkin.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_checkin = Frame(frm_main_checkin, bg='#084235')
    frm_left_checkin.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkin = Frame(frm_main_checkin, bg='white')
    frm_right_checkin.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_checkin, image=img_riskilogos, bd=0 , bg='#084235').place(x=30, y=30)

    #LEFT
    Button(frm_left_checkin, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_checkin, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_checkin, image=btn_checkout, bd=0, bg='#084235').place(x=198, y=380)
    Button(frm_left_checkin, image=btn_home, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_checkin, text='CHECK IN', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_checkin_bg = Frame(frm_right_checkin, bg='#DDDDDD')
    frm_right_checkin_bg.place(x=276, y=258, width=750, height=600)
    Label(frm_right_checkin_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=180, y=60)
    entry_phonenum_checkin = Entry(frm_right_checkin_bg).place(x=350, y=60)
    Label(frm_right_checkin_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_checkin = Entry(frm_right_checkin_bg).place(x=350, y=120)
    Label(frm_right_checkin_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=194, y=180)
    roomtype = OptionMenu(frm_right_checkin_bg, text='wtf').place(x=350, y=180)
    





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
btn_checkin = PhotoImage(file='button/btn_checkin.png')
btn_checkout = PhotoImage(file='button/btn_checkout.png')
btn_home = PhotoImage(file='button/btn_home.png')


#Background
bg_login = PhotoImage(file = 'img/img_bglogin.png')
login_fn()
root.mainloop()