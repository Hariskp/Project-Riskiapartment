from fpdf import FPDF

# Define the receipt information
customer_name = "John Smith"
room_number = "101"
start_date = "April 1, 2023"
end_date = "April 7, 2023"
price_per_night = 50
total_price = price_per_night * 6

# Create a new PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font and size for the title
pdf.set_font("Arial", "B", 16)

# Add the title
pdf.cell(0, 10, "Renting Room Receipt", 0, 1, "C")

# Set the font and size for the receipt information
pdf.set_font("Arial", "", 12)

# Add the customer name
pdf.cell(50, 10, "Customer Name :", 0)
pdf.cell(0, 10, customer_name, 0, 1)

# Add the room number
pdf.cell(50, 10, "Room Number :", 0)
pdf.cell(0, 10, room_number, 0, 1)

# Add the start date
pdf.cell(50, 10, "Start Date :", 0)
pdf.cell(0, 10, start_date, 0, 1)

# Add the end date
pdf.cell(50, 10, "End Date :", 0)
pdf.cell(0, 10, end_date, 0, 1)

# Add the price per night
pdf.cell(150, 10, "Price per Night :", 0)
pdf.cell(0, 10, f"${price_per_night}", 0, 1)

# Add the total price
pdf.cell(150, 10, "Total Price :", 0)
pdf.cell(0, 10, f"${total_price}", 0, 1)

# Save the PDF
pdf.output("test.pdf")