from fpdf import FPDF

renter_name = "Haris Kirdpakdee" #data base
room_number = "101" #data base
rent_amount = 1000
deposit_amount = 500
total_amount = rent_amount + deposit_amount
date = "April 16, 2023" #data base
address = "123 Pachalam Khuen Bog" #data base
admin_name = "Jittawat Praditseree" #data base
phone_number = "099-182-8589" #data base
email = "jittawatofficial@gmail.com"

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=22, style="B")

pdf.cell(0, 15, "RISKI APARTMENT RECEIPT", 0, 1, "C")
pdf.cell(0, 10, "", 0, 1)
pdf.line(10, 28, 200, 28)

pdf.image("img/img_riskilogo_black.png", x=10, y=1, w=30, h=30)

pdf.set_font("Arial", size=12, style="B")

pdf.cell(50, 10, "Date :", 0 )
pdf.cell(0, 10, date, 0, 1,"C")
pdf.cell(50, 10, "Renter Name :", 0)
pdf.cell(0, 10, renter_name, 0, 1,"C")
pdf.cell(50, 10, "Address :", 0)
pdf.cell(0, 10, address, 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Room Number :", 0)
pdf.cell(0, 10, room_number, 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Rent Amount :", 0)
pdf.cell(0, 10, f"${rent_amount}", 0, 1,"C")
pdf.cell(50, 10, "Deposit Amount :", 0)
pdf.cell(0, 10, f"${deposit_amount}", 0, 1,"C")
pdf.cell(50, 10, "Total Amount :", 0)
pdf.cell(0, 10, f"${total_amount}", 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Admin Name :", 0)
pdf.cell(0, 10, admin_name, 0, 1,"C")
pdf.cell(50, 10, "Phone Number :", 0)
pdf.cell(0, 10, phone_number, 0, 1,"C")


pdf.set_font("Arial", size=8, style="I")

pdf.cell(0, 20, "", 0, 1)

pdf.cell(0, 10, "Thank you for your payment!", 0, 1, "C")
pdf.cell(0, 10, "Please contact us if you have any questions.", 0, 1, "C")
pdf.line(10, 135, 200, 135)

pdf.set_fill_color(255, 255, 204)
#pdf.rect(0,270,210,0)


pdf.output("pdf_nut.pdf")
