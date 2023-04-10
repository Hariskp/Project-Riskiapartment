from tkinter import*
import sqlite3
from tkinter import ttk 
from tkinter import messagebox

#CREATE MAINWINDOW
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

#CREATE CONNECTION WITH SQLITE3
def createconnection() : 
    global conn, cursor
    conn = sqlite3.connect('database/riski_database.db')
    cursor = conn.cursor()

def login_backend() :
    global db_user, name_user
    #Existence Check
    if userentry.get() == "" :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอก Username")
        frm_left_login_entry_username.focus_force()
    else :
        if passwordentry.get() == "" :
            messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอก Password")
            frm_left_login_entry_password.focus_force()
        else :
            sql = "SELECT * FROM user WHERE username=? and password=?"
            cursor.execute(sql, [userentry.get().lower(), passwordentry.get().lower()])
            db_user = cursor.fetchone()
            if db_user :
                home_fn()
                name_user = db_user[3] + " " + db_user[4]
            else :
                messagebox.showerror("Riski Apartment : Error", "Username หรือ Password ผิด")
                frm_left_login_entry_username.delete(0, END)
                frm_left_login_entry_password.delete(0, END)
                frm_left_login_entry_username.focus_force()

def login_fn() : #หน้า Login #By Haris
    global frm_left_login_entry_username, frm_left_login_entry_password
    #MAIN
    root.title("Riski Apartment : เข้าสู่ระบบ")
    frm_main_login = Frame(root, bg='black')
    frm_main_login.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_login = Frame(root, bg='white')
    frm_left_login.place(x=0, y=0, width=1250, height=1080)

    #FRAME RIGHT
    frm_right_login = Frame(root, bg='#084235')
    frm_right_login.place(x=1251, y=0, width=669, height=1080)

    #LEFT
    Label(frm_left_login, text='Sign in to Riski Apartment', bg='white', font = 'Calibri 55 bold', fg='#60AC7F').place(x=200, y=110)
    Label(frm_left_login, text='Username', bg='white', fg='#3F9878', font = 'Calibri 40').place(x=360, y=300)
    frm_left_login_entry_username = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0, textvariable=userentry) #Spy
    frm_left_login_entry_username.focus_force()
    userentry.set('')
    frm_left_login_entry_username.place(x=380, y=400, height=50)
    Label(frm_left_login, text='Password', bg='white', fg='#3F9878', font = 'Calibri 40').place(x=360, y=480)
    frm_left_login_entry_password = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0,show="*", textvariable=passwordentry) #Spy
    frm_left_login_entry_password.place(x=380, y=580, height=50)
    passwordentry.set('')
    Button(frm_left_login, image=btn_login, bd=0, bg='white', command=login_backend).place(x=480, y=680)

    #RIGHT
    Label(frm_right_login, image=img_riskilogo, bg='#084235').place(x=93, y=30)
    Label(frm_right_login, text='Welcome Back!', bg='#084235', fg='white', font = 'Calibri 50 bold').place(x=120, y=300)
    Label(frm_right_login, text='to keep connected with us please\n login your personal info', font = 'Calibri 20 bold', bg='#084235', fg='white').place(x=150, y=380)
    Label(frm_right_login, text='contact', font = 'Calibri 20 bold', bg='#084235', fg='white').place(x=300, y=700)
    Label(frm_right_login, image=img_phonenumber).place(x=240, y=750)
    Label(frm_right_login, text='sutee.prodpran@gmail.com', font = 'Calibri 16 bold', bg='#084235', fg='white').place(x=230, y=840)
    Label(frm_right_login, text='THA IT PAK KRET NONTHABURI 11120', font = 'Calibri 14 bold', bg='#084235', fg='white').place(x=200, y=900)

def home_fn() : #หน้า Home #By Haris
    global db_room
    name_user = db_user[3] + " " + db_user[4]
    #MAIN
    root.title("Riski Apartment : หน้าหลัก")
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
    Button(frm_left_home, image=btn_inforeport, bd=0, bg='#084235', command=datareporttable_fn).place(x=180, y=280)
    Button(frm_left_home, image=btn_accmanage, bd=0, bg='#084235', command=accountmanage_fn).place(x=180, y=380)
    Button(frm_left_home, image=btn_roommanage, bd=0, bg='#084235', command=roommanage_fn).place(x=180, y=480)
    Button(frm_left_home, image=btn_service, bd=0, bg='#084235', command=service_fn).place(x=180, y=580)
    Button(frm_left_home, image=btn_signout, bd=0, bg='#084235', command=login_fn).place(x=30, y=900)
    #Welcome
    Label(frm_left_home, text='ยินดีต้อนรับ', bg='#084235', fg='white', font = 'Calibri 25 bold').place(x=110, y=700)
    name_lastname = Label(frm_left_home, text=name_user, bg='#084235', fg='white', font = 'Calibri 25 bold').place(x=200, y=760)

    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_home, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350) 
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))
        
def checkinout_fn() : #หน้า Main Check In/Out#โค้ดนี้กำลังแก้ไขโดย นัท 06/04/2023 เวลา 17:30
    #MAIN
    root.title("Riski Apartment : เช็คอิน/เอ้าท์")
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

    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_inout, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350)
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))

def checkin_fn() : #หน้า Check In #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : เช็คอิน")
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
    root.title("Riski Apartment : เช็คอิน")
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
    Button(frm_right_checkindate_bg, image=btn_finish,bd=0, bg='#DDDDDD').place(x=450, y=250)
    Button(frm_right_checkindate_bg, image=btn_paperform,bd=0, bg='#DDDDDD').place(x=280, y=360)

def checkout_fn() : #หน้า Check Out #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : เช็คเอ้าท์")
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
    root.title("Riski Apartment : เช็คเอ้าท์")
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
    Button(frm_right_checkoutdate_bg, image=btn_finish,bd=0, bg='#DDDDDD').place(x=450, y=250)

def accountmanage_fn() : #หน้า Main จัดการบัญชี #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : จัดการบัญชี")
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
    if db_user[5] == "A" :
        Label(frm_left_accmanage, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_accmanage, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
        Button(frm_left_accmanage, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
        Label(frm_left_accmanage, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
        Button(frm_left_accmanage, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
        Button(frm_left_accmanage, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
        Button(frm_left_accmanage, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)
    if db_user[5] == "U" :
        Label(frm_left_accmanage, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_accmanage, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=270)
        Button(frm_left_accmanage, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=350)
        Button(frm_left_accmanage, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)


    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_accmanage, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350)
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))


def addempaccount_fn() : #หน้าเพิ่มบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    global db_employee, entry_name_addempaccount, entry_surname_addempaccount, entry_username_addempaccount, entry_password_addempaccount, entry_phone_addempaccount
    #MAIN
    root.title("Riski Apartment : เพิ่มบัญชีพนักงาน")
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
    Label(frm_right_addempaccount, text='เพิ่มบัญชีพนักงาน', font='Verdana 30 bold', bg='white', fg='#376957').place(x=470, y=50)
    frm_right_addempaccount_bg = Frame(frm_right_addempaccount, bg='#DDDDDD')
    frm_right_addempaccount_bg.place(x=96, y=158, width=1090, height=350)
    Label(frm_right_addempaccount_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=200, y=50)
    entry_name_addempaccount = Entry(frm_right_addempaccount_bg, textvariable=name_addemp) #Spy
    entry_name_addempaccount.place(x=270, y=50, width=230) 
    Label(frm_right_addempaccount_bg, text='นามสกุล : ', bg='#DDDDDD')
    frm_right_addempaccount_bg.place(x=603, y=50)
    entry_surname_addempaccount = Entry(frm_right_addempaccount_bg, textvariable=lastname_addemp) #Spy
    entry_surname_addempaccount.place(x=730, y=50, width=230) 
    Label(frm_right_addempaccount_bg, text='Username : ', bg='#DDDDDD').place(x=111, y=120)
    entry_username_addempaccount = Entry(frm_right_addempaccount_bg, textvariable=username_addemp) #Spy
    entry_username_addempaccount.place(x=270, y=120, width=230) 
    Label(frm_right_addempaccount_bg, text='Password : ', bg='#DDDDDD').place(x=570, y=120) 
    entry_password_addempaccount = Entry(frm_right_addempaccount_bg, textvariable=password_addemp) #Spy
    entry_password_addempaccount.place(x=730, y=120, width=230) 
    Label(frm_right_addempaccount_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=152, y=190) 
    entry_phone_addempaccount = Entry(frm_right_addempaccount_bg, textvariable=phone_addemp) #Spy
    entry_phone_addempaccount.place(x=270, y=190, width=230)
    Button(frm_right_addempaccount_bg, image=btn_save, bd=0, bg='#DDDDDD', command=addempaccount_backend).place(x=790, y=220)

    #CALL TREEVIEW
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_addempaccount, columns=("username_", "pwd_", "fname_", "lname_","phonenum_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('username_', text="Username", anchor=CENTER)
    mytree.heading('pwd_', text="Password", anchor=CENTER)
    mytree.heading('fname_', text="ชื่อ", anchor=CENTER)
    mytree.heading('lname_', text="นามสกุล", anchor=CENTER)
    mytree.heading('phonenum_', text="เบอร์โทร", anchor=CENTER)

    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('username_', anchor=W, width=200)
    mytree.column('pwd_', anchor=W, width=200)
    mytree.column('fname_', anchor=W, width=250)
    mytree.column('lname_', anchor=W, width=250)
    mytree.column('phonenum_', anchor=W, width=185)
    mytree.place(x=100, y=550, width=1090, height=400)
    #Connect Database user table
    db_employee = conn.execute('SELECT * FROM user')
    #Insert Data to tree
    for i in db_employee :
        mytree.insert("", 'end', values=(i[1], i[2], i[3], i[4], i[0]))

def addempaccount_backend() :
    sql = "SELECT * FROM user WHERE phonenumber=?"
    cursor.execute(sql, [phone_addemp.get()])
    db_phonecheck = cursor.fetchone()

    status = "U"
    #Existence Check
    if name_addemp.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกชื่อ")
        entry_name_addempaccount.focus_force()
    elif lastname_addemp.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกนามสกุล")
        entry_surname_addempaccount.focus_force()
    elif username_addemp.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอก Username")
        entry_username_addempaccount.focus_force()
    elif password_addemp.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอก Password")
        entry_password_addempaccount.focus_force()
    elif phone_addemp.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเบอร์โทรศัพท์")
        entry_phone_addempaccount.focus_force()   
    elif phone_addemp.get().isnumeric == False :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเบอร์โทรศัพท์เป็นตัวเลข")
        entry_phone_addempaccount.focus_force()   
    elif len(phone_addemp.get()) != 10 :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเบอร์โทรศัพท์ให้ครบ 10 ตัว")
    elif db_phonecheck is not None and phone_addemp.get() == db_phonecheck[0]:
        messagebox.showerror("Riski Apartment : Error", "เบอร์โทรศัพท์นี้ถูกใช้ไปแล้ว")
        entry_phone_addempaccount.focus_force() 
    else :
        sql = '''INSERT INTO user (phonenumber, username, password, name, lastname, status) VALUES (?,?,?,?,?,?)'''
        cursor.execute(sql, [phone_addemp.get(), username_addemp.get(), password_addemp.get(), name_addemp.get(), lastname_addemp.get(), status])
        conn.commit()
        retrivedata()
        messagebox.showinfo("Cryptonite : Successfully", "เพิ่มข้อมูลพนักงานเสร็จสิ้น")
        entry_name_addempaccount.delete(0, END)
        entry_surname_addempaccount.delete (0, END)
        entry_username_addempaccount.delete(0, END)
        entry_password_addempaccount.delete(0, END)
        entry_phone_addempaccount.delete(0, END)
    addempaccount_fn()
    
def editempaccount_fn() : #หน้าแก้ไขบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : แก้ไขบัญชีพนักงาน")
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
    Label(frm_right_editempaccount, text='แก้ไขบัญชีพนักงาน', font='Verdana 30 bold', bg='white', fg='#376957').place(x=470, y=50)
    frm_right_editempaccount_bg = Frame(frm_right_editempaccount, bg='#DDDDDD')
    frm_right_editempaccount_bg.place(x=96, y=158, width=1090, height=350)
    Label(frm_right_editempaccount_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=330, y=50)
    entry_findphone_editempaccount = Entry(frm_right_editempaccount_bg).place(x=500, y=50, width=250)
    Button(frm_right_editempaccount_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=780, y=50)
    Label(frm_right_editempaccount_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=200, y=100)
    entry_name_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=100, width=230)
    Label(frm_right_editempaccount_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=603, y=100)
    entry_surname_editempaccount = Entry(frm_right_editempaccount_bg).place(x=730, y=100, width=230)
    Label(frm_right_editempaccount_bg, text='Username : ', bg='#DDDDDD').place(x=111, y=150)
    entry_username_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=150, width=230)
    Label(frm_right_editempaccount_bg, text='Password : ', bg='#DDDDDD').place(x=570, y=150)
    entry_password_editempaccount = Entry(frm_right_editempaccount_bg).place(x=730, y=150, width=230)
    Label(frm_right_editempaccount_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=152, y=200)
    entry_phone_editempaccount = Entry(frm_right_editempaccount_bg).place(x=270, y=200, width=230)
    Button(frm_right_editempaccount_bg, image=btn_delete, bd=0, bg='#DDDDDD').place(x=580, y=240)
    Button(frm_right_editempaccount_bg, image=btn_edit, bd=0, bg='#DDDDDD').place(x=790, y=240)

    #CALL TREEVIEW
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_editempaccount, columns=("username_", "pwd_", "fname_", "lname_","phonenum_"), height=2) #ไม่แน่ใจ ชื่อตัวแปร ซ้ำกับaddempaccount_fn
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('username_', text="Username", anchor=CENTER)
    mytree.heading('pwd_', text="Password", anchor=CENTER)
    mytree.heading('fname_', text="ชื่อ", anchor=CENTER)
    mytree.heading('lname_', text="นามสกุล", anchor=CENTER)
    mytree.heading('phonenum_', text="เบอร์โทร", anchor=CENTER)

    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('username_', anchor=W, width=200)
    mytree.column('pwd_', anchor=W, width=200)
    mytree.column('fname_', anchor=W, width=250)
    mytree.column('lname_', anchor=W, width=250)
    mytree.column('phonenum_', anchor=W, width=185)
    mytree.place(x=100, y=550, width=1090, height=400)
    #Connect Database user table
    db_employee = conn.execute('SELECT * FROM user')
    #Insert Data to tree
    for i in db_employee :
        mytree.insert("", 'end', values=(i[1], i[2], i[3], i[4], i[0]))

def addcustomerinfo_fn() : #หน้าเพิ่มข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    #MAIN
    root.title("Riski Apartment : เพิ่มข้อมูลลูกค้า")
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
    if db_user[5] == "A" :
        Label(frm_left_addcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_addcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
        Button(frm_left_addcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
        Label(frm_left_addcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
        Button(frm_left_addcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
        Button(frm_left_addcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
        Button(frm_left_addcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)
    if db_user[5] == "U" :
        Label(frm_left_addcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_addcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=270)
        Button(frm_left_addcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=350)
        Button(frm_left_addcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT 
    Label(frm_right_addcusinfo, text='เพิ่มข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#376957').place(x=480, y=50)
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

def searchcusinfo_fn() :  # search หน้าแก้ไขข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : แก้ไขข้อมูลลูกค้า")
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
    if db_user[5] == "A" :
        Label(frm_left_searchcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_searchcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
        Button(frm_left_searchcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
        Label(frm_left_searchcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
        Button(frm_left_searchcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
        Button(frm_left_searchcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
        Button(frm_left_searchcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)
    if db_user[5] == "U" :
        Label(frm_left_searchcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_searchcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=270)
        Button(frm_left_searchcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=350)
        Button(frm_left_searchcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_searchcusinfo, text='แก้ไขข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#376957').place(x=480, y=50)
    frm_right_searchcusinfo_bg = Frame(frm_right_searchcusinfo, bg='#DDDDDD')
    frm_right_searchcusinfo_bg.place(x=245, y=220, width=800, height=400)
    Label(frm_right_searchcusinfo_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD', bd=0).place(x=150, y=70)
    entry_phone_editcus = Entry(frm_right_searchcusinfo_bg).place(x=300, y=70)
    Button(frm_right_searchcusinfo_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=620, y=68)
    Label(frm_right_searchcusinfo_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD', bd=0).place(x=154, y=140)     # info from database
    entry_name_editcus = Entry(frm_right_searchcusinfo_bg).place(x=300, y=140)
    Button(frm_right_searchcusinfo_bg, image=btn_deleteinfo, bd=0, bg='#DDDDDD').place(x=200, y=270)
    Button(frm_right_searchcusinfo_bg, image=btn_edit, bd=0, bg='#DDDDDD', command=editcusinfo_fn).place(x=430, y=270)

def editcusinfo_fn() :  # หน้าแก้ไขข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : แก้ไขข้อมูลลูกค้า")
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
    if db_user[5] == "A" :
        Label(frm_left_editcusinfo, image=btn_empmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_editcusinfo, image=btn_addempacc, bd=0 , bg='#084235', command=addempaccount_fn).place(x=180, y=270)
        Button(frm_left_editcusinfo, image=btn_editempacc, bd=0 , bg='#084235', command=editempaccount_fn).place(x=180, y=350)
        Label(frm_left_editcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=435)
        Button(frm_left_editcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=520)
        Button(frm_left_editcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=600)
        Button(frm_left_editcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)
    if db_user[5] == "U" :
        Label(frm_left_editcusinfo, image=btn_cusmanage, bd=0 , bg='#084235').place(x=125, y=185)
        Button(frm_left_editcusinfo, image=btn_addcusinfo, bd=0 , bg='#084235', command=addcustomerinfo_fn).place(x=180, y=270)
        Button(frm_left_editcusinfo, image=btn_editcusinfo, bd=0 , bg='#084235', command=searchcusinfo_fn).place(x=180, y=350)
        Button(frm_left_editcusinfo, image=btn_home, command=home_fn, bd=0, bg='#084235').place(x=30, y=900)

    #RIGHT
    Label(frm_right_editcusinfo, text='แก้ไขข้อมูลลูกค้า', font='Verdana 30 bold', bg='white', fg='#376957').place(x=480, y=50) # ใส่ปุ่มค้นหา
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

def roommanage_fn(): # RoomManagement(Admin) เช็คห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : เช็คห้องพัก")
    frm_main_roommanage = Frame(root, bg='black')
    frm_main_roommanage.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_roommanage = Frame(frm_main_roommanage, bg='#084235')
    frm_left_roommanage.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_roommanage = Frame(frm_main_roommanage, bg='white')
    frm_right_roommanage.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_roommanage, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    if db_user[5] == "A" :
        Button(frm_left_roommanage, image=btn_CheckRoom, bd=0 , bg='#084235', command=roommanage_fn).place(x=125, y=185)
        Label(frm_left_roommanage, image=btn_roommanage_V2, bd=0, bg='#084235').place(x=125, y=280)
        Button(frm_left_roommanage, image=btn_addRoom, bd=0, bg='#084235', command=addRoom_fn).place(x=180, y=365)
        Button(frm_left_roommanage, image=btn_editRoom, bd=0, bg='#084235', command=editRoom_fn).place(x=180, y=440)
        Button(frm_left_roommanage, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    if db_user[5] == "U" :
        Button(frm_left_roommanage, image=btn_CheckRoom, bd=0 , bg='#084235', command=roommanage_fn).place(x=125, y=185)
        Button(frm_left_roommanage, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_roommanage, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350)
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))

def addRoom_fn(): #เพิ่มห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
    root.title("Riski Apartment : เพิ่มห้องพัก")
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

def editRoom_fn(): #แก้ไขห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
    root.title("Riski Apartment : แก้ไขห้องพัก")
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
    room_state = ["ว่าง","ว่าง", "ไม่ว่าง", "ปรับปรุง"]
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
    if db_user[5] == "A" :
        Button(frm_left_service, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
        Button(frm_left_service, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
        Button(frm_left_service, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
        Button(frm_left_service, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    if db_user[5] == "U" :
        Button(frm_left_service, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=180)
        Button(frm_left_service, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=280)
        Button(frm_left_service, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_service, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350)
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))

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
    root.title("Riski Apartment : ค่าห้องพัก")
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
    Label(frm_right_waterelec, text='ค่าน้ำ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=270, y=150)
    Label(frm_right_waterelec, text='ราคาใหม่ :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=130, y=220) 
    entry_waterrate_waterelec = Entry(frm_right_waterelec, width=15).place(x=250, y=225)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD').place(x=305, y=400)
    #WATER CHARGE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=700, y=120)
    Label(frm_right_waterelec, text='Charge ค่าน้ำ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=820, y=150)
    Label(frm_right_waterelec, text='บวกเพิ่ม :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=740, y=220) 
    entry_watercharge_waterelec = Entry(frm_right_waterelec, width=15).place(x=850, y=225)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD').place(x=905, y=400)
    #ELECTRICITY RATE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=100, y=550)
    Label(frm_right_waterelec, text='ค่าไฟ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=270, y=590)
    Label(frm_right_waterelec, text='ราคาใหม่ :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=130, y=650) 
    entry_electricrate_waterelec = Entry(frm_right_waterelec, width=15).place(x=250, y=655)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD').place(x=305, y=800)
    #ELECTRICITY CHARGE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=700, y=550)
    Label(frm_right_waterelec, text='Charge ค่าไฟ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=820, y=590)
    Label(frm_right_waterelec, text='บวกเพิ่ม :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=740, y=650)
    entry_electriccharge_waterelec = Entry(frm_right_waterelec, width=15).place(x=850, y=655)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD').place(x=905, y=800)

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
    if db_user[5] == "A" :
        Button(frm_left_payment, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
        Button(frm_left_payment, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
        Button(frm_left_payment, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
        Button(frm_left_payment, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    if db_user[5] == "U" :
        Button(frm_left_payment, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=180)
        Button(frm_left_payment, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=280)
        Button(frm_left_payment, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_payment, text='ชำระค่าบริการ', bg='white', fg='#376957', font = 'Calibri 40 bold').place(x=475, y=30)
    frm_right_payment_bg = Frame(frm_right_payment, bg='#DDDDDD')
    frm_right_payment_bg.place(x=276, y=158, width=750, height=750)
    Label(frm_right_payment_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=100, y=60)
    entry_phone_payment = Entry(frm_right_payment_bg).place(x=270, y=60)
    Button(frm_right_payment_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=600, y=60)
    Label(frm_right_payment_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=105, y=120)
    entry_name_payment = Entry(frm_right_payment_bg).place(x=270, y=120)
    Label(frm_right_payment_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=120, y=180)
    entry_roomtype_payment = Entry(frm_right_payment_bg).place(x=270, y=180)
    Label(frm_right_payment_bg, text='ค่าเช่าห้อง : ', bg='#DDDDDD').place(x=130, y=240)
    entry_rent_payment = Entry(frm_right_payment_bg).place(x=270, y=240)
    Label(frm_right_payment_bg, text='ค่าไฟ : ', bg='#DDDDDD').place(x=175, y=300)
    entry_electric_payment = Entry(frm_right_payment_bg).place(x=270, y=300)
    Label(frm_right_payment_bg, text='ค่าน้ำ : ', bg='#DDDDDD').place(x=175, y=360)
    entry_water_payment = Entry(frm_right_payment_bg).place(x=270, y=360)
    Label(frm_right_payment_bg, text='รวม : ', bg='#DDDDDD').place(x=190, y=420)
    entry_total_payment = Entry(frm_right_payment_bg).place(x=270, y=420)
    Button(frm_right_payment_bg, image=btn_invoices, bd=0, bg='#DDDDDD').place(x=150, y=600)
    Button(frm_right_payment_bg, image=btn_paystat, bd=0, bg='#DDDDDD', command=paymentstatus_fn).place(x=400, y=600)

def help_fn() : #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:11 07/04/2023 เพิ่มเติมโดย บูม
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
    if db_user[5] == "A" :
        Button(frm_left_help, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
        Button(frm_left_help, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
        Button(frm_left_help, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
        Button(frm_left_help, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    if db_user[5] == "U" :
        Button(frm_left_help, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=180)
        Button(frm_left_help, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=280)
        Button(frm_left_help, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_help, text='บริการช่วยเหลือ', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=475, y=160)
    frm_right_help_bg = Frame(frm_right_help, bg='#DDDDDD')
    frm_right_help_bg.place(x=276, y=270, width=750, height=320)
    Label(frm_right_help_bg, text='วันที่ : ', bg='#DDDDDD').place(x=160, y=50)
    entry_date_help = Entry(frm_right_help_bg).place(x=230, y=50)
    Label(frm_right_help_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD', fg='#969696').place(x=550, y=50)
    Label(frm_right_help_bg, text='เรื่องที่แจ้ง : ', bg='#DDDDDD').place(x=115, y=110)
    entry_inform_help = Entry(frm_right_help_bg).place(x=230, y=110)
    Label(frm_right_help_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD').place(x=120, y=170)
    entry_adminname_help = Entry(frm_right_help_bg).place(x=230, y=170)
    Button(frm_right_help_bg, image=btn_finish, bg='#DDDDDD', bd=0).place(x=360, y=240)

def datareporttable_fn() :  # หน้าข้อมูล / รายงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05

    #MAIN
    root.title("Riski Apartment : ข้อมูล / รายงาน")
    frm_main_datareporttable = Frame(root, bg='black')
    frm_main_datareporttable.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_datareporttable = Frame(frm_main_datareporttable, bg='#084235')
    frm_left_datareporttable.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_datareporttable = Frame(frm_main_datareporttable, bg='white')
    frm_right_datareporttable.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_datareporttable, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_datareporttable, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_datareporttable, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #Create Treeview
    mytree = ttk.Treeview(root)
    mytree= ttk.Treeview(frm_right_datareporttable, columns=("floor_", "roomnum_", "roomstate_"), height=2)
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('floor_', text="ชั้น", anchor=CENTER)
    mytree.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    mytree.heading('roomstate_', text="สถานะ", anchor=CENTER)
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('floor_', anchor=CENTER, width=350)
    mytree.column('roomnum_', anchor=CENTER, width=350)
    mytree.column('roomstate_', anchor=CENTER, width=350)
    mytree.place(x=100, y=50, width=1052, height=900)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        mytree.insert("", 'end', values=(i[1], i[0], i[5]))

def datareport_fn() : # หน้าข้อมูล / รายงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : ข้อมูล / รายงาน")
    frm_main_datareport = Frame(root, bg='black')
    frm_main_datareport.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_datareport = Frame(frm_main_datareport, bg='#084235')
    frm_left_datareport.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_datareport = Frame(frm_main_datareport, bg='white')
    frm_right_datareport.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_datareport, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_datareport, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_datareport, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    if db_user[5] == "A" :
        Button(frm_right_datareport, image=btn_doc, width=250, height=350, bg='#DDDDDD', bd=0, command=servicelog_fn).place(x=170, y=100)
        Label(frm_right_datareport, text='บันทึกการใช้บริการ', fg='#376957', bg='white').place(x=210, y=470)
        Button(frm_right_datareport, image=btn_income, width=250, height=350, bg='#DDDDDD', bd=0, command=income_fn).place(x=535, y=100)
        Label(frm_right_datareport, text='รายรับ', fg='#376957', bg='white').place(x=630, y=470)
        Button(frm_right_datareport, image=btn_pay, width=250, height=350, bg='#DDDDDD', bd=0, command=pay_fn).place(x=900, y=100)
        Label(frm_right_datareport, text='รายจ่าย', fg='#376957', bg='white').place(x=994, y=470)
        Button(frm_right_datareport, image=btn_totalamt, width=250, height=350, bg='#DDDDDD', bd=0, command=totalamt_fn).place(x=170, y=530)
        Label(frm_right_datareport, text='รายได้สุทธิ', fg='#376957', bg='white').place(x=242, y=900)
        Button(frm_right_datareport, image=btn_information, width=250, height=350, bg='#DDDDDD', bd=0, command=receivenoti_fn).place(x=535, y=530)
        Label(frm_right_datareport, text='เรื่องที่รับแจ้ง', fg='#376957', bg='white').place(x=610, y=900)
    if db_user[5] == "U" :
        Button(frm_right_datareport, image=btn_doc, width=250, height=350, bg='#DDDDDD', bd=0, command=servicelog_fn).place(x=170, y=100)
        Label(frm_right_datareport, text='บันทึกการใช้บริการ', fg='#376957', bg='white').place(x=210, y=470)
        Button(frm_right_datareport, image=btn_pay, width=250, height=350, bg='#DDDDDD', bd=0, command=pay_fn).place(x=535, y=100)
        Label(frm_right_datareport, text='รายจ่าย', fg='#376957', bg='white').place(x=630, y=470)
        Button(frm_right_datareport, image=btn_information, width=250, height=350, bg='#DDDDDD', bd=0, command=receivenoti_fn).place(x=900, y=100)
        Label(frm_right_datareport, text='เรื่องที่รับแจ้ง', fg='#376957', bg='white').place(x=994, y=470)

def servicelog_fn() : # หน้าบันทึกการใช้บริการ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : บันทึกการใช้บริการ")
    frm_main_servicelog = Frame(root, bg='black')
    frm_main_servicelog.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_servicelog = Frame(frm_main_servicelog, bg='#084235')
    frm_left_servicelog.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_servicelog = Frame(frm_main_servicelog, bg='white')
    frm_right_servicelog.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_servicelog, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_servicelog, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_servicelog, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_servicelog, text='บันทึกการใช้บริการ', font='Verdana 30 bold', bg='white', fg='#376957').place(x=480, y=80)
    frm_right_servicelog_bg = Frame(frm_right_servicelog, bg='#DDDDDD')
    frm_right_servicelog_bg.place(x=276, y=228, width=750, height=600)
    Label(frm_right_servicelog_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=180, y=60)
    entry_phonenum_servicelog = Entry(frm_right_servicelog_bg).place(x=350, y=60)          #from database
    Button(frm_right_servicelog_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=670, y=58)
    Label(frm_right_servicelog_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_servicelog = Entry(frm_right_servicelog_bg).place(x=350, y=120)             #from database
    Label(frm_right_servicelog_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=232, y=180)
    entry_roomnum_servicelog = Entry(frm_right_servicelog_bg).place(x=350, y=180)
    #room type
    Label(frm_right_servicelog_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=200, y= 240)
    entry_roomtype_servicelog = Entry(frm_right_servicelog_bg).place(x=350, y=240)
    Label(frm_right_servicelog_bg, text='ชั้น : ', bg='#DDDDDD').place(x=275, y= 300)
    entry_floor_servicelog = Entry(frm_right_servicelog_bg).place(x=350, y=300)
    Button(frm_right_servicelog_bg, image=btn_next,bd=0, bg='#DDDDDD', command=servicelogsave_fn).place(x=480, y=450)

def servicelogsave_fn() : # บันทึกการใช้บริการ ค่าน้ำ ค่าไฟ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : บันทึกการใช้บริการ")
    frm_main_servicelogsave = Frame(root, bg='black')
    frm_main_servicelogsave.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_servicelogsave = Frame(frm_main_servicelogsave, bg='#084235')
    frm_left_servicelogsave.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_servicelogsave = Frame(frm_main_servicelogsave, bg='white')
    frm_right_servicelogsave.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_servicelogsave, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_servicelogsave, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_servicelogsave, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_servicelogsave, text='บันทึกการใช้บริการ', font='Verdana 30 bold', bg='white', fg='#376957').place(x=480, y=80)
    frm_right_servicelogsave_bg = Frame(frm_right_servicelogsave, bg='#DDDDDD')
    frm_right_servicelogsave_bg.place(x=256, y=228, width=800, height=650)
    Label(frm_right_servicelogsave_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=150, y=60)
    entry_roomnum_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=60)
    Label(frm_right_servicelogsave_bg, text='ค่าไฟ / หน่วย : ', bg='#DDDDDD').place(x=90, y=120)
    entry_electric_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=120)
    Label(frm_right_servicelogsave_bg, text='ค่าน้ำ / หน่วย : ', bg='#DDDDDD').place(x=92, y=180)
    entry_water_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=180)
    Label(frm_right_servicelogsave_bg, text='เลขมิเตอร์น้ำ : ', bg='#DDDDDD').place(x=108, y=240)
    entry_watermeter_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=240)
    Label(frm_right_servicelogsave_bg, text='เลขมิเตอร์ไฟฟ้า : ', bg='#DDDDDD').place(x=82, y=300)
    entry_electricmeter_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=300)
    Label(frm_right_servicelogsave_bg, text='วันที่บันทึก : ', bg='#DDDDDD').place(x=130, y=360)
    entry_date_servicelogsave = Entry(frm_right_servicelogsave_bg).place(x=270, y=360)
    Label(frm_right_servicelogsave_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=600, y=360)
    Button(frm_right_servicelogsave_bg, image=btn_save,bd=0, bg='#DDDDDD').place(x=400, y=500)

def income_fn() : #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    #MAIN
    root.title("Riski Apartment : รายรับ")
    frm_main_income = Frame(root, bg='black')
    frm_main_income.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_income = Frame(frm_main_income, bg='#084235')
    frm_left_income.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_income = Frame(frm_main_income, bg='white')
    frm_right_income.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_income, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_income, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_income, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_income, text='รายรับ', font='Verdana 30 bold', bg='white', fg='#376957').place(x=580, y=80)
    frm_right_income_bg = Frame(frm_right_income, bg='#DDDDDD')
    frm_right_income_bg.place(x=236, y=228, width=800, height=500)
    Label(frm_right_income_bg, text='เลือกช่วงวันที่ต้องการเช็ค', bg='#DDDDDD', fg='#3F9878').place(x=60, y=35)
    Label(frm_right_income_bg, text='วันที่เริ่มต้น : ', bg='#DDDDDD').place(x=140, y=120)
    entry_startdate_income = Entry(frm_right_income_bg).place(x=280, y=120)
    Label(frm_right_income_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=610, y=120)
    Label(frm_right_income_bg, text='วันที่สิ้นสุด : ', bg='#DDDDDD').place(x=145, y=180)
    entry_enddate_income = Entry(frm_right_income_bg).place(x=280, y=180)
    Label(frm_right_income_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD').place(x=610, y=180)
    Button(frm_right_income_bg, image=btn_find,bd=0, bg='#DDDDDD', command=incometable_fn).place(x=330, y=350)
    
def incometable_fn() : # ตารางรายรับ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 22:07
    #MAIN
    root.title("Riski Apartment : รายรับ")
    frm_main_incometable = Frame(root, bg='black')
    frm_main_incometable.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_incometable = Frame(frm_main_incometable, bg='#084235')
    frm_left_incometable.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_incometable = Frame(frm_main_incometable, bg='white')
    frm_right_incometable.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_incometable, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_incometable, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_incometable, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_incometable, text='รายรับ', font='Verdana 30 bold', bg='white', fg='#376957').place(x=580, y=80)
    Button(frm_right_incometable, image=btn_back, bd=0, bg='white', command=income_fn).place(x=550, y=880)
    #Button(frm_right_incometable, image=btn_printincome, bd=0, bg='white').place(x=850, y=880)

    #Button(frm_right_incometable, image=btn_printincome, bd=0, bg='white').place(x=850, y=880)

    #CALL TREEVIEW
    my_tree = ttk.Treeview(frm_right_incometable,column=("date_","roomnum_","rentroom_","water&electric_","total_"), height=2)
    
    #CREATE HEADING
    my_tree.heading("#0",text='',anchor=W)
    my_tree.heading("date_",text='วันที่',anchor=CENTER)
    my_tree.heading("roomnum_",text='เลขที่ห้อง',anchor=CENTER)
    my_tree.heading("rentroom_",text='ค่าเช่าห้อง',anchor=CENTER)
    my_tree.heading("water&electric_",text='ค่าน้ำ+ค่าไฟ',anchor=CENTER)
    my_tree.heading("total_",text='รวม',anchor=CENTER)
    my_tree.place(x=100,y=190,height=650,width=1052)

    #FORMAT COLUMNS
    my_tree.column("#0",width=0,minwidth=25)
    my_tree.column("date_",anchor=CENTER,width=250)
    my_tree.column("roomnum_",anchor=CENTER,width=200)
    my_tree.column("rentroom_",anchor=CENTER,width=170)
    my_tree.column("water&electric_",anchor=CENTER,width=170)
    my_tree.column("total_",anchor=CENTER,width=250)

#PAY FRAME [ ปุ่มข้อมูล/รายงาน หน้าหลัก หา , ช่องกรอกวันที่เริ่มต้น วันที่สิ้นสุด ] #หน้ารายจ่าย
def pay_fn() :
    #MAIN
    root.title("Riski Apartment : รายจ่าย")
    frm_main_pay = Frame(root, bg='black')
    frm_main_pay.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_pay = Frame(frm_main_pay, bg='#084235')
    frm_left_pay.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_pay = Frame(frm_main_pay, bg='white')
    frm_right_pay.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_pay, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT SIDE [ ปุ่มข้อมูล/รายงาน ]
    Button(frm_left_pay, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185) 
    Button(frm_left_pay, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900) 

    #RIGHT SIDE [ ช่องกรอกวันที่เริ่มต้น วันที่สิ้นสุด ]
    Label(frm_right_pay, text='รายจ่าย', font='Verdana 30 bold', bg='white', fg='#376957').place(x=550, y=20)
    frm_right_pay= Frame(frm_right_pay, bg='#DDDDDD')
    frm_right_pay.place(x=236, y=110, width=800, height=870)

    Label(frm_right_pay, text='เลือกช่วงวันที่ต้องการเช็ค', bg='#DDDDDD', fg='#3F9878').place(x=20, y=20)
    Label(frm_right_pay, text='วันที่เริ่มต้น : ', bg='#DDDDDD').place(x=121, y=116)
    entry_startdate_pay = Entry(frm_right_pay).place(x=260, y=120) 
    Label(frm_right_pay, text='(วว/ดด/ปปปป)', bg='#DDDDDD',fg="#969696").place(x=570, y=116)
    Label(frm_right_pay, text='วันที่สิ้นสุด : ', bg='#DDDDDD').place(x=125, y=176)
    entry_endate_pay = Entry(frm_right_pay).place(x=260, y=180) 
    Label(frm_right_pay, text='(วว/ดด/ปปปป)', bg='#DDDDDD',fg="#969696").place(x=570, y=178)
    Button(frm_right_pay, image=btn_find,bd=0, bg='#DDDDDD').place(x=330, y=250)
    Button(frm_right_pay,image=btn_back, bd=0 ,  bg="#DDDDDD",command=datareport_fn).place(x=560,y=790) 

    #CALL TREEVIEW [ วันที่ รายรับ รายจ่าย รายได้สุทธิ ]
    my_tree = ttk.Treeview(frm_right_pay,column=("date_","waterelectric_","amount_"), height=2)
    
    #CREATE HEADING
    my_tree.heading("#0",text='',anchor=W)
    my_tree.heading("date_",text='วันที่',anchor=CENTER)
    my_tree.heading("waterelectric_",text='รายรับ',anchor=CENTER)
    my_tree.heading("amount_",text='รายจ่าย',anchor=CENTER)
    my_tree.place(x=82,y=330,height=450,width=650)

    #FORMAT COLUMNS
    my_tree.column("#0",width=0,minwidth=25)
    my_tree.column("date_",anchor=CENTER,width=216)
    my_tree.column("waterelectric_",anchor=CENTER,width=216)
    my_tree.column("amount_",anchor=CENTER,width=216)
    
def paymentstatus_fn() : #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 00:07
    #MAIN
    root.title("Riski Apartment : สถานะการชำระเงิน")
    frm_main_paymentstatus = Frame(root, bg='black')
    frm_main_paymentstatus.place(x=0, y=0, width = w, height = h) 

    #FRAME LEFT 
    frm_left_paymentstatus = Frame(frm_main_paymentstatus, bg='#084235')
    frm_left_paymentstatus.place(x=0, y=0, width=650, height=1080)

    #LOGO
    Button(frm_left_paymentstatus, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #FRAME RIGHT
    frm_right_paymentstatus = Frame(frm_main_paymentstatus, bg='white')
    frm_right_paymentstatus.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    if db_user[5] == "A" :
        Button(frm_left_paymentstatus, image=btn_ratemanage, bd=0, bg='#084235', command=ratemanage_fn).place(x=180, y=180)
        Button(frm_left_paymentstatus, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=280)
        Button(frm_left_paymentstatus, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=380)
        Button(frm_left_paymentstatus, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)
    if db_user[5] == "U" :
        Button(frm_left_paymentstatus, image=btn_payment, bd=0, bg='#084235',command=payment_fn).place(x=180, y=180)
        Button(frm_left_paymentstatus, image=btn_help, bd=0, bg='#084235',command=help_fn).place(x=180, y=280)
        Button(frm_left_paymentstatus, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_paymentstatus, text='สถานะการชำระเงิน', bg='white', fg='#376957', font = 'Calibri 40 bold').place(x=430, y=30)
    frm_right_paymentstatus_bg = Frame(frm_right_paymentstatus, bg='#DDDDDD')
    frm_right_paymentstatus_bg.place(x=276, y=158, width=750, height=400)
    Label(frm_right_paymentstatus_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=100, y=60)
    entry_phone_paymentstatus = Entry(frm_right_paymentstatus_bg).place(x=270, y=60)
    Button(frm_right_paymentstatus_bg, image=btn_search, bd=0, bg='#DDDDDD').place(x=600, y=60)
    Label(frm_right_paymentstatus_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=105, y=120)
    entry_name_paymentstatus= Entry(frm_right_paymentstatus_bg).place(x=270, y=120)
    Label(frm_right_paymentstatus_bg, text='สถานะการชำระเงิน : ', bg='#DDDDDD').place(x=52, y=180) #ริสใส่listให้หน่อย
    payment_status = [" ", "ชำระเงินแล้ว", "ยังไม่ได้ชำระเงิน"]
    paymentstatus = OptionMenu(frm_right_paymentstatus_bg, *payment_status).place(x=270, y=180, width=310)
    Button(frm_right_paymentstatus_bg, image=btn_printreceipt, bd=0, bg='#DDDDDD' ).place(x=150, y=280)
    Button(frm_right_paymentstatus_bg, image=btn_finish, bd=0, bg='#DDDDDD' ).place(x=450, y=280)

def totalamt_fn() : #โค้ดนี้กำลงแก้ไขโดย จอม 07/04/2023 เวลา 21:46
    #MAIN
    root.title("Riski Apartment : รายได้สุทธิ")
    frm_main_totalamt = Frame(root, bg='black')
    frm_main_totalamt.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_totalamt = Frame(frm_main_totalamt, bg='#084235')
    frm_left_totalamt.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_totalamt = Frame(frm_main_totalamt, bg='white')
    frm_right_totalamt.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_totalamt, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #LEFT
    Button(frm_left_totalamt, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_totalamt, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT 
    Label(frm_right_totalamt, text='รายได้สุทธิ', font='Verdana 30 bold', bg='white', fg='#376957').place(x=550, y=20)
    frm_right_totalamt = Frame(frm_right_totalamt, bg='#DDDDDD')
    frm_right_totalamt.place(x=236, y=110, width=800, height=870)

    Label(frm_right_totalamt, text='เลือกช่วงวันที่ต้องการเช็ค', bg='#DDDDDD', fg='#3F9878').place(x=20, y=20)
    Label(frm_right_totalamt, text='วันที่เริ่มต้น : ', bg='#DDDDDD').place(x=121, y=116)
    entry_startdate_totalamt = Entry(frm_right_totalamt).place(x=260, y=120)
    Label(frm_right_totalamt, text='(วว/ดด/ปปปป)', bg='#DDDDDD',fg="#969696").place(x=570, y=116)
    Label(frm_right_totalamt, text='วันที่สิ้นสุด : ', bg='#DDDDDD').place(x=125, y=176)
    entry_endate_totalamt = Entry(frm_right_totalamt).place(x=260, y=180)
    Label(frm_right_totalamt, text='(วว/ดด/ปปปป)', bg='#DDDDDD',fg="#969696").place(x=570, y=178)
    Button(frm_right_totalamt, image=btn_find,bd=0, bg='#DDDDDD').place(x=330, y=250)
    Button(frm_right_totalamt,image=btn_printtotalamt, bd=0 ,  bg="#DDDDDD").place(x=570,y=790)

    #CALL TREEVIEW
    my_tree = ttk.Treeview(frm_right_totalamt,column=("date_","revenue_","expenses_","totalamt_"), height=2)
    
    #CREATE HEADING
    my_tree.heading("#0",text='',anchor=W)
    my_tree.heading("date_",text='วันที่',anchor=CENTER)
    my_tree.heading("revenue_",text='รายรับ',anchor=CENTER)
    my_tree.heading("expenses_",text='รายจ่าย',anchor=CENTER)
    my_tree.heading("totalamt_",text='รายได้สุทธิ',anchor=CENTER)
    my_tree.place(x=82,y=330,height=450,width=652)

    #FORMAT COLUMNS
    my_tree.column("#0",width=0,minwidth=25)
    my_tree.column("date_",anchor=CENTER,width=150)
    my_tree.column("revenue_",anchor=CENTER,width=150)
    my_tree.column("expenses_",anchor=CENTER,width=150)
    my_tree.column("totalamt_",anchor=CENTER,width=150)

def receivenoti_fn() : #โค้ดนี้กำลงแก้ไขโดย จอม 07/04/2023 เวลา 00:37
    #MAIN
    root.title("Riski Apartment : เรื่องที่รับแจ้ง")
    frm_main_receivenoti = Frame(root, bg='black')
    frm_main_receivenoti.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_receivenoti = Frame(frm_main_receivenoti, bg='#084235')
    frm_left_receivenoti.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_receivenoti = Frame(frm_main_receivenoti, bg='white')
    frm_right_receivenoti.place(x=651,y=0, width= 1269, height=1080)

    #LEFT
    Button(frm_left_receivenoti, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_receivenoti, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #LOGO
    Button(frm_left_receivenoti, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)
    
    #RIGHT 
    Label(frm_right_receivenoti, text='เรื่องที่รับแจ้ง', font='Verdana 30 bold', bg='white', fg='#376957').place(x=527, y=20)
    frm_right_receivenoti = Frame(frm_right_receivenoti, bg='#DDDDDD')
    frm_right_receivenoti.place(x=236, y=110, width=800, height=820 )
    Button(frm_right_receivenoti,image=btn_back,bd=0 ,  bg='#DDDDDD',command=datareport_fn).place(x=570,y=720)

    #CALL TREEVIEW
    my_tree = ttk.Treeview(frm_right_receivenoti,column=("date_","admin_","topic_"), height=2)
    
    #CREATE HEADING
    my_tree.heading("#0",text='',anchor=W)
    my_tree.heading("date_",text='วันที่',anchor=CENTER)
    my_tree.heading("admin_",text='เจ้าหน้าที่',anchor=CENTER)
    my_tree.heading("topic_",text='เรื่องที่แจ้ง',anchor=CENTER)
    my_tree.place(x=50,y=50,height=640,width=702)

    #FORMAT COLUMNS
    my_tree.column("#0",width=0,minwidth=25)
    my_tree.column("date",anchor=CENTER,width=150)
    my_tree.column("admin_",anchor=CENTER,width=150)
    my_tree.column("topic_",anchor=CENTER,width=400)

def retrivedata() :
    sql = "select * from user"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

#Program resolution
w = 1920
h = 1080

createconnection()
root = mainwindow()

#Spy's Job
userentry = StringVar()
passwordentry = StringVar()
name_addemp = StringVar()
lastname_addemp = StringVar()
username_addemp = StringVar()
password_addemp = StringVar()
phone_addemp = StringVar()

#Image import
img_riskilogo = PhotoImage(file='img/img_riskilogo.png')
img_phonenumber = PhotoImage(file='img/img_phonenumber.png')
img_riskilogos = PhotoImage(file='img/img_riskilogo.png').subsample(2,2)



#Button import
btn_printtotalamt = PhotoImage(file='button/btn_printtotalamt.png')
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
btn_datareport = PhotoImage(file='button/btn_datareport.png')
btn_doc = PhotoImage(file='button/btn_doc.png')
btn_income = PhotoImage(file='button/btn_income.png')
btn_pay = PhotoImage(file='button/btn_pay.png')
btn_totalamt = PhotoImage(file='button/btn_totalamt.png')
btn_information = PhotoImage(file='button/btn_information.png')
btn_find = PhotoImage(file='button/btn_find.png')
btn_printincome = PhotoImage(file='button/btn_printincome.png')
btn_invoices = PhotoImage(file='button/btn_invoices.png')
btn_paystat = PhotoImage(file='button/btn_paystat.png')
btn_printreceipt = PhotoImage(file='button/btn_printreceipt.png')


#Background
bg_login = PhotoImage(file = 'img/img_bglogin.png')
login_fn()
root.mainloop()