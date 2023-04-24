from fpdf import FPDF
import subprocess
import sys


pdf = FPDF()
pdf.add_page()

pdf.add_font('THSarabunNew', '', 'THSarabunNew.ttf', uni=True)

pdf.set_font('THSarabunNew', '', 14)

pdf.cell(20, 10, 'สวัสดีชาวโลก', 0, 1, 'C')

    
pdf.output('test_thai.pdf')
