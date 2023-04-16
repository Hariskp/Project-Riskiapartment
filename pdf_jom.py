from fpdf import FPDF

renter_name = "Haris Kirdpakdee"
room_number = "101"
rent_amount = 1000
deposit_amount = 500
total_amount = rent_amount + deposit_amount
date = "April 16, 2023"
address = "123 Pachalam Khuen Bog"
admin_name = "Jittawat Praditseree"
phone_number = "099-182-8589"
email = "jittawatofficial@gmail.com"

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=22, style="B")

pdf.cell(0, 30, "Riski Apartment Receipt", 0, 1, "C")

pdf.set_font("Arial", size=12)

pdf.cell(50, 10, "Date:", 0)
pdf.cell(0, 10, date, 0, 1,"C")
pdf.cell(50, 10, "Renter Name:", 0)
pdf.cell(0, 10, renter_name, 0, 1,"C")
pdf.cell(50, 10, "Address:", 0)
pdf.cell(0, 10, address, 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Room Number:", 0)
pdf.cell(0, 10, room_number, 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Rent Amount:", 0)
pdf.cell(0, 10, f"${rent_amount}", 0, 1,"C")
pdf.cell(50, 10, "Deposit Amount:", 0)
pdf.cell(0, 10, f"${deposit_amount}", 0, 1,"C")
pdf.cell(50, 10, "Total Amount:", 0)
pdf.cell(0, 10, f"${total_amount}", 0, 1,"C")

pdf.cell(0, 10, "", 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Admin Name:", 0)
pdf.cell(0, 10, admin_name, 0, 1,"C")
pdf.cell(50, 10, "Phone Number:", 0)
pdf.cell(0, 10, phone_number, 0, 1,"C")
pdf.cell(50, 10, "Email:", 0)
pdf.cell(0, 10, email, 0, 1,"C")

pdf.set_font("Arial", size=8, style="I")

pdf.cell(0, 20, "", 0, 1)

pdf.cell(0, 10, "Thank you for your payment!", 0, 1, "C")
pdf.cell(0, 10, "Please contact us if you have any questions.", 0, 1, "C")

pdf.set_fill_color(255, 255, 204)

pdf.output("pdf_jom.pdf")
