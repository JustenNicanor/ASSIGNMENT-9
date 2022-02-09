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
Educational = Information["PERSONAL INFORMATION"]["Education"]
Elem = Information["PERSONAL INFORMATION"]["Elem"]
Junior = Information["PERSONAL INFORMATION"]["JHigh"]
Senior = Information["PERSONAL INFORMATION"]["SHigh"]
College = Information["PERSONAL INFORMATION"]["College"]
Course = Information["PERSONAL INFORMATION"]["Course"]

pdf = FPDF('p', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('times', 'B', 30)
pdf.cell(100, 15, 'JUSTEN L. NICANOR', ln=True)
pdf.set_font('times', '', 10)
pdf.cell(50, 5, Adresss, ln=True)
pdf.cell(50, 5, Contact, ln=True)
pdf.cell(50, 5, Email, ln=True)
pdf.set_font('times', 'B', 15)
pdf.cell(50, 15, Personal, ln=True)
pdf.set_font('times', '', 10)
pdf.cell(50, 10, DateofBirth, ln=True)
pdf.cell(50, 10, PlaceofBirth, ln=True)
pdf.cell(50, 10, Gender, ln=True)
pdf.cell(50, 10, CivilStatus, ln=True)
pdf.cell(50, 10, Citizenship, ln=True)
pdf.cell(50, 10, Height, ln=True)
pdf.cell(50, 10, Weight, ln=True)
pdf.cell(50, 10, FathersName, ln=True)
pdf.cell(50, 10, Ocupation, ln=True)
pdf.cell(50, 10, MothersName, ln=True)
pdf.cell(50, 10, Occupation, ln=True)
pdf.cell(50, 10, Address, ln=True)
pdf.set_font('times', 'B', 15)
pdf.cell(50, 15, Educational, ln=True)
pdf.set_font('times', '', 10)
pdf.cell(50, 10, Elem, ln=True)
pdf.cell(50, 10, Junior, ln=True)
pdf.cell(50, 10, Senior, ln=True)
pdf.cell(50, 10, College, ln=True)
pdf.cell(50, 10, Course, ln=True)

pdf.output('NICANOR_JUSTEN.pdf')
