from fpdf import FPDF


admin_name = "Jittawat Praditseree" #data base
renter_name = "Haris Kirdpakdee" #data base 
start_date = "April 1, 2023" #data base 
end_date = "March 31, 2024" #data base 
rent_amount = 1000
security_deposit = 500
address = "123 Pachalam Khuen Bog" #data base 
room_number = "101" #data base 

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=22, style="B")

pdf.cell(0, 20, "Riski Aparment Lease Contact", 0, 1, "C")
pdf.line(10, 28, 200, 28)

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

def footer(self):
        # Go to 1.5 cm from bottom
    self.set_y(-15)
        # Select Arial italic 8
    self.set_font('Arial', 'I', 8)
        # Print centered page number
    self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

pdf.output("lease_jom.pdf")