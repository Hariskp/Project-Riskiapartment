from fpdf import FPDF


admin_name = "Jittawat Praditseree"
renter_name = "Haris Kirdpakdee"
start_date = "April 1, 2023"
end_date = "March 31, 2024"
rent_amount = 1000
security_deposit = 500
address = "123 Pachalam Khuen Bog"
room_number = "101"

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=22, style="B")

pdf.cell(0, 30, "Riski Aparment Lease Contact", 0, 1, "C")

pdf.set_font("Arial", size=12)

pdf.cell(50, 10, "Admin Name:", 0)
pdf.cell(0, 10, admin_name, 0, 1)
pdf.cell(50, 10, "Address:", 0)
pdf.cell(0, 10, address, 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Renter Name:", 0)
pdf.cell(0, 10, renter_name, 0, 1)
pdf.cell(50, 10, "Address:", 0)
pdf.cell(0, 10, address, 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Lease Start Date:", 0)
pdf.cell(0, 10, start_date, 0, 1)
pdf.cell(50, 10, "Lease End Date:", 0)
pdf.cell(0, 10, end_date, 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Room Number:", 0)
pdf.cell(0, 10, room_number, 0, 1)

pdf.cell(0, 10, "", 0, 1)

pdf.cell(50, 10, "Rent Amount:", 0)
pdf.cell(0, 10, f"${rent_amount}", 0, 1)
pdf.cell(50, 10, "Security Deposit:", 0)
pdf.cell(0, 10, f"${security_deposit}", 0, 1)

pdf.cell(0, 10, "", 0, 1)


pdf.cell(0, 10, "TERMS AND CONDITIONS:", 0, 1)
pdf.cell(0, 10, "This Lease Agreement is made and entered into on this date between.", 0, 1)
pdf.cell(0, 10, "The Renter : "f"{renter_name}", 0, 1) 
pdf.cell(0, 10, "The Admin : "f"{admin_name}",0 , 1)

pdf.cell(0, 10, "1. Premises. The Landlord leases to the Renter the premises located at", 0, 1)
pdf.cell(0, 10, "Address : "f"{address}",0, 1)
pdf.cell(0, 10, "The Renter shall have exclusive use of the room numbered. "f"{room_number}", 0, 1)       

pdf.output("lease_jom.pdf")