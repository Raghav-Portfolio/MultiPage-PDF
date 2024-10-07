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
for index, rows in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(100,100,100) # combination for gray colour in RGB
    pdf.cell(w=0, h=12, txt=row['topics'], align='L', ln=1)
    pdf.line(10,21, 200, 21)



pdf.output('output.pdf')