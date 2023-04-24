from fpdf import FPDF
import sqlite3

def createconnection() : 
    global conn, cursor
    conn = sqlite3.connect('database/riski_database.db')
    cursor = conn.cursor()

def payreceipt_pdf():
    
    pdf = FPDF()
    pdf.add_page()

    renter_name = "จอม" #data base customer
    room_number = "101" #data base customer & room
    rent_amount = 1000
    deposit_amount = 500
    total_amount = rent_amount + deposit_amount
    date = "16/04/2023" #data base room
    address = "123 ถ.นานานานานานานา" #data base 
    admin_name = "จอม" #data base user
    phone_number = "099-182-8589" #data base user
    phone_number_rent = "081-817-8555"
    
    pdf.add_font('TH Sarabun New','',fname='THSarabunNew.ttf', uni=True)
    pdf.add_font('TH Sarabun New Bold','B',fname='THSarabunNew Bold.ttf', uni=True)

    pdf.set_font("TH Sarabun New Bold", size=30 , style='B')
    pdf.encoding = 'utf-8'
    pdf.cell(0, 15, "RISKI APARTMENT RECEIPT", 0, 1, "C")
    pdf.cell(0, 10, "", 0, 1)
    pdf.line(10, 32, 200, 32)
    pdf.image("img/img_riskilogo_black.png", x=10, y=1, w=30, h=30)

    pdf.cell(0, 10, "", 0, 1) #space
    
    pdf.set_font("TH Sarabun New", size=20 , style='')
    pdf.cell(50, 10, "วันที่ :", 0 )
    pdf.cell(0, 10, date, 0, 1 ,"C")
    pdf.cell(50, 10, "ผู้เช่า :", 0)
    pdf.cell(0, 10, renter_name, 0, 1,"C")
    pdf.cell(50, 10, "เบอร์โทรศัพท์ :", 0)
    pdf.cell(0, 10, phone_number_rent, 0, 1,"C")
    
    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(50, 10, "หมายเลขห้อง :", 0)
    pdf.cell(0, 10, room_number, 0, 1,"C")

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(50, 10, "ค่าเช่า :", 0)
    pdf.cell(0, 10, f"${rent_amount}", 0, 1,"C")
    pdf.cell(50, 10, "ค่าน้ำ/ค่าไฟ :", 0)
    pdf.cell(0, 10, f"${deposit_amount}", 0, 1,"C")
    pdf.cell(50, 10, "รวมทั้งหมด :", 0)
    pdf.cell(0, 10, f"${total_amount}", 0, 1,"C")

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.cell(0, 10, "", 0, 1) #space

    pdf.set_font("TH Sarabun New", size=20 , style='')
    pdf.cell(50, 10, "เจ้าหน้าที่ :", 0)
    pdf.cell(0, 10, admin_name, 0, 1,"C")
    pdf.cell(50, 10, "เบอร์โทรศัพท์ :", 0)
    pdf.cell(0, 10, phone_number, 0, 1,"C")
    pdf.cell(50, 10, "ที่อยู่ :", 0)
    pdf.cell(0, 10, address, 0, 1,"C")


    pdf.set_font("Arial", size=8, style="I")

    pdf.cell(0, 20, "", 0, 1) #space

    pdf.cell(0, 10, "Thank you for your payment!", 0, 1, "C")
    pdf.cell(0, 10, "Please contact us if you have any questions.", 0, 1, "C")
    pdf.line(10, 144, 200, 144)
    
    pdf.output('riski_apartment.pdf')

payreceipt_pdf()