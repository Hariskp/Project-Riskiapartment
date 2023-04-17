from fpdf import FPDF
import sqlite3

def createconnection() : 
    global conn, cursor
    conn = sqlite3.connect('database/riski_database.db')
    cursor = conn.cursor()

def payreceipt_pdf():
    sql = 'SELECT * FROM customer WHERE phonenumber=0805847716'
    cursor.execute(sql)
    db_customer = cursor.fetchone()

    renter_name = db_customer[0] #data base customer
    room_number = "101" #data base customer & room
    rent_amount = 1000
    deposit_amount = 500
    total_amount = rent_amount + deposit_amount
    date = "April 16, 2023" #data base room
    address = "123 Pachalam Khuen Bog" #data base 
    admin_name = "Jittawat Praditseree" #data base user
    phone_number = "099-182-8589" #data base user
    phone_number_rent = "081-817-8555"

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=22, style="B")
    pdf.cell(0, 15, "RISKI APARTMENT RECEIPT", 0, 1, "C")
    pdf.cell(0, 10, "", 0, 1)
    pdf.line(10, 32, 200, 32)
    pdf.image("img/img_riskilogo_black.png", x=10, y=1, w=30, h=30)

    pdf.cell(0, 10, "", 0, 1) #space
    
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(50, 10, "Date :", 0 )
    pdf.cell(0, 10, date, 0, 1,"C")
    pdf.cell(50, 10, "Renter Name :", 0)
    pdf.cell(0, 10, renter_name, 0, 1,"C")
    pdf.cell(50, 10, "Phone Number :", 0)
    pdf.cell(0, 10, phone_number_rent, 0, 1,"C")

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(50, 10, "Room Number :", 0)
    pdf.cell(0, 10, room_number, 0, 1,"C")

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(50, 10, "Rent Amount :", 0)
    pdf.cell(0, 10, f"${rent_amount}", 0, 1,"C")
    pdf.cell(50, 10, "Deposit Amount :", 0)
    pdf.cell(0, 10, f"${deposit_amount}", 0, 1,"C")
    pdf.cell(50, 10, "Total Amount :", 0)
    pdf.cell(0, 10, f"${total_amount}", 0, 1,"C")

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(50, 10, "Admin Name :", 0)
    pdf.cell(0, 10, admin_name, 0, 1,"C")
    pdf.cell(50, 10, "Phone Number :", 0)
    pdf.cell(0, 10, phone_number, 0, 1,"C")
    pdf.cell(50, 10, "Address :", 0)
    pdf.cell(0, 10, address, 0, 1,"C")


    pdf.set_font("Arial", size=8, style="I")

    pdf.cell(0, 20, "", 0, 1) #space

    pdf.cell(0, 10, "Thank you for your payment!", 0, 1, "C")
    pdf.cell(0, 10, "Please contact us if you have any questions.", 0, 1, "C")
    pdf.line(10, 144, 200, 144)
    
    pdf.output('riski_apartment.pdf')

payreceipt_pdf()