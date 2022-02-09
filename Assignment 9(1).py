from fpdf import FPDF
import json

with open('Personaldetails.json') as jsonfile:
    Information = json.load(jsonfile) 
Adresss = Information["PERSONAL INFORMATION"]["Add"]
Contact =Information["PERSONAL INFORMATION"]["Contact"]
Email = Information["PERSONAL INFORMATION"]["Email"]

Personal = Information["PERSONAL INFORMATION"]["Perinfo"]

DateofBirth	= Information["PERSONAL INFORMATION"]["Date of Birth"]
PlaceofBirth = Information["PERSONAL INFORMATION"]["Place of Birth"]
Gender = Information["PERSONAL INFORMATION"]["Gender"]		
CivilStatus	= Information["PERSONAL INFORMATION"]["Civil Status"]
Citizenship	= Information["PERSONAL INFORMATION"]["Citizenship"]
Height = Information["PERSONAL INFORMATION"]["Height"]		
Weight = Information["PERSONAL INFORMATION"]["Weight"]
FathersName	= Information["PERSONAL INFORMATION"]["Father`s Name"]
Ocupation = Information["PERSONAL INFORMATION"]["Ocupation"]
MothersName = Information["PERSONAL INFORMATION"]["Mother`s Name"]
Occupation	= Information["PERSONAL INFORMATION"]["Occupation"]	
Address	= Information["PERSONAL INFORMATION"]["Address"]

pdf = FPDF('p', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('times', 'B', 30)
pdf.cell(100, 15, 'JUSTEN L. NICANOR', ln=True)
pdf.set_font('times', '', 10)
pdf.cell(50, 5, Adresss, ln=True)
pdf.cell(50, 5, Contact, ln=True)
pdf.cell(50, 5, Email, ln=True)
pdf.set_font('times', 'B', 15)
pdf.cell(50, 10, Personal, ln=True)
pdf.set_font('times', '', 10)
pdf.cell(50, 5, DateofBirth, ln=True)
pdf.cell(50, 5, PlaceofBirth, ln=True)
pdf.cell(50, 5, Gender, ln=True)
pdf.cell(50, 5, CivilStatus, ln=True)
pdf.cell(50, 5, Citizenship, ln=True)
pdf.cell(50, 5, Height, ln=True)
pdf.cell(50, 5, Weight, ln=True)
pdf.cell(50, 5, FathersName, ln=True)
pdf.cell(50, 5, Ocupation, ln=True)
pdf.cell(50, 5, MothersName, ln=True)
pdf.cell(50, 5, Occupation, ln=True)
pdf.cell(50, 5, Address, ln=True)




pdf.output('NICANOR_JUSTEN.pdf')
