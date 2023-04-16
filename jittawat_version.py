from tkinter import*
import sqlite3
from tkinter import ttk 
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

#เวอร์ชั่นนี้เป็นเวอร์ชันทดลองเท่านั้น อาจจะมี ERROR ก็เป็นได้

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

def login_fn() :#เสร็จแล้ว #หน้า Login #By Haris
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
    frm_left_login_entry_password = Entry(frm_left_login, width=30, bg='#E6E6E6', bd=0,show="●", textvariable=passwordentry) #Spy
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

def home_fn() : #เสร็จแล้ว #หน้า Home #By Haris
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
    #Add some style
    style = ttk.Style()
    #Configure our treeview color
    style.configure("Treeview",background="#D9D9D9", foreground="black",rowheight=50, filebackground="silver" ,font=('Verdana', 12))
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
        
def checkinout_fn() : #เสร็จแล้ว #หน้า Main Check In/Out#โค้ดนี้กำลังแก้ไขโดย นัท 06/04/2023 เวลา 17:30
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

def checkin_fn() : #เสร็จแล้ว #หน้า Check In #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    global entry_phonenum_checkin, entry_name_checkin, entry_floor_checkin, entry_price_checkin, treecheckin, entry_roomtype_checkin
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
    Label(frm_right_checkin, text='CHECK IN', bg='white', font = 'Calibri 55 bold', fg='#376957').place(x=500, y=70)
    frm_right_checkin_bg = Frame(frm_right_checkin, bg='#DDDDDD')
    frm_right_checkin_bg.place(x=276, y=160, width=750, height=520)
    Label(frm_right_checkin_bg, text='เบอร์โทรศัพท์ : ', bg='#DDDDDD').place(x=180, y=60)
    entry_phonenum_checkin = Entry(frm_right_checkin_bg, textvariable=phone_checkin) #Spy
    entry_phonenum_checkin.place(x=350, y=60)
    Button(frm_right_checkin_bg, image=btn_search, bd=0, bg='#DDDDDD', command=checkin_search_backend).place(x=670, y=58) 
    Label(frm_right_checkin_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_checkin = Entry(frm_right_checkin_bg, textvariable=name_checkin, state='readonly') #Spy
    entry_name_checkin.place(x=350, y=120)
    Label(frm_right_checkin_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=210, y=180)
    entry_number_checkin = Entry(frm_right_checkin_bg, textvariable=number_checkin, state='readonly') #Spy
    entry_number_checkin.place(x=350, y=180)
    Label(frm_right_checkin_bg, text='ชั้น : ', bg='#DDDDDD').place(x=240, y= 240)
    entry_floor_checkin = Entry(frm_right_checkin_bg, textvariable=floor_checkin, state='readonly') #Spy
    entry_floor_checkin.place(x=350, y=240)
    Label(frm_right_checkin_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=180, y= 300)
    entry_roomtype_checkin = Entry(frm_right_checkin_bg, textvariable=roomtype_checkin, state='readonly') #Spy
    entry_roomtype_checkin.place(x=350, y=300)
    Label(frm_right_checkin_bg, text='ราคา : ', bg='#DDDDDD').place(x=230, y= 360)
    entry_price_checkin = Entry(frm_right_checkin_bg, textvariable=price_checkin, state='readonly') #Spy
    entry_price_checkin.place(x=350, y=360)
    Button(frm_right_checkin_bg, image=btn_next,bd=0, bg='#DDDDDD', command=checkin_date).place(x=480, y=450)
    
    #Create Treeview
    treecheckin = ttk.Treeview(root)
    treecheckin= ttk.Treeview(frm_right_checkin, columns=("floor_", "roomnum_", "roomtype_", "roomrate_"), height=2)
    #create headings
    treecheckin.heading('#0', text='') #default
    treecheckin.heading('floor_', text="ชั้น", anchor=CENTER)
    treecheckin.heading('roomnum_', text="เลขห้อง", anchor=CENTER)
    treecheckin.heading('roomtype_', text="ประเภทห้อง", anchor=CENTER)
    treecheckin.heading('roomrate_', text="ราคา", anchor=CENTER)
    #format columns
    treecheckin.column("#0", width=0, minwidth=0)
    treecheckin.column('floor_', anchor=CENTER, width=150)
    treecheckin.column('roomnum_', anchor=CENTER, width=150)
    treecheckin.column('roomtype_', anchor=CENTER, width=150)
    treecheckin.column('roomrate_', anchor=CENTER, width=150)
    treecheckin.place(x=100, y=700, width=1052, height=250)
    #Connect Database room table
    db_room = conn.execute('SELECT * FROM room')
    #Insert Data to tree
    for i in db_room :
        if i[5] == "ว่าง" :
            treecheckin.insert("", 'end', values=(i[1], i[0], i[2], i[3]))
    #Tree bind
    treecheckin.bind("<Double-1>", checkin_insert_backend)

def checkin_insert_backend(event) : #เสร็จแล้ว โดย Haris
    db_room = conn.execute('SELECT * FROM room')
    for i in db_room :
        i = treecheckin.item(treecheckin.focus(), "values")
        number_checkin.set(i[1])
        floor_checkin.set(i[0])
        roomtype_checkin.set(i[2])
        price_checkin.set(i[3])

def checkin_search_backend() : #เสร็จแล้ว โดย Haris
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_checkin.get()])
    db_customer = cursor.fetchone()

    if db_customer is None or phone_checkin.get() != db_customer[0] :
        messagebox.showwarning('Riski Apartment : Warning', 'ไม่พบลูกค้า')
        entry_phonenum_checkin.delete(0, END)
    else : 
        name_checkin.set(db_customer[2] + ' ' + db_customer[3])

def checkin_date() : #เสร็จแล้ว โดย Haris #หน้า Check In ที่ 2 #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    name_user = db_user[3] + " " + db_user[4]
    global calendar1, calendar2, entry_user_in, btn_logic
    btn_logic = 'F'
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
    calendar1 = DateEntry(frm_right_checkindate_bg, selectmode='day', date_pattern='dd/mm/yyyy')
    calendar1.place(x=250, y=60)
    Label(frm_right_checkindate_bg, text='สิ้นสุดวันที่ : ', bg='#DDDDDD').place(x=109, y=120)
    calendar2 = DateEntry(frm_right_checkindate_bg, selectmode='day', date_pattern='dd/mm/yyyy')
    calendar2.place(x=250, y=120)
    Label(frm_right_checkindate_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD').place(x=121, y=180)
    entry_user_in = Entry(frm_right_checkindate_bg,textvariable=employee_checkindate) #Spy
    entry_user_in.place(x=250, y=180)
    employee_checkindate.set(name_user)
    Button(frm_right_checkindate_bg, image=btn_save,bd=0, bg='#DDDDDD', command=get_date).place(x=150, y=250)
    Button(frm_right_checkindate_bg, image=btn_finish,bd=0, bg='#DDDDDD', command=checkindate_backend).place(x=450, y=250)
    Button(frm_right_checkindate_bg, image=btn_paperform,bd=0, bg='#DDDDDD').place(x=280, y=360)

def get_date() : #เสร็จแล้ว โดย Haris
    global btn_logic
    btn_logic = 'T'
    date = calendar1.get_date()
    date_string1 = date.strftime("%d/%m/%Y")
    date = calendar2.get_date()
    date_string2 = date.strftime("%d/%m/%Y")   
    return date_string1, date_string2

def checkindate_backend() : #เสร็จแล้ว โดย Haris
    if btn_logic == "T" :
        date1, date2 = get_date()
        #Fetch customer
        sql = 'SELECT * FROM customer WHERE phonenumber=?'
        cursor.execute(sql, [phone_checkin.get()])
        db_customer = cursor.fetchone()
        status = "ไม่ว่าง"
        electric_bill = 0
        water_bill = 0
        electric_meter = 0
        water_meter = 0
        payment_status = '-'
        room_bill = 0
        #Update customer
        sql = '''
                UPDATE customer
                SET room=?
                WHERE phonenumber=?
        '''
        cursor.execute(sql, [number_checkin.get(), db_customer[0]])
        conn.commit()
        #Update room
        sql = '''
                UPDATE room
                SET customer_name=?, check_in_date=?, status=?, check_out_date=?
                WHERE room_number=?
        '''    
        cursor.execute(sql, [db_customer[2] + " " + db_customer[3], date1, status, date2,number_checkin.get()])
        conn.commit()
        checkin_date()
        messagebox.showinfo("Riski Apartment : Success", "เช็คอินลูกค้า %s เรียบร้อย"%(db_customer[2]))
        #Fetch room
        sql = '''SELECT * FROM room WHERE room_number=?'''
        cursor.execute(sql, [number_checkin.get()])
        db_room = cursor.fetchone()

        #Insert data to service_log
        sql = '''INSERT INTO service_log (phonenumber, date, roomnumber, name, roomtype, floor, electric_bill, water_bill, electric_meter, water_meter, payment_status, room_bill)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(sql, [db_customer[0], date1, db_room[0], db_customer[2] + " " + db_customer[3], db_room[2], db_room[1], electric_bill, water_bill, electric_meter, water_meter, payment_status, room_bill])
        conn.commit()
        name_checkin.set("")
        roomtype_checkin.set("")
        number_checkin.set("")
        floor_checkin.set("")
        price_checkin.set("")

    else :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณาบันทึกก่อน")

def checkout_fn() : #เสร็จแล้ว #หน้า Check Out #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    global checkout_logic
    checkout_logic = "F"
    global entry_phonenum_checkout, entry_name_checkout,  entry_roomnum_checkout, entry_floor_checkout, entry_roomtype_checkout
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
    entry_phonenum_checkout = Entry(frm_right_checkout_bg, textvariable=phone_checkout) #Spy
    entry_phonenum_checkout.place(x=350, y=60)
    Button(frm_right_checkout_bg, image=btn_search, bd=0, bg='#DDDDDD', command=checkout_search_backend).place(x=670, y=58)       #from database
    Label(frm_right_checkout_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_checkout = Entry(frm_right_checkout_bg, textvariable=name_checkout, state='readonly') #Spy
    entry_name_checkout.place(x=350, y=120)             #from database
    Label(frm_right_checkout_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=232, y=180)
    entry_roomnum_checkout = Entry(frm_right_checkout_bg, textvariable=number_checkout, state='readonly') #Spy
    entry_roomnum_checkout.place(x=350, y=180)
    #room type
    Label(frm_right_checkout_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=200, y= 240)
    entry_roomtype_checkout = Entry(frm_right_checkout_bg, textvariable=roomtype_checkout, state='readonly') #Spy
    entry_roomtype_checkout.place(x=350, y=240)
    Label(frm_right_checkout_bg, text='ชั้น : ', bg='#DDDDDD').place(x=275, y= 300)
    entry_floor_checkout = Entry(frm_right_checkout_bg, textvariable=floor_checkout, state='readonly') #Spy
    entry_floor_checkout.place(x=350, y=300)
    Button(frm_right_checkout_bg, image=btn_confirm,bd=0, bg='#DDDDDD', command=checkout_date).place(x=480, y=450)   #ไม่แน่ใจว่ากดยืนยันแล้วจะไปหน้าเลือกวันที่มั้ยแต่ผูกไว้ก่อนนะ

def checkout_date() :#เสร็จแล้ว #หน้า Check Out ที่ 2 #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 3:09
    global checkout_logic
    #date1, date2 = get_date()
    name_user = db_user[3] + " " + db_user[4]
    if checkout_logic == 'T' :
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
        entry_startdate_out = Entry(frm_right_checkoutdate_bg, textvariable=startdate_checkoutdate, state='readonly') #Spy
        entry_startdate_out.place(x=250, y=60)
        Label(frm_right_checkoutdate_bg, text='สิ้นสุดวันที่ : ', bg='#DDDDDD').place(x=109, y=120)
        entry_endate_out = Entry(frm_right_checkoutdate_bg, textvariable=enddate_checkoutdate, state='readonly') #Spy
        entry_endate_out.place(x=250, y=120)
        Label(frm_right_checkoutdate_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD').place(x=121, y=180)
        entry_user_out = Entry(frm_right_checkoutdate_bg, textvariable=user_checkoutdate, state='readonly') #Spy
        entry_user_out.place(x=250, y=180)
        user_checkoutdate.set(name_user)
        Button(frm_right_checkoutdate_bg, image=btn_back,bd=0, bg='#DDDDDD', command=checkout_fn).place(x=150, y=250)
        Button(frm_right_checkoutdate_bg, image=btn_finish,bd=0, bg='#DDDDDD', command=checkoutdate_backend).place(x=450, y=250)
        #Fetching data to insert date
        sql = 'SELECT * FROM customer WHERE phonenumber=?'
        cursor.execute(sql, [phone_checkout.get()])
        db_customer = cursor.fetchone()

        sql = 'SELECT * FROM room WHERE room_number=?'
        cursor.execute(sql, [db_customer[1]])
        db_room = cursor.fetchone()

        startdate_checkoutdate.set(db_room[9])
        enddate_checkoutdate.set(db_room[10])
    else :
        messagebox.showwarning('Riski Apartment : Warning', 'กรุณากรอกเบอร์ลูกค้า')

def checkout_search_backend() : #เสร็จแล้ว โดย Haris
    global checkout_logic
    checkout_logic = "T"
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_checkout.get()])
    db_customer = cursor.fetchone()

    if db_customer is None or phone_checkout.get() != db_customer[0] :
        messagebox.showwarning('Riski Apartment : Warning', 'ไม่พบลูกค้า')
    else :
        name_checkout.set(db_customer[2] + ' ' + db_customer[3])
    if db_customer[1] == '-' :
        messagebox.showwarning('Riski Apartment : Warning', 'ลูกค้ายังไม่ได้ Check In')
        entry_phonenum_checkout.delete(0, END)
        entry_name_checkout.delete(0, END)
    else : 
        number_checkout.set(db_customer[1])
        sql = 'SELECT * FROM room WHERE room_number=?'
        cursor.execute(sql, [db_customer[1]])
        db_room = cursor.fetchone()
        roomtype_checkout.set(db_room[2])
        floor_checkout.set(db_room[1])

def checkoutdate_insert_backend() : #เสร็จแล้ว โดย Haris
    date1, date2 = get_date()
    startdate_checkoutdate.set(date1)
    enddate_checkoutdate.set(date2)

def checkoutdate_backend() : #เสร็จแล้ว โดย Haris
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_checkout.get()])
    db_customer = cursor.fetchone()
    status = "ว่าง"
    room = '-'
    sql = '''
            UPDATE room
            SET customer_name=?, check_in_date=?, status=?, check_out_date=?
            WHERE room_number=?
    '''
    cursor.execute(sql, ["", "", status, "", db_customer[1]])
    conn.commit()
    sql = '''
            UPDATE customer
            SET room=?
            WHERE phonenumber=?
    '''
    cursor.execute(sql, [room, db_customer[0]])
    conn.commit()
    sql = '''DELETE FROM service_log WHERE phonenumber=?'''
    cursor.execute(sql, [db_customer[0]])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "เช็คเอาท์ลูกค้า %s เรียบร้อย"%(db_customer[2]))
    entry_phonenum_checkout.delete(0, END)
    name_checkout.set("")
    number_checkout.set("")
    roomtype_checkout.set("")
    floor_checkout.set("")
    checkout_fn()

def accountmanage_fn() : #เสร็จแล้ว #หน้า Main จัดการบัญชี #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
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

def addempaccount_fn() : #เสร็จแล้ว #หน้าเพิ่มบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
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
    Label(frm_right_addempaccount_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=603, y=50)
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

def addempaccount_backend() : #เสร็จแล้ว โดย Haris
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
        cursor.execute(sql, [phone_addemp.get(), username_addemp.get().lower(), password_addemp.get().lower(), name_addemp.get(), lastname_addemp.get(), status])
        conn.commit()
        retrivedata()
        messagebox.showinfo("Cryptonite : Successfully", "เพิ่มข้อมูลพนักงานเสร็จสิ้น")
        entry_name_addempaccount.delete(0, END)
        entry_surname_addempaccount.delete (0, END)
        entry_username_addempaccount.delete(0, END)
        entry_password_addempaccount.delete(0, END)
        entry_phone_addempaccount.delete(0, END)
    addempaccount_fn()
    
def editempaccount_fn() : #เสร็จแล้ว #หน้าแก้ไขบัญชีพนักงาน #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    global entry_findphone_editempaccount, entry_name_editempaccount, entry_surname_editempaccount, entry_username_editempaccount, entry_password_editempaccount, entry_phone_editempaccount
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
    entry_findphone_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=findphone_editempaccount) #Spy
    entry_findphone_editempaccount.place(x=500, y=50, width=250)
    Button(frm_right_editempaccount_bg, image=btn_search, bd=0, bg='#DDDDDD', command=editempaccount_search_backend).place(x=780, y=50)
    Label(frm_right_editempaccount_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=200, y=100)
    entry_name_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=name_editempaccount) #Spy
    entry_name_editempaccount.place(x=270, y=100, width=230)
    Label(frm_right_editempaccount_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=603, y=100)
    entry_surname_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=lastname_editempaccount) #Spy
    entry_surname_editempaccount.place(x=730, y=100, width=230)
    Label(frm_right_editempaccount_bg, text='Username : ', bg='#DDDDDD').place(x=111, y=150)
    entry_username_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=username_editempaccount) #Spy
    entry_username_editempaccount.place(x=270, y=150, width=230)
    Label(frm_right_editempaccount_bg, text='Password : ', bg='#DDDDDD').place(x=570, y=150)
    entry_password_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=password_editempaccount) #Spy
    entry_password_editempaccount.place(x=730, y=150, width=230)
    Label(frm_right_editempaccount_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=152, y=200)
    entry_phone_editempaccount = Entry(frm_right_editempaccount_bg, textvariable=phone_editempaccount) #Spy
    entry_phone_editempaccount.place(x=270, y=200, width=230)
    Button(frm_right_editempaccount_bg, image=btn_delete, bd=0, bg='#DDDDDD', command=editempaccount_delete_backend).place(x=580, y=240)
    Button(frm_right_editempaccount_bg, image=btn_edit, bd=0, bg='#DDDDDD', command=editempaccount_edit_backend).place(x=790, y=240)

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

def editempaccount_search_backend() : #เสร็จแล้ว โดย Haris
    sql = 'SELECT * FROM user WHERE phonenumber=?'
    cursor.execute(sql, [findphone_editempaccount.get()])
    db_emp = cursor.fetchone() 
    if db_emp is None or findphone_editempaccount.get() != db_emp[0]:
        messagebox.showwarning("Riski Apartment : Warning", "ไม่พบเบอร์โทรศัพท์ %s" %(findphone_editempaccount.get()))
        entry_phone_editempaccount.delete(0, END)
        entry_phone_editempaccount.focus_force
    else :
        phone_editempaccount.set(db_emp[0])
        username_editempaccount.set(db_emp[1])
        password_editempaccount.set(db_emp[2])
        name_editempaccount.set(db_emp[3])
        lastname_editempaccount.set(db_emp[4])

def editempaccount_edit_backend() : #เสร็จแล้ว โดย Haris
    sql = '''
            UPDATE user
            SET phonenumber=?, username=?, password=?, name=?, lastname=?, status=?
            WHERE phonenumber=?   
    '''
    cursor.execute(sql, [phone_editempaccount.get(), username_editempaccount.get(), password_editempaccount.get(), name_editempaccount.get(), lastname_editempaccount.get(), db_user[5], findphone_editempaccount.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "แก้ไขข้อมูลของเรียบร้อย")
    entry_name_editempaccount.delete(0, END)
    entry_surname_editempaccount.delete(0, END)
    entry_username_editempaccount.delete(0, END)
    entry_password_editempaccount.delete(0, END)
    entry_findphone_editempaccount.delete(0, END)
    entry_phone_editempaccount.delete(0, END)
    editempaccount_fn()

def editempaccount_delete_backend() : #เสร็จแล้ว โดย Haris
    delete_confirm = messagebox.askquestion("Riski Apartment : ยืนยันการลบ", "คุณแน่ใจหรือไม่ว่าจะลบ %s ออกจากพนักงาน" %(name_editempaccount.get()))
    if delete_confirm == 'yes' :
        sql = '''
                DELETE FROM user WHERE phonenumber=?
        '''
        cursor.execute(sql,[phone_editempaccount.get()])
        conn.commit()
        messagebox.showinfo("Riski Apartment : Success", "ลบ %s ออกเรียบร้อย" %(name_editempaccount.get()))
        entry_name_editempaccount.delete(0, END)
        entry_surname_editempaccount.delete(0, END)
        entry_username_editempaccount.delete(0, END)
        entry_password_editempaccount.delete(0, END)
        entry_phone_editempaccount.delete(0, END)
        entry_findphone_editempaccount.delete(0, END)
        entry_findphone_editempaccount.focus_force()
    editempaccount_fn()

def addcustomerinfo_fn() : #เสร็จแล้ว #หน้าเพิ่มข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 2:30
    global entry_name_addcusinfo, entry_surname_addcusinfo, entry_phone_addcusinfo, entry_ethnicity_addcusinfo, entry_nation_addcusinfo, entry_number_addcusinfo, entry_village_addcusinfo, entry_road_addcusinfo, entry_subdistrict_addcusinfo, entry_district_addcusinfo, entry_province_addcusinfo
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
    Label(frm_right_addcusinfo_bg, text='ชื่อ : ', bg='#DDDDDD').place(x=110, y=50) #ตัวแปรเปลี่ยนชื่อได้ตามdatabaseที่ออกแบบไว้ได้เลยนะอันนี้เขียนไว้ก่อนเฉยๆ
    entry_name_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=name_addcus)
    entry_name_addcusinfo.place(x=170, y=50)
    Label(frm_right_addcusinfo_bg, text='นามสกุล : ', bg='#DDDDDD').place(x=59, y=150)
    entry_surname_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=lastname_addcus)
    entry_surname_addcusinfo.place(x=170, y=150)
    Label(frm_right_addcusinfo_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=61, y=250)
    entry_phone_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=phone_addcus)
    entry_phone_addcusinfo.place(x=170, y=250)
    Label(frm_right_addcusinfo_bg, text='เชื้อชาติ : ', bg='#DDDDDD').place(x=65, y=350)
    entry_ethnicity_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=ethinicity_addcus) #ศัพท์จาก apple translate
    entry_ethnicity_addcusinfo.place(x=170, y=350)
    Label(frm_right_addcusinfo_bg, text='สัญชาติ : ', bg='#DDDDDD').place(x=67, y=450)
    entry_nation_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=nation_addcus) #nation --> nationality
    entry_nation_addcusinfo.place(x=170, y=450)
    Label(frm_right_addcusinfo_bg, text='บ้านเลขที่ : ', bg='#DDDDDD').place(x=600, y=50)
    entry_number_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=number_addcus) #บ้านเลขที่ --> number , จะเปลี่ยนก็ได้ตามใจชอบบ
    entry_number_addcusinfo.place(x=720, y=50)
    Label(frm_right_addcusinfo_bg, text='หมู่บ้าน : ', bg='#DDDDDD').place(x=621, y=150)
    entry_village_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=village_addcus)
    entry_village_addcusinfo.place(x=720, y=150)
    Label(frm_right_addcusinfo_bg, text='ถนน : ', bg='#DDDDDD').place(x=645, y=250)
    entry_road_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=road_addcus)
    entry_road_addcusinfo.place(x=720, y=250)
    Label(frm_right_addcusinfo_bg, text='ตำบล/แขวง : ', bg='#DDDDDD').place(x=578, y=350)
    entry_subdistrict_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=subdistrict_addcus)
    entry_subdistrict_addcusinfo.place(x=720, y=350)
    Label(frm_right_addcusinfo_bg, text='อำเภอ/เขต : ', bg='#DDDDDD').place(x=588, y=450)
    entry_district_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=district_addcus)
    entry_district_addcusinfo.place(x=720, y=450)
    Label(frm_right_addcusinfo_bg, text='จังหวัด : ', bg='#DDDDDD').place(x=632, y=550)
    entry_province_addcusinfo = Entry(frm_right_addcusinfo_bg, textvariable=province_addcus)
    entry_province_addcusinfo.place(x=720, y=550) 
    Button(frm_right_addcusinfo_bg, image=btn_longsave, bd=0, bg='#DDDDDD', command=addcustomerinfo_backend).place(x=760, y=650)

def addcustomerinfo_backend() : #เสร็จแล้ว โดย Haris
    sql = "SELECT * FROM customer WHERE phonenumber=?"
    cursor.execute(sql, [phone_addemp.get()])
    db_phonecheck = cursor.fetchone()
    room = "-"

    status = "U"
    #Existence Check
    if name_addcus.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกชื่อ")
        entry_name_addcusinfo.focus_force()
    elif lastname_addcus.get() == '' :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกนามสกุล")
        entry_surname_addcusinfo.focus_force()
    elif phone_addcus.get().isnumeric == False :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเบอร์โทรศัพท์เป็นตัวเลข")
        entry_phone_addcusinfo.focus_force()   
    elif len(phone_addcus.get()) != 10 :
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเบอร์โทรศัพท์ให้ครบ 10 ตัว")
    elif db_phonecheck is not None and phone_addcus.get() == db_phonecheck[0]:
        messagebox.showerror("Riski Apartment : Error", "เบอร์โทรศัพท์นี้ถูกใช้ไปแล้ว")
        entry_phone_addcusinfo.focus_force() 
    else :
        sql = '''INSERT INTO customer (phonenumber, room, name, lastname, house_number, village, road, district, amphoe, province, ethnicity, nationality) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
        cursor.execute(sql, [phone_addcus.get(), room, name_addcus.get(), lastname_addcus.get(), number_addcus.get(), village_addcus.get(), road_addcus.get(), subdistrict_addcus.get(), district_addcus.get(), province_addcus.get(), ethinicity_addcus.get(), nation_addcus.get()])
        conn.commit()
        # retrivedata()
        messagebox.showinfo("Cryptonite : Successfully", "เพิ่มข้อมูลลูกค้าเสร็จสิ้น")
        entry_name_addcusinfo.delete(0, END)
        entry_surname_addcusinfo.delete (0, END)
        entry_phone_addcusinfo.delete (0, END)
        entry_nation_addcusinfo.delete (0, END)
        entry_ethnicity_addcusinfo.delete (0, END)
        entry_number_addcusinfo.delete (0, END)
        entry_village_addcusinfo.delete (0, END)
        entry_road_addcusinfo.delete (0, END)
        entry_subdistrict_addcusinfo.delete (0, END)
        entry_district_addcusinfo.delete (0, END)
        entry_province_addcusinfo.delete (0, END)
    addcustomerinfo_fn()

def searchcusinfo_fn() :  #เสร็จแล้ว # search หน้าแก้ไขข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05 
    global entry_phone_searchcusinfo, entry_name_searchcusinfo
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
    entry_phone_searchcusinfo = Entry(frm_right_searchcusinfo_bg, textvariable=phone_searchcusinfo) #Spy
    entry_phone_searchcusinfo.place(x=300, y=70)
    Button(frm_right_searchcusinfo_bg, image=btn_search, bd=0, bg='#DDDDDD', command=searchcusinfo_search_backend).place(x=620, y=68)
    Label(frm_right_searchcusinfo_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD', bd=0).place(x=154, y=140) #Info from database
    entry_name_searchcusinfo = Entry(frm_right_searchcusinfo_bg, textvariable=name_searchcusinfo) #Spy
    entry_name_searchcusinfo.place(x=300, y=140)
    Button(frm_right_searchcusinfo_bg, image=btn_deleteinfo, bd=0, bg='#DDDDDD', command=editcusinfo_delete_backend).place(x=200, y=270)
    Button(frm_right_searchcusinfo_bg, image=btn_edit, bd=0, bg='#DDDDDD', command=editcusinfo_fn).place(x=430, y=270)

def searchcusinfo_search_backend() : #เสร็จแล้ว โดย Haris
    global searchphone, name_searchcusinfo
    searchphone = phone_searchcusinfo.get()
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_searchcusinfo.get()])
    db_customer = cursor.fetchone()

    if db_customer is None or phone_searchcusinfo.get() != db_customer[0] :
        messagebox.showwarning('Riski Apartment : Warning', 'ไม่พบลูกค้า')
        entry_phone_searchcusinfo.delete(0, END)
        entry_name_searchcusinfo.delete(0, END)
    else :
        name_searchcusinfo.set(db_customer[2] + " " + db_customer[3])

def editcusinfo_fn() : #เสร็จแล้ว # หน้าแก้ไขข้อมูลลูกค้า #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    global entry_name_editcusinfo, entry_surname_editcusinfo, entry_phone_editcusinfo, entry_ethnicity_editcusinfo, entry_nation_editcusinfo, entry_number_editcusinfo, entry_village_editcusinfo,  entry_road_editcusinfo, entry_subdistrict_editcusinfo, entry_district_editcusinfo, entry_province_editcusinfo
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
    entry_name_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=name_editcusinfo) #Spy
    entry_name_editcusinfo.place(x=170, y=50)
    Label(frm_right_editcusinfo_bg, text='นามสกุล : ', bg='#DDDDDD', bd=0).place(x=59, y=150)
    entry_surname_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=lastname_editcusinfo) #Spy
    entry_surname_editcusinfo.place(x=170, y=150)
    Label(frm_right_editcusinfo_bg, text='เบอร์โทร : ', bg='#DDDDDD').place(x=61, y=250)
    entry_phone_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=phone_editcusinfo) #Spy
    entry_phone_editcusinfo.place(x=170, y=250)
    Label(frm_right_editcusinfo_bg, text='เชื้อชาติ : ', bg='#DDDDDD').place(x=65, y=350)
    entry_ethnicity_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=ethinicity_editcusinfo) #Spy
    entry_ethnicity_editcusinfo.place(x=170, y=350)
    Label(frm_right_editcusinfo_bg, text='สัญชาติ : ', bg='#DDDDDD').place(x=67, y=450)
    entry_nation_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=nation_editcusinfo) #Spy
    entry_nation_editcusinfo.place(x=170, y=450)
    Label(frm_right_editcusinfo_bg, text='บ้านเลขที่ : ', bg='#DDDDDD').place(x=600, y=50)
    entry_number_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=number_editcusinfo) #Spy
    entry_number_editcusinfo.place(x=720, y=50)
    Label(frm_right_editcusinfo_bg, text='หมู่บ้าน : ', bg='#DDDDDD').place(x=621, y=150)
    entry_village_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=village_editcusinfo) #Spy
    entry_village_editcusinfo.place(x=720, y=150)
    Label(frm_right_editcusinfo_bg, text='ถนน : ', bg='#DDDDDD').place(x=645, y=250)
    entry_road_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=road_editcusinfo) #Spy
    entry_road_editcusinfo.place(x=720, y=250)
    Label(frm_right_editcusinfo_bg, text='ตำบล/แขวง : ', bg='#DDDDDD').place(x=578, y=350)
    entry_subdistrict_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=subdistrict_editcusinfo) #Spy
    entry_subdistrict_editcusinfo.place(x=720, y=350)
    Label(frm_right_editcusinfo_bg, text='อำเภอ/เขต : ', bg='#DDDDDD').place(x=588, y=450)
    entry_district_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=district_editcusinfo) #Spy
    entry_district_editcusinfo.place(x=720, y=450)
    Label(frm_right_editcusinfo_bg, text='จังหวัด : ', bg='#DDDDDD').place(x=632, y=550)
    entry_province_editcusinfo = Entry(frm_right_editcusinfo_bg, textvariable=province_editcusinfo) #Spy
    entry_province_editcusinfo.place(x=720, y=550)
    Button(frm_right_editcusinfo_bg, image=btn_longsave, bd=0, bg='#DDDDDD', command=editcusinfo_edit_backend).place(x=760, y=650)

    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [searchphone])
    db_customer = cursor.fetchone()

    #editcustomerinfo
    name_editcusinfo.set(db_customer[2])
    lastname_editcusinfo.set(db_customer[3])
    phone_editcusinfo.set(db_customer[0])
    ethinicity_editcusinfo.set(db_customer[10])
    nation_editcusinfo.set(db_customer[11])
    number_editcusinfo.set(db_customer[4])
    village_editcusinfo.set(db_customer[5])
    road_editcusinfo.set(db_customer[6])
    subdistrict_editcusinfo.set(db_customer[7])
    district_editcusinfo.set(db_customer[8])
    province_editcusinfo.set(db_customer[9])

def editcusinfo_edit_backend() : #เสร็จแล้ว โดย Haris #แก้เพิ่มห้อง
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [searchphone])
    db_customer = cursor.fetchone()
    room = db_customer[1]
    sql = '''
            UPDATE customer
            SET phonenumber=?, room=?, name=?, lastname=?, house_number=?, village=?,
            road=?, district=?, amphoe=?, province=?, ethnicity=?, nationality=?
            WHERE phonenumber=?   
    '''
    cursor.execute(sql, [phone_editcusinfo.get(), room, name_editcusinfo.get(), lastname_editcusinfo.get(), number_editcusinfo.get(), village_editcusinfo.get(), road_editcusinfo.get(), subdistrict_editcusinfo.get(), district_editcusinfo.get(), province_editcusinfo.get(), ethinicity_editcusinfo.get(), nation_editcusinfo.get(),phone_searchcusinfo.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "แก้ไขข้อมูลของเรียบร้อย")
    entry_name_editcusinfo.delete(0, END)
    entry_surname_editcusinfo.delete(0, END)
    entry_phone_editcusinfo.delete(0, END)
    entry_nation_editcusinfo.delete(0, END)
    entry_ethnicity_editcusinfo.delete(0, END)
    entry_number_editcusinfo.delete(0, END)
    entry_village_editcusinfo.delete(0, END)
    entry_road_editcusinfo.delete(0, END)
    entry_subdistrict_editcusinfo.delete(0, END)
    entry_district_editcusinfo.delete(0, END)
    entry_province_editcusinfo.delete(0, END)
    editcusinfo_fn()

def editcusinfo_delete_backend() : #เสร็จแล้ว
    delete_confirm = messagebox.askquestion("Riski Apartment : ยืนยันการลบ", "คุณแน่ใจหรือไม่ว่าจะลบลูกค้า")
    if delete_confirm == 'yes' :
        sql = '''
                DELETE FROM customer WHERE phonenumber=?
        '''
        cursor.execute(sql,[phone_searchcusinfo.get()])
        conn.commit()
        messagebox.showinfo("Riski Apartment : Success", "ลบลูกค้าออกเรียบร้อย")
        entry_phone_searchcusinfo.delete(0, END)
        entry_name_searchcusinfo.delete(0, END)
        entry_phone_searchcusinfo.focus_force()   
    searchcusinfo_fn()

def roommanage_fn(): #เสร็จแล้ว โดย Haris #RoomManagement(Admin) เช็คห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
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

def addRoom_fn(): #เสร็จแล้ว #เพิ่มห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
    global entry_roomnumber_addRoom, entry_floor_addRoom
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
    entry_roomnumber_addRoom = Entry(frm_right_addRoom_bg, textvariable=roomnumber_addroom) #Spy
    entry_roomnumber_addRoom.place(x=350, y=60)
    Label(frm_right_addRoom_bg, text='ชั้น : ', bg='#DDDDDD').place(x=272, y=120)
    entry_floor_addRoom = Entry(frm_right_addRoom_bg, textvariable=floor_addroom) #Spy
    entry_floor_addRoom.place(x=350, y=120)
    Label(frm_right_addRoom_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=198, y=180)
    #room type
    room_type = ["รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_addRoom_bg, roomtype_addroom, *room_type).place(x=350, y=180, width=310) #Spy
    roomtype_addroom.set('ประเภทห้อง')
    Button(frm_right_addRoom_bg, image=btn_add,bd=0, bg='#DDDDDD', command=addRoom_backend).place(x=485, y=270)

def addRoom_backend() : #เสร็จแล้ว เนื่องจากต้องมีค่าห้องพักที่ต้องเชื่อมกับฟังชันการกำหนดราคาห้องพัก
    roomtype_price = 0
    unit = 0
    room_execute = conn.execute('SELECT * FROM room')
    for db_room in room_execute :
        if db_room[2] == roomtype_addroom.get() :
            roomtype_price = db_room[3]
            unit = db_room[4]
            break  # exit the loop once a matching room type is found

    sql = "SELECT * FROM room WHERE room_number=?"
    cursor.execute(sql, [roomnumber_addroom.get()])
    db_roomnumbercheck = cursor.fetchone()
    room_status = "ว่าง"

    #Existence Check
    if roomnumber_addroom.get() == '':
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเลขห้อง")
        entry_roomnumber_addRoom.focus_force()
    elif not roomnumber_addroom.get().isnumeric():
        messagebox.showwarning("Riski Apartment : Warning", "กรุณากรอกเลขห้องเป็นตัวเลข")
        entry_roomnumber_addRoom.focus_force()
    else:
        sql = "SELECT * FROM room WHERE room_number=?"
        cursor.execute(sql, [roomnumber_addroom.get()])
        db_roomnumbercheck = cursor.fetchone()
        if db_roomnumbercheck:
            messagebox.showwarning("Riski Apartment : Warning", "หมายเลขห้องนี้ถูกใช้ไปแล้ว")
            entry_roomnumber_addRoom.delete(0, END)
            entry_floor_addRoom.delete(0, END)
            roomtype_addroom.set('ประเภทห้อง')
            entry_roomnumber_addRoom.focus_force()
        else:
            room_status = "ว่าง"
            sql = '''INSERT INTO room (room_number, floor, room_type, price, unit, status) VALUES (?,?,?,?,?,?)'''
            cursor.execute(sql, [roomnumber_addroom.get(), floor_addroom.get(), roomtype_addroom.get(), roomtype_price, unit, room_status])
            conn.commit()
            retrivedata()
            messagebox.showinfo("Cryptonite : Successfully", "เพิ่มข้อมูลห้องพักเสร็จสิ้น")
            entry_roomnumber_addRoom.delete(0, END)
            entry_floor_addRoom.delete(0, END)
            roomtype_addroom.set('ประเภทห้อง')
        
    addRoom_fn()

def editRoom_fn(): #เสร็จแล้ว โดย Haris #แก้ไขห้องพัก #โค้ดนี้กำลังแก้ไขโดย บูม 07/04/2023 เวลา 18:05
    global entry_roomnumber_editRoom, entry_floor_editRoom
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
    entry_roomnumber_editRoom = Entry(frm_right_editRoom_bg, textvariable=roomnumber_editroom) #Spy
    entry_roomnumber_editRoom.place(x=350, y=60)
    Button(frm_right_editRoom_bg, image=btn_search, bd=0, bg='#DDDDDD', command=editRoom_search_backend).place(x=660, y=60)
    Label(frm_right_editRoom_bg, text='ชั้น : ', bg='#DDDDDD').place(x=272, y=120)
    entry_floor_editRoom = Entry(frm_right_editRoom_bg, textvariable=floor_editroom) #Spy
    entry_floor_editRoom.place(x=350, y=120)
    Label(frm_right_editRoom_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=198, y=180)
    #room type
    room_type = ["รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_editRoom_bg, roomtype_editroom, *room_type).place(x=350, y=180, width=310) #Spy
    roomtype_editroom.set('ประเภทห้อง')
    #room state
    Label(frm_right_editRoom_bg, text='สถานะห้อง : ', bg='#DDDDDD').place(x=198, y=250)
    room_status = ["ว่าง", "ไม่ว่าง", "ปรับปรุง"]
    roomstatus = OptionMenu(frm_right_editRoom_bg, roomstatus_editroom, *room_status).place(x=350, y=250, width=310) #Spy
    roomstatus_editroom.set('สถานะห้อง')
    Button(frm_right_editRoom_bg, image=btn_delete, bd=0, bg='#DDDDDD', command=editRoom_delete_backend).place(x=250, y=350)
    Button(frm_right_editRoom_bg, image=btn_edit,bd=0, bg='#DDDDDD', command=editRoom_edit_backend).place(x=485, y=350)

def editRoom_search_backend() : #เสร็จแล้ว โดย Haris
    sql = "SELECT * FROM room WHERE room_number=?"
    cursor.execute(sql, [roomnumber_editroom.get()])
    db_roomnumbercheck = cursor.fetchone()

    if db_roomnumbercheck is None or roomnumber_editroom.get() != db_roomnumbercheck[0]:
        messagebox.showwarning("Riski Apartment : Warning", "ไม่พบหมายเลขห้อง %s" % (roomnumber_editroom.get()))
        entry_roomnumber_editRoom.delete(0, END)
        entry_floor_editRoom.delete(0, END)
        roomtype_editroom.set('ประเภทห้อง')
        roomstatus_editroom.set('สถานะห้อง')
        entry_roomnumber_editRoom.focus_force

    else:
        floor_editroom.set(db_roomnumbercheck[1])
        roomtype_editroom.set(db_roomnumbercheck[2])
        roomstatus_editroom.set(db_roomnumbercheck[5])

def editRoom_edit_backend() : #เสร็จแล้ว โดย Haris
    roomtype_price = 0
    unit = 0
    room_execute = conn.execute('SELECT * FROM room')
    for db_room in room_execute :
        if db_room[2] == roomtype_editroom.get() :
            roomtype_price = db_room[3]
            unit = db_room[4]
            break  # exit the loop once a matching room type is found
    sql = '''
            UPDATE room
            SET room_number=?, floor=?, room_type=?, price=?, unit=?, status=?
            WHERE room_number=?    
        '''
    cursor.execute(sql, [roomnumber_editroom.get(), floor_editroom.get(), roomtype_editroom.get(), roomtype_price, unit, roomstatus_editroom.get(), roomnumber_editroom.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "แก้ไขห้อง %s เรียบร้อยแล้ว" % (roomnumber_editroom.get()))
    entry_roomnumber_editRoom.delete(0, END)
    entry_floor_editRoom.delete(0, END)
    roomtype_editroom.set('ประเภทห้อง')
    roomstatus_editroom.set('สถานะห้อง')
    entry_roomnumber_editRoom.focus_force()
    editRoom_fn()

def editRoom_delete_backend() : #เสร็จแล้ว โดย Haris
    delete_confirm = messagebox.askquestion("Riski Apartment : ยืนยันการลบ", "คุณแน่ใจหรือไม่ว่าจะลบห้อง %s"%(roomnumber_editroom.get()))
    if delete_confirm == 'yes' :
        sql = '''
                DELETE FROM room WHERE room_number=?
            '''
        cursor.execute(sql, [roomnumber_editroom.get()])
        conn.commit()
        messagebox.showinfo("Riski Apartment : Success", "ลบห้อง %s เรียบร้อยแล้ว" % (roomnumber_editroom.get()))
        entry_roomnumber_editRoom.delete(0, END)
        entry_floor_editRoom.delete(0, END)
        roomtype_editroom.set('ประเภทห้อง')
        roomstatus_editroom.set('สถานะห้อง')
        entry_roomnumber_editRoom.focus_force()
        editRoom_fn()

def service_fn() : #เสร็จแล้ว #หน้า Main บริการต่าง ๆ #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 14:34 07/04/2023
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

def ratemanage_fn() : #เสร็จแล้ว #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:01 07/04/2023
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

def roomrate_fn() : #เสร็จแล้ว #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 17:11 07/04/2023
    global entry_oldrate_roomrate, entry_newrate_roomrate
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
    room_type = ["รายเดือนแอร์", "รายเดือนพัดลม", "รายวันแอร์", "ห้องแถว"]
    roomtype = OptionMenu(frm_right_roomrate_bg, roomtype_roomrate, *room_type).place(x=320, y=60, width=310) #Spy
    roomtype_roomrate.set('ประเภทห้อง')
    Label(frm_right_roomrate_bg, text='ราคาเดิม : ', bg='#DDDDDD').place(x=190, y=120)
    entry_oldrate_roomrate = Entry(frm_right_roomrate_bg, textvariable=oldrate_roomrate) #Spy
    entry_oldrate_roomrate.place(x=320, y=120)
    Label(frm_right_roomrate_bg, text='ราคาใหม่ : ', bg='#DDDDDD').place(x=189, y=180)
    entry_newrate_roomrate = Entry(frm_right_roomrate_bg, textvariable=newrate_roomrate) #Spy
    entry_newrate_roomrate.place(x=320, y=180)
    Button(frm_right_roomrate_bg, image=btn_save, bg='#DDDDDD', bd=0, command=roomrate_backend).place(x=450, y=280)
    Button(frm_right_roomrate_bg, image=btn_search, bg='#DDDDDD', bd=0, command=roomrate_search_backend).place(x=650, y=65)

def roomrate_search_backend() : #เสร็จแล้ว โดย Haris
    #INSERT DATA
    room_execute = conn.execute('SELECT * FROM room')
    for db_room in room_execute :
        if db_room[2] == roomtype_roomrate.get() :
            roomtype_price = db_room[3]
            oldrate_roomrate.set(roomtype_price)

def roomrate_backend() : #เสร็จแล้ว โดย Haris
    room_execute = conn.execute('SELECT * FROM room')
    for db_room in room_execute :
        if db_room[2] == roomtype_roomrate.get() :
            roomtype_price = int(newrate_roomrate.get())
            break
    sql = '''
            UPDATE room
            SET price=?
            WHERE room_type=?    
    '''
    cursor.execute(sql, [roomtype_price, roomtype_roomrate.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "แก้ไขราคาห้อง %s เรียบร้อยแล้ว" % (roomtype_roomrate.get()))
    roomrate_fn()

def waterelectricrate_fn() : #เสร็จแล้ว #หน้า กำหนดค่าน้ำค่าไฟต่อหน่วย #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 17:06 07/04/2023
    global entry_waterrate_waterelec, entry_electricrate_waterelec
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
    Label(frm_right_waterelec, text='ค่าน้ำ / ไฟ ต่อหน่วย', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=455, y=80)
    #WATER RATE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=100, y=300)
    Label(frm_right_waterelec, text='ค่าน้ำ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=280, y=340)
    Label(frm_right_waterelec, text='ราคาใหม่ :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=140, y=450) 
    entry_waterrate_waterelec = Entry(frm_right_waterelec, width=15, textvariable=waterrate_waterelec) #Spy
    entry_waterrate_waterelec.place(x=260, y=450)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD', command=waterrate_save_backend).place(x=310, y=570)
    #ELECTRICITY RATE
    Label(frm_right_waterelec, width=30, height=15, bd=0, bg='#DDDDDD').place(x=700, y=300)
    Label(frm_right_waterelec, text='ค่าไฟ', bg='#DDDDDD', fg='#084235', font = 'Calibri 30 bold').place(x=875, y=340)
    Label(frm_right_waterelec, text='ราคาใหม่ :', bg='#DDDDDD', fg='#084235', font = 'Calibri 19').place(x=740, y=450) 
    entry_electricrate_waterelec = Entry(frm_right_waterelec, width=15, textvariable=electricrate_waterelec) #Spy
    entry_electricrate_waterelec.place(x=865, y=450)
    Button(frm_right_waterelec, image=btn_save, bd=0, bg='#DDDDDD', command=electricrate_save_backend).place(x=920, y=570)

def waterrate_save_backend() : #เสร็จแล้ว โดย Haris
    sql = "UPDATE room SET water_rate = ?"
    cursor.execute(sql, [waterrate_waterelec.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "อัพเดทค่าน้ำเรียบร้อยแล้ว")
    entry_waterrate_waterelec.delete(0, END)
    waterelectricrate_fn()

def electricrate_save_backend() : #เสร็จแล้ว โดย Haris
    sql = "UPDATE room SET electric_rate = ?"
    cursor.execute(sql, [electricrate_waterelec.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "อัพเดทค่าไฟเรียบร้อยแล้ว")
    entry_electricrate_waterelec.delete(0, END)
    waterelectricrate_fn()

def payment_fn() : #เสร็จแล้ว #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:11 07/04/2023
    global entry_phone_payment, entry_name_payment, entry_roomtype_payment, entry_rent_payment, entry_electric_payment, entry_water_payment, entry_total_payment
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
    entry_phone_payment = Entry(frm_right_payment_bg, textvariable=phone_payment) #Spy
    entry_phone_payment.place(x=270, y=60)
    Button(frm_right_payment_bg, image=btn_search, bd=0, bg='#DDDDDD', command=payment_search_backend).place(x=600, y=60)
    Label(frm_right_payment_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=105, y=120)
    entry_name_payment = Entry(frm_right_payment_bg, textvariable=name_payment) #Spy
    entry_name_payment.place(x=270, y=120)
    Label(frm_right_payment_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=120, y=180)
    entry_roomtype_payment = Entry(frm_right_payment_bg, textvariable=roomtype_payment) #Spy
    entry_roomtype_payment.place(x=270, y=180)
    Label(frm_right_payment_bg, text='ค่าเช่าห้อง : ', bg='#DDDDDD').place(x=130, y=240)
    entry_rent_payment = Entry(frm_right_payment_bg, textvariable=rent_payment) #Spy
    entry_rent_payment.place(x=270, y=240)
    Label(frm_right_payment_bg, text='ค่าไฟ : ', bg='#DDDDDD').place(x=175, y=300)
    entry_electric_payment = Entry(frm_right_payment_bg, textvariable=electric_payment) #Spy
    entry_electric_payment.place(x=270, y=300)
    Label(frm_right_payment_bg, text='ค่าน้ำ : ', bg='#DDDDDD').place(x=175, y=360)
    entry_water_payment = Entry(frm_right_payment_bg, textvariable=water_payment) #Spy
    entry_water_payment.place(x=270, y=360)
    Label(frm_right_payment_bg, text='รวม : ', bg='#DDDDDD').place(x=190, y=420)
    entry_total_payment = Entry(frm_right_payment_bg, textvariable=total_payment) #Spy
    entry_total_payment.place(x=270, y=420)
    Button(frm_right_payment_bg, image=btn_invoices, bd=0, bg='#DDDDDD').place(x=150, y=600)
    Button(frm_right_payment_bg, image=btn_paystat, bd=0, bg='#DDDDDD', command=paymentstatus_fn).place(x=400, y=600)

def payment_search_backend() : #เสร็จแล้ว โดย Haris
    #Fetch customer
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_payment.get()])
    db_customer = cursor.fetchone()
    #Fetch service_log
    sql = 'SELECT * FROM service_log WHERE phonenumber=?'
    cursor.execute(sql, [db_customer[0]])
    db_log = cursor.fetchone()

    if db_customer is None or phone_payment.get() != db_customer[0] :
        messagebox.showwarning("Riski Apartment : Warning", "ไม่พบเบอร์โทรศัพท์ %s"%(phone_payment.get()))
        #entry_phone_payment, entry_name_payment, entry_roomtype_payment, entry_rent_payment, entry_electric_payment, entry_water_payment, entry_total_payment
        entry_phone_payment.delete(0, END)
    else :
        name_payment.set(db_customer[2] + " " + db_customer[3])
        roomtype_payment.set(db_log[4])
        rent_payment.set(db_log[11])
        electric_payment.set(db_log[6])
        water_payment.set(db_log[7])
        total = db_log[11] + db_log[6] + db_log[7]
        total_payment.set(total)

def paymentstatus_fn() : #ยังไม่สมบูรณ์ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 00:07
    global entry_phone_paymentstatus, entry_name_paymentstatus
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
    entry_phone_paymentstatus = Entry(frm_right_paymentstatus_bg, textvariable=phone_paymentstatus) #Spy
    entry_phone_paymentstatus.place(x=270, y=60)
    Label(frm_right_paymentstatus_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=105, y=120)
    entry_name_paymentstatus = Entry(frm_right_paymentstatus_bg, textvariable=name_paymentstatus) #Spy
    entry_name_paymentstatus.place(x=270, y=120)
    Label(frm_right_paymentstatus_bg, text='สถานะการชำระเงิน : ', bg='#DDDDDD').place(x=52, y=180)
    payment_status = ["ชำระเงินแล้ว", "ยังไม่ได้ชำระเงิน"]
    paymentstatus = OptionMenu(frm_right_paymentstatus_bg, status_paymentstatus, *payment_status).place(x=270, y=180, width=310) #Spy
    status_paymentstatus.set("สถานะการชำระเงิน")

    Button(frm_right_paymentstatus_bg, image=btn_printreceipt, bd=0, bg='#DDDDDD' ).place(x=150, y=280)
    Button(frm_right_paymentstatus_bg, image=btn_finish, bd=0, bg='#DDDDDD' , command=paymentstatus_backend).place(x=450, y=280)
    #Insert Data
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_payment.get()])
    db_customer = cursor.fetchone()

    sql = 'SELECT * FROM service_log WHERE phonenumber=?'
    cursor.execute(sql, [db_customer[0]])
    db_log = cursor.fetchone()

    phone_paymentstatus.set(db_log[0])
    name_paymentstatus.set(db_log[3])

def paymentstatus_backend() : #ยังไม่สมบูรณ์
    sql = '''
            UPDATE service_log
            SET payment_status=?
            WHERE phonenumber=?
    '''
    cursor.execute(sql, [status_paymentstatus.get(), phone_payment.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "อัพเดทสถานะการชำระเงิน")
    entry_phone_payment.delete(0, END)
    name_payment.set("")
    roomtype_payment.set("")
    rent_payment.set("")
    electric_payment.set("")
    water_payment.set("")
    total_payment.set("")
    payment_fn()

def help_fn() : #เสร็จแล้ว #หน้า Rate manage #โค้ดนี้กำลังแก้ไขโดย Haris เวลา 15:11 07/04/2023 เพิ่มเติมโดย บูม
    global entry_date_help, entry_inform_help, entry_adminname_help
    name_user = db_user[3] + " " + db_user[4]
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
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
    Label(frm_right_help, text='บริการช่วยเหลือ', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=475, y=80)
    frm_right_help_bg = Frame(frm_right_help, bg='#DDDDDD')
    frm_right_help_bg.place(x=276, y=200, width=750, height=320)
    Label(frm_right_help_bg, text='วันที่ : ', bg='#DDDDDD').place(x=160, y=50)
    entry_date_help = Entry(frm_right_help_bg, textvariable=date_help, state='readonly') #Spy
    entry_date_help.place(x=230, y=50)
    date_help.set(current_date)
    Label(frm_right_help_bg, text='เรื่องที่แจ้ง : ', bg='#DDDDDD').place(x=115, y=110)
    entry_inform_help = Entry(frm_right_help_bg, textvariable=request_help) #Spy
    entry_inform_help.place(x=230, y=110)
    Label(frm_right_help_bg, text='เจ้าหน้าที่ : ', bg='#DDDDDD', ).place(x=120, y=170)
    entry_adminname_help = Entry(frm_right_help_bg, textvariable=admin_help, state='readonly') #Spy
    entry_adminname_help.place(x=230, y=170)
    admin_help.set(name_user)
    Button(frm_right_help_bg, image=btn_finish, bg='#DDDDDD', bd=0, command=help_backend).place(x=360, y=240)

def help_backend() : #เสร็จแล้ว โดย Haris
    name_user = db_user[3] + " " + db_user[4]
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    sql = '''INSERT INTO report_problem (date, employee_name, report_details) VALUES (?,?,?)'''
    cursor.execute(sql, [current_date, name_user, request_help.get()])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "รับเรื่องเรียบร้อย")
    date_help.set("")
    help_fn()

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
        Button(frm_right_datareport, image=btn_savepayment, width=250, height=350, bg='#DDDDDD', bd=0, command=savepayment_fn).place(x=900, y=530)
        Label(frm_right_datareport, text='บันทึกรายจ่าย', fg='#376957', bg='white').place(x=970, y=900)
    if db_user[5] == "U" :
        Button(frm_right_datareport, image=btn_doc, width=250, height=350, bg='#DDDDDD', bd=0, command=servicelog_fn).place(x=170, y=100)
        Label(frm_right_datareport, text='บันทึกการใช้บริการ', fg='#376957', bg='white').place(x=210, y=470)
        Button(frm_right_datareport, image=btn_pay, width=250, height=350, bg='#DDDDDD', bd=0, command=pay_fn).place(x=535, y=100)
        Label(frm_right_datareport, text='รายจ่าย', fg='#376957', bg='white').place(x=630, y=470)
        Button(frm_right_datareport, image=btn_information, width=250, height=350, bg='#DDDDDD', bd=0, command=receivenoti_fn).place(x=900, y=100)
        Label(frm_right_datareport, text='เรื่องที่รับแจ้ง', fg='#376957', bg='white').place(x=994, y=470)
        Button(frm_right_datareport, image=btn_savepayment, width=250, height=350, bg='#DDDDDD', bd=0, command=savepayment_fn).place(x=170, y=530)
        Label(frm_right_datareport, text='บันทึกรายจ่าย', fg='#376957', bg='white').place(x=235, y=900)

def servicelog_fn() : # หน้าบันทึกการใช้บริการ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    global entry_phonenum_servicelog, entry_name_servicelog, entry_roomnum_servicelog, entry_roomtype_servicelog, entry_floor_servicelog
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
    entry_phonenum_servicelog = Entry(frm_right_servicelog_bg, textvariable=phone_servicelog) #Spy
    entry_phonenum_servicelog.place(x=350, y=60)
    Button(frm_right_servicelog_bg, image=btn_search, bd=0, bg='#DDDDDD', command=servicelog_search_fn).place(x=670, y=58)
    Label(frm_right_servicelog_bg, text='ชื่อ-นามสกุล : ', bg='#DDDDDD').place(x=183, y=120)
    entry_name_servicelog = Entry(frm_right_servicelog_bg, textvariable=name_servicelog, state='readonly') #Spy
    entry_name_servicelog.place(x=350, y=120)
    Label(frm_right_servicelog_bg, text='เลขห้อง : ', bg='#DDDDDD').place(x=232, y=180)
    entry_roomnum_servicelog = Entry(frm_right_servicelog_bg, textvariable=number_servicelog, state='readonly') #Spy
    entry_roomnum_servicelog.place(x=350, y=180)
    #room type
    Label(frm_right_servicelog_bg, text='ประเภทห้อง : ', bg='#DDDDDD').place(x=200, y= 240)
    entry_roomtype_servicelog = Entry(frm_right_servicelog_bg, textvariable=roomtype_servicelog, state='readonly') #Spy
    entry_roomtype_servicelog.place(x=350, y=240)
    Label(frm_right_servicelog_bg, text='ชั้น : ', bg='#DDDDDD').place(x=275, y= 300)
    entry_floor_servicelog = Entry(frm_right_servicelog_bg, textvariable=floor_servicelog, state='readonly') #Spy
    entry_floor_servicelog.place(x=350, y=300)
    Button(frm_right_servicelog_bg, image=btn_next,bd=0, bg='#DDDDDD', command=servicelogsave_fn).place(x=480, y=450)

def servicelog_search_fn() : #เสร็จแล้ว โดย Haris
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_servicelog.get()])
    db_customer = cursor.fetchone()

    if db_customer is None or phone_servicelog.get() != db_customer[0] :
        messagebox.showwarning('Riski Apartment : Warning', 'ไม่พบลูกค้า หรือเบอร์โทรศัพท์ไม่ถูกต้อง')
    else : 
        name_servicelog.set(db_customer[2] + ' ' + db_customer[3])
    if db_customer[1] == '-' :
        messagebox.showwarning('Riski Apartment : Warning', 'ลูกค้ายังไม่ได้ Check In หรือว่า ลูกค้าทำการ Check Out ไปแล้ว')
        entry_phonenum_servicelog.delete(0, END)
        entry_name_servicelog.delete(0, END)
    else :
        number_servicelog.set(db_customer[1])
        sql = 'SELECT * FROM room WHERE room_number=?'
        cursor.execute(sql, [db_customer[1]])
        db_room = cursor.fetchone()
        roomtype_servicelog.set(db_room[2])
        floor_servicelog.set(db_room[1])

def servicelogsave_fn() : # บันทึกการใช้บริการ ค่าน้ำ ค่าไฟ #โค้ดนี้กำลังแก้ไขโดย นัท 07/04/2023 เวลา 18:05
    global entry_roomnum_servicelogsave, entry_electric_servicelogsave, entry_water_servicelogsave, entry_watermeter_servicelogsave, entry_electricmeter_servicelogsave, servicelog_logic
    global savedate
    servicelog_logic = "F"
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
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
    entry_roomnum_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=number_servicelogsave, state='readonly') #Spy
    entry_roomnum_servicelogsave.place(x=270, y=60)
    Label(frm_right_servicelogsave_bg, text='ค่าไฟ / หน่วย : ', bg='#DDDDDD').place(x=90, y=120)
    entry_electric_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=electric_servicelogsave, state='readonly') #Spy
    entry_electric_servicelogsave.place(x=270, y=120)
    Label(frm_right_servicelogsave_bg, text='ค่าน้ำ / หน่วย : ', bg='#DDDDDD').place(x=92, y=180)
    entry_water_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=water_servicelogsave, state='readonly') #Spy
    entry_water_servicelogsave.place(x=270, y=180)
    Label(frm_right_servicelogsave_bg, text='เลขมิเตอร์น้ำ : ', bg='#DDDDDD').place(x=108, y=240)
    entry_watermeter_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=watermeter_servicelogsave) #Spy
    entry_watermeter_servicelogsave.place(x=270, y=240)
    Label(frm_right_servicelogsave_bg, text='เลขมิเตอร์ไฟฟ้า : ', bg='#DDDDDD').place(x=82, y=300)
    entry_electricmeter_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=electricmeter_servicelogsave) #Spy
    entry_electricmeter_servicelogsave.place(x=270, y=300)
    Label(frm_right_servicelogsave_bg, text='วันที่บันทึก : ', bg='#DDDDDD').place(x=130, y=360)
    # savedate = DateEntry(frm_right_servicelogsave_bg, selectmode='day', date_pattern='dd/mm/yyyy')
    # savedate.place(x=270, y=360)
    entry_date_servicelogsave = Entry(frm_right_servicelogsave_bg, textvariable=date_servicelogsave, state='readonly') #Spy
    entry_date_servicelogsave.place(x=270, y=360)
    date_servicelogsave.set(current_date)
    Button(frm_right_servicelogsave_bg, image=btn_finish,bd=0, bg='#DDDDDD', command=servicelogsave_backend).place(x=400, y=500)
    Button(frm_right_servicelogsave_bg, image=btn_save,bd=0, bg='#DDDDDD').place(x=200, y=500)
    #Insert data
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_servicelog.get()])
    db_customer = cursor.fetchone()
    number_servicelogsave.set(db_customer[1])
    sql = 'SELECT * FROM room WHERE room_number=?'
    cursor.execute(sql, [db_customer[1]])
    db_room = cursor.fetchone()
    electric_servicelogsave.set(db_room[7])
    water_servicelogsave.set(db_room[6])

# def get_date() : #เสร็จแล้ว โดย Haris
#     global servicelog_logic
#     servicelog_logic = "T"
#     date = savedate.get_date()
#     save_date = date.strftime("%d/%m/%Y")   
#     return save_date

def servicelogsave_backend() : #เสร็จแล้ว โดย Haris
    save_date = date_servicelogsave.get()
    #Fetch customer
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_servicelog.get()])
    db_customer = cursor.fetchone()
    #Fetch room
    sql = 'SELECT * FROM room WHERE room_number=?'
    cursor.execute(sql, [db_customer[1]])
    db_room = cursor.fetchone()
    #Fetch service_log
    sql = 'SELECT * FROM service_log WHERE phonenumber=?'
    cursor.execute(sql, [db_customer[0]])
    #Update service_log
    sql = '''
            UPDATE service_log
            SET electric_meter=?, water_meter=?, date=?
            WHERE phonenumber=?
    '''
    cursor.execute(sql, [electricmeter_servicelogsave.get(), watermeter_servicelogsave.get(), save_date, db_customer[0]])
    conn.commit()
    messagebox.showinfo("Riski Apartment : Success", "บันทึก Service log เรียบร้อย")
    calculaterent_backend()

def calculaterent_backend() :
    #Fetch customer
    sql = 'SELECT * FROM customer WHERE phonenumber=?'
    cursor.execute(sql, [phone_servicelog.get()])
    db_customer = cursor.fetchone()
    #Fetch room
    sql = 'SELECT * FROM room WHERE room_number=?'
    cursor.execute(sql, [db_customer[1]])
    db_room = cursor.fetchone()
    #Fetch service_log
    sql = 'SELECT * FROM service_log WHERE phonenumber=?'
    cursor.execute(sql, [db_customer[0]])
    db_log = cursor.fetchone()

    #Get Check in date
    check_in = db_room[9]
    check_in_date = datetime.strptime(check_in, "%d/%m/%Y")
    #Get Check out date
    check_out = db_room[10]
    check_out_date = datetime.strptime(check_out, "%d/%m/%Y")

    #Calculate duration of stay
    duration = (check_out_date - check_in_date).days

    #Calculate the total rent
    rent_per_month = db_room[3]
    rent_total = rent_per_month * ((duration // 30))

    #Calculate payment date
    start_date = datetime(check_in_date.year, check_in_date.month, 1).date()
    end_date = datetime(check_out_date.year, check_out_date.month+1, 1).date()
    payment_date = start_date
    payment_list = []
    while payment_date < end_date:
        payment_list.append(rent_per_month)
        payment_date = datetime(payment_date.year, payment_date.month+1, 1).date()

    total_months = (duration // 30)
    total_rent = rent_total

    print(total_months)
    print(total_rent)
    print(payment_list)

    #เตือนตัวเองตอนตื่นนอน ค้างอยู่ตรงนี้ ให้ตื่นมาทำตัวเช็คสถานะการเช็คเงิน จาก table service_log
    #แนวคิดระบบนี้พิมไว้ใน chatgpt ไปอ่านทวนความจำ
    #Check payment status
    paid = True #"ชำระเงินแล้ว"
    for row in cursor.fetchall():
        if row[4] != 'paid':
            paid = False #"ยังไม่ได้ชำระเงิน" 
            break

    # payment_status = db_log[10]
    # for row in db_log[10] :
    if db_log[10] == 'ชำระเงินแล้ว':
        print("ชำระเงินแล้ว")
        #Show new payment list to customer
        current_month = datetime.now().month
        current_year = datetime.now().year
        payment_list_display = []
        for payment_month in range(current_month, current_month+total_months):
            payment_list_display.append(f"{payment_month}/{current_year}")
        print("ค่าห้องในรอบถัดไปที่ต้องชำระ:")
        for payment in payment_list_display[1:]:
            print(f" - {db_room[1]}: {db_room[3]} บาท ({payment})")
    else:
        print("ยังไม่ได้ชำระเงิน")
    #return total_months, total_rent, payment_list


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

def savepayment_fn() :
    #MAIN
    root.title("Riski Apartment : บันทึกรายจ่าย")
    frm_main_savepayment = Frame(root, bg='black')
    frm_main_savepayment.place(x=0, y=0, width = w, height = h)

    #FRAME LEFT
    frm_left_savepayment = Frame(frm_main_savepayment, bg='#084235')
    frm_left_savepayment.place(x=0, y=0, width=650, height=1080)

    #FRAME RIGHT
    frm_right_savepayment = Frame(frm_main_savepayment, bg='white')
    frm_right_savepayment.place(x=651,y=0, width= 1269, height=1080)

    #LOGO
    Button(frm_left_savepayment, image=img_riskilogos, bd=0 , bg='#084235', command=home_fn).place(x=30, y=30)

    #LEFT
    Button(frm_left_savepayment, image=btn_datareport, bd=0, bg='#084235', command=datareport_fn).place(x=125, y=185)
    Button(frm_left_savepayment, image=btn_home, bd=0, bg='#084235', command=home_fn).place(x=30, y=900)

    #RIGHT
    Label(frm_right_savepayment, text='บันทึกค่าใช้จ่าย', bg='white', font = 'Calibri 40 bold', fg='#376957').place(x=465, y=110)
    frm_right_savepayment_bg = Frame(frm_right_savepayment, bg='#DDDDDD')
    frm_right_savepayment_bg.place(x=220, y=270, width=800, height=500)
    Label(frm_right_savepayment_bg, text='ค่าน้ำ / ค่าไฟ : ', bg='#DDDDDD').place(x=90, y=65)
    entry_waterelectric_savepayment = Entry(frm_right_savepayment_bg).place(x=250, y=65)
    Label(frm_right_savepayment_bg, text='อื่น ๆ : ', bg='#DDDDDD').place(x=173, y=165)
    entry_others_savepayment = Entry(frm_right_savepayment_bg).place(x=250, y=165)
    Label(frm_right_savepayment_bg, text='วันที่บันทึก : ', bg='#DDDDDD').place(x=121, y=265)
    entry_savedate_savepayment = Entry(frm_right_savepayment_bg).place(x=250, y=265)
    Label(frm_right_savepayment_bg, text='(วว/ดด/ปปปป)', bg='#DDDDDD', fg='#969696').place(x=600, y=265)
    Button(frm_right_savepayment_bg, image=btn_save, bg='#DDDDDD', bd=0).place(x=385, y=350)

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
#login
userentry = StringVar()
passwordentry = StringVar()
#addemployee
name_addemp = StringVar()
lastname_addemp = StringVar()
username_addemp = StringVar()
password_addemp = StringVar()
phone_addemp = StringVar()
#addcustomer
name_addcus = StringVar()
lastname_addcus = StringVar()
phone_addcus  = StringVar()
ethinicity_addcus = StringVar()
nation_addcus = StringVar()
number_addcus = StringVar()
village_addcus = StringVar()
road_addcus = StringVar()
subdistrict_addcus = StringVar()
#addroom
district_addcus = StringVar()
province_addcus = StringVar()
roomtype_addroom = StringVar()
roomnumber_addroom = StringVar()
floor_addroom = StringVar()
#editroom
floor_editroom = StringVar()
roomnumber_editroom = StringVar()
roomtype_editroom = StringVar()
roomstatus_editroom = StringVar()
#editempaccount
findphone_editempaccount = StringVar()
name_editempaccount = StringVar()
lastname_editempaccount = StringVar()
username_editempaccount = StringVar()
password_editempaccount = StringVar()
phone_editempaccount = StringVar()
#searchcustomerinfo
phone_searchcusinfo = StringVar()
name_searchcusinfo = StringVar()
#editcustomerinfo
name_editcusinfo = StringVar()
lastname_editcusinfo = StringVar()
phone_editcusinfo = StringVar()
ethinicity_editcusinfo = StringVar()
nation_editcusinfo = StringVar()
number_editcusinfo = StringVar()
village_editcusinfo = StringVar()
road_editcusinfo = StringVar()
subdistrict_editcusinfo = StringVar()
district_editcusinfo = StringVar()
province_editcusinfo = StringVar()
#roomrate
roomtype_roomrate = StringVar()
oldrate_roomrate = StringVar()
newrate_roomrate = StringVar()
#waterelectricrate
waterrate_waterelec = StringVar()
electricrate_waterelec = StringVar()
#payment
phone_payment = StringVar()
name_payment = StringVar()
roomtype_payment = StringVar()
rent_payment = StringVar()
electric_payment = StringVar()
water_payment = StringVar()
total_payment = StringVar()
#checkin
phone_checkin = StringVar()
name_checkin = StringVar()
floor_checkin = StringVar() 
price_checkin = StringVar()
roomtype_checkin = StringVar()
number_checkin = StringVar()
#checkin date
employee_checkindate = StringVar()
#servicelog
phone_servicelog = StringVar()
name_servicelog = StringVar()
number_servicelog = StringVar()
roomtype_servicelog = StringVar()
floor_servicelog = StringVar()
#checkout
phone_checkout = StringVar()
name_checkout = StringVar()
number_checkout = StringVar()
roomtype_checkout = StringVar()
floor_checkout = StringVar()
#checkout date
startdate_checkoutdate = StringVar()
enddate_checkoutdate = StringVar()
user_checkoutdate = StringVar()
#servicelog save
number_servicelogsave = StringVar()
electric_servicelogsave = StringVar()
water_servicelogsave = StringVar()
watermeter_servicelogsave = StringVar()
electricmeter_servicelogsave = StringVar()
date_servicelogsave = StringVar()
#payment status
phone_paymentstatus = StringVar()
name_paymentstatus = StringVar()
status_paymentstatus = StringVar()
#help
date_help = StringVar()
request_help = StringVar()
admin_help = StringVar()
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
btn_savepayment = PhotoImage(file='button/btn_savepayment.png')

login_fn()
root.mainloop()