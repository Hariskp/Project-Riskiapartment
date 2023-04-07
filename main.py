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

def login_fn() : #หน้า Login #By Haris
    #MAIN
    root.title("Riski Apartment : Login")
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
    frm_left_login_entry_password = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0,show="*")
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

def home_fn() : #หน้า Home #By Haris
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
    Button(frm_left_home, image=btn_accmanage, bd=0, bg='#084235', command=accountmanage_fn).place(x=180, y=380)
    Button(frm_left_home, image=btn_roommanage, bd=0, bg='#084235', command=roommanage_fn).place(x=180, y=480)
    Button(frm_left_home, image=btn_service, bd=0, bg='#084235', command=service_fn).place(x=180, y=580)
    Button(frm_left_home, image=btn_signout, bd=0, bg='#084235', command=login_fn).place(x=30, y=900)

def checkinout_fn() : #หน้า Main Check In/Out#โค้ดนี้กำลังแก้ไขโดย นัท 06/04/2023 เวลา 17:30
    #MAIN
    root.title("Riski Apartment : Check In/Out")
    frm_main_inout = Frame(root, bg='black')
    frm_main_inout.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_inout = Frame(frm_main_inout, bg='#084235')
    frm_left_inout.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_inout = Frame(frm_main_inout, bg='white')
    frm_right_inout.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_inout, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_inout, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_inout, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_inout, image=btn_checkout, bd=0, bg='#084235', command=checkout_fn).place(x=198, y=380)
    Button(frm_left_inout, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

def checkin_fn() : #หน้า Check In #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Check In")
    frm_main_checkin = Frame(root, bg='black')
    frm_main_checkin.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_checkin = Frame(frm_main_checkin, bg='#084235')
    frm_left_checkin.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkin = Frame(frm_main_checkin, bg='white')
    frm_right_checkin.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_checkin, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_checkin, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_checkin, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_checkin, image=btn_checkout, bd=0, bg='#084235', command=checkout_fn).place(x=198, y=380)
    Button(frm_left_checkin, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_checkin, text='CHECK IN', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_checkin_bg = Frame(frm_right_checkin, bg='#DDDDDD')
    frm_right_checkin_bg.place(x=276, y=258, width=750, height=600)
    Label(frm_right_checkin_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=180, y=60)     # ต้องใส่ปุ่มค้นหา
    entry_phonenum_checkin = Entry(frm_right_checkin_bg).place(x=350, y=60)
    Button(frm_right_checkin_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=670, y=58)
    Label(frm_right_checkin_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_checkin = Entry(frm_right_checkin_bg).place(x=350, y=120)
    Label(frm_right_checkin_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=198, y=180)
    #room type
    room_type = ["รายเดือนแอร์", "รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_checkin_bg, *room_type).place(x=350, y=180, width=310)
    Label(frm_right_checkin_bg, text='ชั้น : ', bg='#DDDDDD').place(x=271, y= 240)
    entry_floor_checkin = Entry(frm_right_checkin_bg).place(x=350, y=240)
    Label(frm_right_checkin_bg, text='ราคา : ', bg='#DDDDDD').place(x=259, y= 300)
    entry_price_checkin = Entry(frm_right_checkin_bg).place(x=350, y=300)
    Button(frm_right_checkin_bg, image=btn_next,bd=0, bg='#DDDDDD', command=checkin_date).place(x=480, y=450)

def checkin_date() : #หน้า Check In ที่ 2 #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Check In")
    frm_main_checkindate = Frame(root, bg='black')
    frm_main_checkindate.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_checkindate = Frame(frm_main_checkindate, bg='#084235')
    frm_left_checkindate.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkindate = Frame(frm_main_checkindate, bg='white')
    frm_right_checkindate.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_checkindate, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_checkindate, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_checkindate, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_checkindate, image=btn_checkout, bd=0, bg='#084235', command=checkout_fn).place(x=198, y=380)
    Button(frm_left_checkindate, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_checkindate, text='CHECK IN', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_checkindate_bg = Frame(frm_right_checkindate, bg='#DDDDDD')
    frm_right_checkindate_bg.place(x=276, y=258, width=750, height=500)
    Label(frm_right_checkindate_bg, text='เริ่มวันที่ : ', bg='#DDDDDD').place(x=132, y=60)
    entry_startdate_in = Entry(frm_right_checkindate_bg).place(x=250, y=60)
    Label(frm_right_checkindate_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=570, y=60)
    Label(frm_right_checkindate_bg, text='สิ้นสุดวันที่ : ', bg='#DDDDDD').place(x=109, y=120)
    entry_enddate_in = Entry(frm_right_checkindate_bg).place(x=250, y=120)
    Label(frm_right_checkindate_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=570, y=120)
    Label(frm_right_checkindate_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD').place(x=121, y=180)
    entry_user_in = Entry(frm_right_checkindate_bg).place(x=250, y=180)
    Button(frm_right_checkindate_bg, image=btn_back,bd=0, bg='#DDDDDD', command=checkin_fn).place(x=150, y=250)
    Button(frm_right_checkindate_bg, image=btn_next,bd=0, bg='#DDDDDD').place(x=450, y=250)
    Button(frm_right_checkindate_bg, image=btn_paperform,bd=0, bg='#DDDDDD').place(x=280, y=360)

def checkout_fn() : #หน้า Check Out #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Check Out")
    frm_main_checkout = Frame(root, bg='black')
    frm_main_checkout.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_checkout = Frame(frm_main_checkout, bg='#084235')
    frm_left_checkout.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkout = Frame(frm_main_checkout, bg='white')
    frm_right_checkout.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_checkout, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_checkout, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_checkout, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_checkout, image=btn_checkout, bd=0, bg='#084235', command=checkout_fn).place(x=198, y=380)
    Button(frm_left_checkout, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    
    #RIGHT
    Label(frm_right_checkout, text='CHECK OUT', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_checkout_bg = Frame(frm_right_checkout, bg='#DDDDDD')
    frm_right_checkout_bg.place(x=276, y=258, width=750, height=600)
    Label(frm_right_checkout_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=180, y=60)
    entry_phonenum_checkout = Entry(frm_right_checkout_bg).place(x=350, y=60)
    Button(frm_right_checkout_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=670, y=58)       #from database
    Label(frm_right_checkout_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_checkout = Entry(frm_right_checkout_bg).place(x=350, y=120)             #from database
    Label(frm_right_checkout_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=232, y=180)
    entry_roomnum_checkout = Entry(frm_right_checkout_bg).place(x=350, y=180)
    #room type
    Label(frm_right_checkout_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=200, y= 240)
    entry_roomtype_checkout = Entry(frm_right_checkout_bg).place(x=350, y=240)
    Label(frm_right_checkout_bg, text='ชั้น : ', bg='#DDDDDD').place(x=275, y= 300)
    entry_floor_checkout = Entry(frm_right_checkout_bg).place(x=350, y=300)
    Button(frm_right_checkout_bg, image=btn_confirm,bd=0, bg='#DDDDDD', command=checkout_date).place(x=480, y=450)   #ไม่แน่ใจว่ากดยืนยันแล้วจะไปหน้าเลือกวันที่มั้ยแต่ผูกไว้ก่อนนะ

def checkout_date() : #หน้า Check Out ที่ 2 #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 3:09
    #MAIN
    root.title("Riski Apartment : Check Out")
    frm_main_checkoutdate = Frame(root, bg='black')
    frm_main_checkoutdate.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_checkoutdate = Frame(frm_main_checkoutdate, bg='#084235')
    frm_left_checkoutdate.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkoutdate = Frame(frm_main_checkoutdate, bg='white')
    frm_right_checkoutdate.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_checkoutdate, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_checkoutdate, image=btn_checkinout, bd=0 , bg='#084235').place(x=180, y=180)
    Button(frm_left_checkoutdate, image=btn_checkin, bd=0, bg='#084235', command=checkin_fn).place(x=198, y=280)
    Button(frm_left_checkoutdate, image=btn_checkout, bd=0, bg='#084235', command=checkout_fn).place(x=198, y=380)
    Button(frm_left_checkoutdate, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_checkoutdate, text='CHECK OUT', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_checkoutdate_bg = Frame(frm_right_checkoutdate, bg='#DDDDDD')
    frm_right_checkoutdate_bg.place(x=276, y=258, width=750, height=400)
    Label(frm_right_checkoutdate_bg, text='เริ่มวันที่ : ', bg='#DDDDDD').place(x=132, y=60)
    entry_startdate_out = Entry(frm_right_checkoutdate_bg).place(x=250, y=60)
    Label(frm_right_checkoutdate_bg, text='สิ้นสุดวันที่ : ', bg='#DDDDDD').place(x=109, y=120)
    entry_endate_out = Entry(frm_right_checkoutdate_bg).place(x=250, y=120)
    Label(frm_right_checkoutdate_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=570, y=120)
    Label(frm_right_checkoutdate_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD').place(x=121, y=180)
    entry_user_out = Entry(frm_right_checkoutdate_bg).place(x=250, y=180)
    Button(frm_right_checkoutdate_bg, image=btn_back,bd=0, bg='#DDDDDD', command=checkout_fn).place(x=150, y=250)
    Button(frm_right_checkoutdate_bg, image=btn_next,bd=0, bg='#DDDDDD').place(x=450, y=250)

def accountmanage_fn() : #หน้า Main จัดการห้องพัก #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_accmanage = Frame(root, bg='black')
    frm_main_accmanage.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_accmanage = Frame(frm_main_accmanage, bg='#084235')
    frm_left_accmanage.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_accmanage = Frame(frm_main_accmanage, bg='white')
    frm_right_accmanage.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_accmanage, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_accmanage, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_accmanage, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_accmanage, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_accmanage, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_accmanage, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_accmanage, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_accmanage, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

def addempaccount_fn() : #หน้าเพิ่มบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_addempaccount = Frame(root, bg='black')
    frm_main_addempaccount.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_addempaccount = Frame(frm_main_addempaccount, bg='#084235')
    frm_left_addempaccount.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_addempaccount = Frame(frm_main_addempaccount, bg='white')
    frm_right_addempaccount.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_addempaccount, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_addempaccount, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_addempaccount, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_addempaccount, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_addempaccount, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_addempaccount, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_addempaccount, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_addempaccount, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_addempaccount, text='เพิ่มบัญชีพนักงาน', font='Verdana 30 bold', bg='white', fg='#60AC7F').place(x=470, y=50)
    frm_right_addempaccount_bg = Frame(frm_right_addempaccount, bg='#DDDDDD')
    frm_right_addempaccount_bg.place(x=96, y=158, width=1090, height=350)
    Label(frm_right_addempaccount_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=200, y=50)
    entry_name_addempaccount = Entry(frm_right_addempaccount_bg).place(x=270, y=50, width=230)
    Label(frm_right_addempaccount_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=603, y=50)
    entry_surname_addempaccount = Entry(frm_right_addempaccount_bg).place(x=730, y=50, width=230)
    Label(frm_right_addempaccount_bg, text='Username : ', bg='#DDDDDD').place(x=111, y=120)
    entry_username_addempaccount = Entry(frm_right_addempaccount_bg).place(x=270, y=120, width=230)
    Label(frm_right_addempaccount_bg, text='Password : ', bg='#DDDDDD').place(x=570, y=120)
    entry_password_addempaccount = Entry(frm_right_addempaccount_bg).place(x=730, y=120, width=230)
    Label(frm_right_addempaccount_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=152, y=190)
    entry_phone_addempaccount = Entry(frm_right_addempaccount_bg).place(x=270, y=190, width=230)
    Button(frm_right_addempaccount_bg, image=btn_save, bd=0, bg='#DDDDDD').place(x=790, y=220)

def editempaccount_fn() : #หน้าแก้ไขบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_editempaccount = Frame(root, bg='black')
    frm_main_editempaccount.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_editempaccount = Frame(frm_main_editempaccount, bg='#084235')
    frm_left_editempaccount.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_editempaccount = Frame(frm_main_editempaccount, bg='white')
    frm_right_editempaccount.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_editempaccount, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_editempaccount, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_editempaccount, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_editempaccount, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_editempaccount, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_editempaccount, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_editempaccount, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_editempaccount, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_editempaccount, text='แก้ไขบัญชีพนักงาน', font='Verdana 30 bold', bg='white', fg='#60AC7F').place(x=470, y=50)
    frm_right_editempaccount_bg = Frame(frm_right_editempaccount, bg='#DDDDDD')
    frm_right_editempaccount_bg.place(x=96, y=158, width=1090, height=350)
    Label(frm_right_editempaccount_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=200, y=50)
    entry_name_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=50, width=230)
    Label(frm_right_editempaccount_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=603, y=50)
    entry_surname_editempaccount = Entry(frm_right_editempaccount_bg).place(x=730, y=50, width=230)
    Label(frm_right_editempaccount_bg, text='Username : ', bg='#DDDDDD').place(x=111, y=120)
    entry_username_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=120, width=230)
    Label(frm_right_editempaccount_bg, text='Password : ', bg='#DDDDDD').place(x=570, y=120)
    entry_password_editempaccount = Entry(frm_right_editempaccount_bg).place(x=730, y=120, width=230)
    Label(frm_right_editempaccount_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=152, y=190)
    entry_phone_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=190, width=230)
    Button(frm_right_editempaccount_bg, image=btn_delete, bd=0, bg='#DDDDDD').place(x=580, y=220)
    Button(frm_right_editempaccount_bg, image=btn_edit, bd=0, bg='#DDDDDD').place(x=790, y=220)

def addcustomerinfo_fn() : #หน้าเพิ่มข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_addcusinfo = Frame(root, bg='black')
    frm_main_addcusinfo.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_addcusinfo = Frame(frm_main_addcusinfo, bg='#084235')
    frm_left_addcusinfo.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_addcusinfo = Frame(frm_main_addcusinfo, bg='white')
    frm_right_addcusinfo.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_addcusinfo, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_addcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_addcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_addcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_addcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_addcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_addcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_addcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT 
    Label(frm_right_addcusinfo, text='เพิ่มข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#60AC7F').place(x=480, y=50)
    frm_right_addcusinfo_bg = Frame(frm_right_addcusinfo, bg='#DDDDDD')
    frm_right_addcusinfo_bg.place(x=96, y=158, width=1090, height=760)
    Label(frm_right_addcusinfo_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=110, y=50)  #ตัวแปรเปลี่ยนชื่อได้ตามdatabaseที่ออกแบบไว้ได้เลยนะอันนี้เขียนไว้ก่อนเฉยๆ
    entry_name_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=170, y=50)
    Label(frm_right_addcusinfo_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=59, y=150)
    entry_surname_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=170, y=150)
    Label(frm_right_addcusinfo_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=61, y=250)
    entry_phone_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=170, y=250)
    Label(frm_right_addcusinfo_bg, text='เชื้อชาติ : ', bg='#DDDDDD').place(x=65, y=350)
    entry_ethnicity_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=170, y=350)  #ศัพท์จาก apple translate
    Label(frm_right_addcusinfo_bg, text='สัญชาติ : ', bg='#DDDDDD').place(x=67, y=450)
    entry_nation_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=170, y=450)     #nation --> nationality
    Label(frm_right_addcusinfo_bg, text='บ้านเลขที่ : ', bg='#DDDDDD').place(x=600, y=50)
    entry_number_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=50)      #บ้านเลขที่ --> number , จะเปลี่ยนก็ได้ตามใจชอบบ
    Label(frm_right_addcusinfo_bg, text='หมู่บ้าน : ', bg='#DDDDDD').place(x=621, y=150)
    entry_village_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=150)
    Label(frm_right_addcusinfo_bg, text='ถนน : ', bg='#DDDDDD').place(x=645, y=250)
    entry_road_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=250)
    Label(frm_right_addcusinfo_bg, text='ตำบล/แขวง : ', bg='#DDDDDD').place(x=578, y=350)
    entry_subdistrict_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=350)
    Label(frm_right_addcusinfo_bg, text='อำเภอ/เขต : ', bg='#DDDDDD').place(x=588, y=450)
    entry_district_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=450)
    Label(frm_right_addcusinfo_bg, text='จังหวัด : ', bg='#DDDDDD').place(x=632, y=550)
    entry_province_addcusinfo = Entry(frm_right_addcusinfo_bg).place(x=720, y=550)
    Button(frm_right_addcusinfo_bg, image=btn_longsave, bd=0, bg='#DDDDDD').place(x=760, y=650)

def searchcusinfo_fn() :  # search หน้าแก้ไขข้อมูลลูกค้า
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_searchcusinfo = Frame(root, bg='black')
    frm_main_searchcusinfo.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_searchcusinfo = Frame(frm_main_searchcusinfo, bg='#084235')
    frm_left_searchcusinfo.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_searchcusinfo = Frame(frm_main_searchcusinfo, bg='white')
    frm_right_searchcusinfo.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_searchcusinfo, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_searchcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_searchcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_searchcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_searchcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_searchcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_searchcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_searchcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_searchcusinfo, text='แก้ไขข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#60AC7F').place(x=480, y=50)
    frm_right_searchcusinfo_bg = Frame(frm_right_searchcusinfo, bg='#DDDDDD')
    frm_right_searchcusinfo_bg.place(x=245, y=220, width=800, height=400)
    Label(frm_right_searchcusinfo_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD', bd=0).place(x=150, y=70)
    entry_phone_editcus = Entry(frm_right_searchcusinfo_bg).place(x=300, y=70)
    Button(frm_right_searchcusinfo_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=620, y=68)
    Label(frm_right_searchcusinfo_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD', bd=0).place(x=154, y=140)     # info from database
    entry_name_editcus = Entry(frm_right_searchcusinfo_bg).place(x=300, y=140)
    Button(frm_right_searchcusinfo_bg, image=btn_deleteinfo, bd=0, bg='#DDDDDD').place(x=200, y=270)
    Button(frm_right_searchcusinfo_bg, image=btn_edit, bd=0, bg='#DDDDDD', command=editcusinfo_fn).place(x=430, y=270)

def editcusinfo_fn() :  # หน้าแก้ไขข้อมูลลูกค้า
    #MAIN
    root.title("Riski Apartment : Accountmanage")
    frm_main_editcusinfo = Frame(root, bg='black')
    frm_main_editcusinfo.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_editcusinfo = Frame(frm_main_editcusinfo, bg='#084235')
    frm_left_editcusinfo.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_editcusinfo = Frame(frm_main_editcusinfo, bg='white')
    frm_right_editcusinfo.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_editcusinfo, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Label(frm_left_editcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
    Button(frm_left_editcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
    Button(frm_left_editcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
    Label(frm_left_editcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
    Button(frm_left_editcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
    Button(frm_left_editcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
    Button(frm_left_editcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_editcusinfo, text='แก้ไขข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#60AC7F').place(x=480, y=50) # ใส่ปุ่มค้นหา
    frm_right_editcusinfo_bg = Frame(frm_right_editcusinfo, bg='#DDDDDD')
    frm_right_editcusinfo_bg.place(x=96, y=158, width=1090, height=750)
    Label(frm_right_editcusinfo_bg, text='ชื่อ : ', bg='#DDDDDD', bd=0).place(x=110, y=50)
    entry_name_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=170, y=50)
    Label(frm_right_editcusinfo_bg, text='นามสกุล : ', bg='#DDDDDD', bd=0).place(x=59, y=150)
    entry_surname_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=170, y=150)
    Label(frm_right_editcusinfo_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=61, y=250)
    entry_phone_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=170, y=250)
    Label(frm_right_editcusinfo_bg, text='เชื้อชาติ : ', bg='#DDDDDD').place(x=65, y=350)
    entry_ethnicity_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=170, y=350)
    Label(frm_right_editcusinfo_bg, text='สัญชาติ : ', bg='#DDDDDD').place(x=67, y=450)
    entry_nation_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=170, y=450)
    Label(frm_right_editcusinfo_bg, text='บ้านเลขที่ : ', bg='#DDDDDD').place(x=600, y=50)
    entry_number_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=50)
    Label(frm_right_editcusinfo_bg, text='หมู่บ้าน : ', bg='#DDDDDD').place(x=621, y=150)
    entry_village_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=150)
    Label(frm_right_editcusinfo_bg, text='ถนน : ', bg='#DDDDDD').place(x=645, y=250)
    entry_road_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=250)
    Label(frm_right_editcusinfo_bg, text='ตำบล/แขวง : ', bg='#DDDDDD').place(x=578, y=350)
    entry_subdistrict_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=350)
    Label(frm_right_editcusinfo_bg, text='อำเภอ/เขต : ', bg='#DDDDDD').place(x=588, y=450)
    entry_district_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=450)
    Label(frm_right_editcusinfo_bg, text='จังหวัด : ', bg='#DDDDDD').place(x=632, y=550)
    entry_province_editcusinfo = Entry(frm_right_editcusinfo_bg).place(x=720, y=550)
    Button(frm_right_editcusinfo_bg, image=btn_longsave, bd=0, bg='#DDDDDD').place(x=760, y=650)

def roommanage_fn(): # RoomManagement(Admin) เช็คห้องพัก
    root.title("Riski Apartment : Room Management")
    frm_main_roommanage = Frame(root, bg='black')
    frm_main_roommanage.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_roommanage = Frame(frm_main_roommanage, bg='#084235')
    frm_left_roommanage.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_checkin = Frame(frm_main_roommanage, bg='white')
    frm_right_checkin.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_roommanage, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_roommanage, image=btn_CheckRoom, bd=0 , bg='#084235', command=roommanage_fn).place(x=125, y=185)
    Label(frm_left_roommanage, image=btn_roommanage_V2, bd=0, bg='#084235').place(x=125, y=280)
    Button(frm_left_roommanage, image=btn_addRoom, bd=0, bg='#084235', command=addRoom_fn).place(x=180, y=365)
    Button(frm_left_roommanage, image=btn_editRoom, bd=0, bg='#084235', command=editRoom_fn).place(x=180, y=440)
    Button(frm_left_roommanage, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

def addRoom_fn(): #เพิ่มห้องพัก
    root.title("Riski Apartment : Room Management")
    frm_main_addRoom = Frame(root, bg='black')
    frm_main_addRoom.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_addRoom = Frame(frm_main_addRoom, bg='#084235')
    frm_left_addRoom.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_addRoom = Frame(frm_main_addRoom, bg='white')
    frm_right_addRoom.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_addRoom, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_addRoom, image=btn_CheckRoom, bd=0 , bg='#084235', command=roommanage_fn).place(x=125, y=185)
    Label(frm_left_addRoom, image=btn_roommanage_V2, bd=0, bg='#084235').place(x=125, y=280)
    Button(frm_left_addRoom, image=btn_addRoom, bd=0, bg='#084235', command=addRoom_fn).place(x=180, y=365)
    Button(frm_left_addRoom, image=btn_editRoom, bd=0, bg='#084235', command=editRoom_fn).place(x=180, y=440)
    Button(frm_left_addRoom, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    
    #RIGHT
    Label(frm_right_addRoom, text='เพิ่มห้องพัก', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_addRoom_bg = Frame(frm_right_addRoom, bg='#DDDDDD')
    frm_right_addRoom_bg.place(x=276, y=270, width=750, height=400)
    Label(frm_right_addRoom_bg, text='ห้องเลขที่ : ', bg='#DDDDDD').place(x=220, y=60) 
    entry_phonenum_checkin = Entry(frm_right_addRoom_bg).place(x=350, y=60)
    Label(frm_right_addRoom_bg, text='ชั้น : ', bg='#DDDDDD').place(x=272, y=120)
    entry_name_addRoom = Entry(frm_right_addRoom_bg).place(x=350, y=120)
    Label(frm_right_addRoom_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=198, y=180)
    #room type
    room_type = ["รายเดือนแอร์", "รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_addRoom_bg, *room_type).place(x=350, y=180, width=310)
    Button(frm_right_addRoom_bg, image=btn_add,bd=0, bg='#DDDDDD',).place(x=485, y=270)

def editRoom_fn(): #แก้ไขห้องพัก
    root.title("Riski Apartment : Room Management")
    frm_main_editRoom = Frame(root, bg='black')
    frm_main_editRoom.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_editRoom = Frame(frm_main_editRoom, bg='#084235')
    frm_left_editRoom.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_editRoom = Frame(frm_main_editRoom, bg='white')
    frm_right_editRoom.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_editRoom, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_editRoom, image=btn_CheckRoom, bd=0 , bg='#084235', command=roommanage_fn).place(x=125, y=185)
    Label(frm_left_editRoom, image=btn_roommanage_V2, bd=0, bg='#084235').place(x=125, y=280)
    Button(frm_left_editRoom, image=btn_addRoom, bd=0, bg='#084235', command=addRoom_fn).place(x=180, y=365)
    Button(frm_left_editRoom, image=btn_editRoom, bd=0, bg='#084235', command=editRoom_fn).place(x=180, y=440)
    Button(frm_left_editRoom, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    
    #RIGHT
    Label(frm_right_editRoom, text='แก้ไขห้องพัก', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=100)
    frm_right_editRoom_bg = Frame(frm_right_editRoom, bg='#DDDDDD')
    frm_right_editRoom_bg.place(x=276, y=270, width=750, height=450)
    Label(frm_right_editRoom_bg, text='ห้องเลขที่ : ', bg='#DDDDDD').place(x=220, y=60)     
    entry_phonenum_editRoom = Entry(frm_right_editRoom_bg).place(x=350, y=60)
    Button(frm_right_editRoom_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=660, y=60)
    Label(frm_right_editRoom_bg, text='ชั้น : ', bg='#DDDDDD').place(x=272, y=120)
    entry_name_editRoom = Entry(frm_right_editRoom_bg).place(x=350, y=120)
    Label(frm_right_editRoom_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=198, y=180)
    #room type
    room_type = ["รายเดือนแอร์", "รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_editRoom_bg, *room_type).place(x=350, y=180, width=310)
    #room state
    Label(frm_right_editRoom_bg, text='สถานะห้อง : ', bg='#DDDDDD').place(x=198, y=250)
    room_state = ["ว่าง","ว่าง", "ไม่ว่าง"]
    roomstate = OptionMenu(frm_right_editRoom_bg, *room_state).place(x=350, y=250, width=310)
    Button(frm_right_editRoom_bg, image=btn_edit,bd=0, bg='#DDDDDD',).place(x=485, y=350)

def service_fn() : #หน้า Main บริการต่าง ๆ #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 14:34 07/04/2023
    #MAIN
    root.title("Riski Apartment : บริการต่าง ๆ")
    frm_main_service = Frame(root, bg='black')
    frm_main_service.place(x=0, y=0, width = w, height = h)    

    #FRAME LEFT 
    frm_left_service = Frame(frm_main_service, bg='#084235')
    frm_left_service.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_service, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_service = Frame(frm_main_service, bg='white')
    frm_right_service.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_service, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_service, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_service, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_service, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_service, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

def ratemanage_fn() : #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:01 07/04/2023
    #MAIN
    root.title("Riski Apartment : กำหนดอัตราค่าบริการ")
    frm_main_ratemanage = Frame(root, bg='black')
    frm_main_ratemanage.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_ratemanage = Frame(frm_main_ratemanage, bg='#084235')
    frm_left_ratemanage.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_ratemanage, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_ratemanage = Frame(frm_main_ratemanage, bg='white')
    frm_right_ratemanage.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_ratemanage, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_ratemanage, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_ratemanage, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_ratemanage, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_ratemanage, text='กำหนดอัตราค่าบริการ', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=400, y=30)
    Button(frm_right_ratemanage, width=25, height=20, bd=0, bg='#DDDDDD', command=roomrate_fn).place(x=150, y=200)
    Label(frm_right_ratemanage, image=btn_room, bd=0, bg='#DDDDDD').place(x=315, y=430)
    Button(frm_right_ratemanage, width=25, height=20, bd=0, bg='#DDDDDD', command=waterelectricrate_fn).place(x=750, y=200)
    Label(frm_right_ratemanage, image=btn_water, bd=0, bg='#DDDDDD').place(x=885, y=400)
    Label(frm_right_ratemanage, image=btn_electricity, bd=0, bg='#DDDDDD').place(x=965, y=500)
    Label(frm_right_ratemanage, text='ค่าห้องพัก', bg='white', fg='#084235').place(x=300, y=720)
    Label(frm_right_ratemanage, text='ค่าน้ำ/ไฟ', bg='white', fg='#084235').place(x=900, y=720)

def roomrate_fn() : #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 17:11 07/04/2023
    #MAIN
    root.title("Riski Apartment : ชำระค่าบริการ")
    frm_main_roomrate = Frame(root, bg='black')
    frm_main_roomrate.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_roomrate = Frame(frm_main_roomrate, bg='#084235')
    frm_left_roomrate.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_roomrate, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_roomrate = Frame(frm_main_roomrate, bg='white')
    frm_right_roomrate.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_roomrate, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_roomrate, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_roomrate, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_roomrate, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_roomrate, text='ค่าห้องพัก', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=510, y=30)
    frm_right_roomrate_bg = Frame(frm_right_roomrate, bg='#DDDDDD')
    frm_right_roomrate_bg.place(x=276, y=158, width=750, height=400)
    Label(frm_right_roomrate_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=170, y=60)
    room_type = ["รายเดือนแอร์", "รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_roomrate_bg, *room_type).place(x=320, y=60, width=310)
    Label(frm_right_roomrate_bg, text='ราคาเดิม : ', bg='#DDDDDD').place(x=190, y=120)
    entry_oldrate_roomrate = Entry(frm_right_roomrate_bg).place(x=320, y=120)
    Label(frm_right_roomrate_bg, text='ราคาใหม่ : ', bg='#DDDDDD').place(x=189, y=180)
    entry_oldrate_roomrate = Entry(frm_right_roomrate_bg).place(x=320, y=180)
    Button(frm_right_roomrate_bg, image=btn_save, bg='#DDDDDD', bd=0).place(x=450, y=280)

def waterelectricrate_fn() : #หน้า กำหนดค่าน้ำค่าไฟต่อหน่วย #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 17:06 07/04/2023
    #MAIN
    root.title("Riski Apartment : กำหนดค่าน้ำ ค่าไฟ")
    frm_main_waterelec = Frame(root, bg='black')
    frm_main_waterelec.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_waterelec = Frame(frm_main_waterelec, bg='#084235')
    frm_left_waterelec.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_waterelec, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_waterelec = Frame(frm_main_waterelec, bg='white')
    frm_right_waterelec.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_waterelec, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_waterelec, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_waterelec, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_waterelec, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_waterelec, text='ค่าน้ำ/ไฟ ต่อหน่วย', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=475, y=30)
    #WATER RATE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=100, y=120)
    #WATER CHARGE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=700, y=120)
    #ELECTRICITY RATE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=100, y=550)
    #ELECTRICITY CHARGE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=700, y=550)

def payment_fn() : #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:11 07/04/2023
    #MAIN
    root.title("Riski Apartment : ชำระค่าบริการ")
    frm_main_payment = Frame(root, bg='black')
    frm_main_payment.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_payment = Frame(frm_main_payment, bg='#084235')
    frm_left_payment.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_payment, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_payment = Frame(frm_main_payment, bg='white')
    frm_right_payment.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_payment, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_payment, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_payment, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_payment, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT

def help_fn() : #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:11 07/04/2023
    #MAIN
    root.title("Riski Apartment : บริการช่วยเหลือ")
    frm_main_help = Frame(root, bg='black')
    frm_main_help.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_help = Frame(frm_main_help, bg='#084235')
    frm_left_help.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_help, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_help = Frame(frm_main_help, bg='white')
    frm_right_help.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_help, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
    Button(frm_left_help, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
    Button(frm_left_help, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
    Button(frm_left_help, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

  
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
btn_next = PhotoImage(file='button/btn_next.png')
btn_back = PhotoImage(file='button/btn_back.png')
btn_finish = PhotoImage(file='button/btn_finish.png')
btn_paperform = PhotoImage(file='button/btn_paperform.png')
btn_confirm = PhotoImage(file='button/btn_confirm.png')
btn_empmanage = PhotoImage(file='button/btn_empmanage.png')
btn_addempacc = PhotoImage(file='button/btn_addempacc.png')
btn_editempacc = PhotoImage(file='button/btn_editempacc.png')
btn_editcusinfo = PhotoImage(file='button/btn_editcusinfo.png')
btn_cusmanage = PhotoImage(file='button/btn_cusmanage.png')
btn_addcusinfo = PhotoImage(file='button/btn_addcusinfo.png')
btn_save = PhotoImage(file='button/btn_save.png')
btn_delete = PhotoImage(file='button/btn_delete.png')
btn_edit = PhotoImage(file='button/btn_edit.png')
btn_longsave = PhotoImage(file='button/btn_longsave.png')
btn_search = PhotoImage(file='button/btn_search.png').subsample(2,2)
btn_deleteinfo = PhotoImage(file='button/btn_deleteinfo.png')
btn_CheckRoom = PhotoImage(file='button/btn_CheckRoom.png')
btn_addRoom = PhotoImage(file='button/btn_addRoom.png')
btn_editRoom = PhotoImage(file='button/btn_editRoom.png')
btn_roommanage_V2 = PhotoImage(file='button/btn_roommanage_V2.png')
btn_add = PhotoImage(file='button/btn_add.png')
btn_ratemanage = PhotoImage(file='button/btn_ratemanage.png')
btn_payment = PhotoImage(file='button/btn_payment.png')
btn_help = PhotoImage(file='button/btn_help.png')
btn_room = PhotoImage(file='button/btn_room.png')
btn_water = PhotoImage(file='button/btn_water.png')
btn_electricity = PhotoImage(file='button/btn_electricity.png')


#Background
bg_login = PhotoImage(file = 'img/img_bglogin.png')
login_fn()
root.mainloop()