from fpdf import FPDF
import pandas as pd

df=pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit = 'mm', format = 'A4')
# these arguments don't apply to the set_font method as these are concerned with the page layout while 
# set_font is specfically used for styling text. 
"""
The global arguments (such as orientation, unit, and format) only affect the page layout 
and do not influence text properties like fonts. 
Even if you don't call the set_font() method, the global arguments won't impact the font at all. 
"""
pdf.set_auto_page_break(auto=False, margin=0)


for index, rows in df.iterrows():
    pdf.add_page()
    
    #Set the header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100) # combination for gray colour in RGB
    pdf.cell(w=34, h=12, txt=rows['Topic'], align='L', ln=1)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)
    
    #Set the footer
    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(154,232,45)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='R')
    
   

    for i in range(rows['Pages'] - 1):
        pdf.add_page()
         
        #Set the footer
        pdf.ln(272)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(245,232,245)
        pdf.cell(w=0, h=12, txt=rows['Topic'], align='R')
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
pdf.output('output.pdf')