from fpdf import FPDF
import json

with open('Personaldetails.json') as jsonfile:
    Information = json.load(jsonfile) 
Adresss = Information["PERSONAL INFORMATION"]["Add"]
Contact =Information["PERSONAL INFORMATION"]["Contact"]
Email = Information["PERSONAL INFORMATION"]["Email"]
Skills = Information["PERSONAL INFORMATION"]["Skills"]
First = Information["PERSONAL INFORMATION"]["1"]
Second = Information["PERSONAL INFORMATION"]["2"]
Third = Information["PERSONAL INFORMATION"]["3"]
Fourth = Information["PERSONAL INFORMATION"]["4"]
Fifth = Information["PERSONAL INFORMATION"]["5"]
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
Achievements = Information["PERSONAL INFORMATION"]["Achievements"]
FirstQ = Information["PERSONAL INFORMATION"]["01"]
SecondQ = Information["PERSONAL INFORMATION"]["02"]
ThirdQ = Information["PERSONAL INFORMATION"]["03"]

pdf = FPDF('p', 'mm', 'Letter')
pdf.add_page()
pdf.set_font('times', 'B', 30)
pdf.cell(100, 15, 'JUSTEN L. NICANOR', ln=True)
pdf.set_font('times', '', 15)
pdf.cell(50, 5, Adresss, ln=True)
pdf.cell(50, 5, Contact, ln=True)
pdf.cell(50, 5, Email, ln=True)
pdf.set_font('times', 'B', 20)
pdf.cell(50, 15, Skills, ln=True)
pdf.set_font('times', '', 15)
pdf.cell(50, 6, First, ln=True)
pdf.cell(50, 6, Second, ln=True)
pdf.cell(50, 6, Third, ln=True)
pdf.cell(50, 6, Fourth, ln=True)
pdf.cell(50, 6, Fifth, ln=True)
pdf.set_font('times', 'B', 20)
pdf.cell(50, 15, Personal, ln=True)
pdf.set_font('times', '', 15)
pdf.cell(50, 6, DateofBirth, ln=True)
pdf.cell(50, 6, PlaceofBirth, ln=True)
pdf.cell(50, 6, Gender, ln=True)
pdf.cell(50, 6, CivilStatus, ln=True)
pdf.cell(50, 6, Citizenship, ln=True)
pdf.cell(50, 6, Height, ln=True)
pdf.cell(50, 6, Weight, ln=True)
pdf.cell(50, 6, FathersName, ln=True)
pdf.cell(50, 6, Ocupation, ln=True)
pdf.cell(50, 6, MothersName, ln=True)
pdf.cell(50, 6, Occupation, ln=True)
pdf.cell(50, 6, Address, ln=True)
pdf.set_font('times', 'B', 20)
pdf.cell(50, 15, Educational, ln=True)
pdf.set_font('times', '', 15)
pdf.cell(50, 6, Elem, ln=True)
pdf.cell(50, 6, Junior, ln=True)
pdf.cell(50, 6, Senior, ln=True)
pdf.cell(50, 6, College, ln=True)
pdf.cell(50, 6, Course, ln=True)
pdf.set_font('times', 'B', 20)
pdf.cell(50, 15, Achievements, ln=True)
pdf.set_font('times', '', 15)
pdf.cell(50, 6, FirstQ, ln=True)
pdf.cell(50, 6, SecondQ, ln=True)
pdf.cell(50, 6, ThirdQ, ln=True)


pdf.output('NICANOR_JUSTEN.pdf')
