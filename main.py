from fpdf import FPDF
from pathlib import Path
import glob

pdf = FPDF(orientation='P',unit='mm',format='A4')
filepaths = glob.glob('files/*.txt')
for filepath in filepaths:
    pdf.add_page()
    pdf.set_font(family='Times',style='B',size=20)
    name = Path(filepath).stem
    name = name.title()
    pdf.cell(w=10,h=20,txt=f'{name}',ln=1)
    pdf.line(10,25,200,25)
    
    with open(filepath) as file:
        content = file.read()
    pdf.set_font(family='Times',style='B',size=15)
    pdf.multi_cell(w=0,h=6,txt=content)

        
pdf.output('output.pdf')