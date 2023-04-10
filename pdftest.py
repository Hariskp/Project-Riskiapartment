from fpdf import FPDF

pdf = FPDF()

w = 210 
h = 297


pdf.set_font("Arial","B",16)

pdf.add_page()
pdf.cell(0,7,"Click Me",border=1,align="C")


pdf.output("test.pdf")