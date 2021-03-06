"""Import csv, PyPDF2, and pandas to create
dataframe, pdf, read csv and file functions"""

import main as mn
#from main import *
import csv
import os
from fpdf import FPDF
import PyPDF2
from PyPDF2 import PdfFileMerger
import pandas as pd

merge = PdfFileMerger()

#functions to read CSV files so as to test them if they are empty
def read_student_csv():
    df = pd.read_csv('pdfs/students_table.csv')  # or pd.read_excel(filename) for xls file
    return df.empty  # will return True if the dataframe is empty or False if not.
def read_teachers_csv():
    df = pd.read_csv('pdfs/teacher_table.csv')  # or pd.read_excel(filename) for xls file
    return df.empty  # will return True if the dataframe is empty or False if not.

def read_school_csv():
    df = pd.read_csv('pdfs/school_table.csv')  # or pd.read_excel(filename) for xls file
    return df.all()  # will return True if the dataframe is empty or False if not.

"""we convert tables from the database to csv 
and then read data from the csv to pdf file"""
def create_pdf(n):

    # checks if user selected 1 which is for the student table
    if n == 1:
        mn.student_table()
        with open('pdfs/students_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Students Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.cell(col_width, th, row[7], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('student.pdf', 'F')

    # checks if user selected 2 which is for the teachers table
    if n == 2:
        mn.teachers_table()
        with open('pdfs/teacher_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Teachers Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 12)

                col_width = page_width / 5

                pdf.ln(1)

                th = pdf.font_size

                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('teachers.pdf', 'F')

    # checks if user selected 3 which is for the school table
    if n == 3:
        mn.schools_table()
        with open('pdfs/school_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

                # create pages
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w -(-2) * pdf.l_margin

                # setting the font color, size and also data
                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Schools Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                # set the size and specification of the pdf page
                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('school.pdf', 'F')

    # checks if user selected 4 which convert each table to csv which are then converted to pdfs
    if n == 4:
        mn.student_table()
        with open('pdfs/students_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                # setting the font color, size and also data
                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Students Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                # set the size and specification of the pdf page
                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.cell(col_width, th, row[7], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('student.pdf', 'F')

        # read teachers table then converts it to csv then pdf
        mn.teachers_table()
        with open('pdfs/teacher_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - 2 * pdf.l_margin

                # setting the font color, size and also data
                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Teachers Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 12)

                col_width = page_width / 5

                pdf.ln(1)

                th = pdf.font_size

                # creating columns where the data is written
                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('teachers.pdf', 'F')

        # read school table then converts it to csv then pdf
        mn.schools_table()
        with open('pdfs/school_table.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
                pdf = FPDF()
                pdf.add_page()
                page_width = pdf.w - (-2) * pdf.l_margin

                # setting the font color, size and also data
                pdf.set_font('Times', 'B', 14.0)
                pdf.cell(page_width, 0.0, 'Schools Data', align='C')
                pdf.ln(10)

                pdf.set_font('Courier', '', 8)

                col_width = page_width / 8

                pdf.ln(1)

                th = pdf.font_size

                # creating columns where the data is written
                for row in reader:
                    # print(row)
                    pdf.cell(col_width, th, str(row[0]), border=1)
                    pdf.cell(col_width, th, row[1], border=1)
                    pdf.cell(col_width, th, row[2], border=1)
                    pdf.cell(col_width, th, row[3], border=1)
                    pdf.cell(col_width, th, row[4], border=1)
                    pdf.cell(col_width, th, row[5], border=1)
                    pdf.cell(col_width, th, row[6], border=1)
                    pdf.ln(th)

                pdf.ln(10)

                pdf.set_font('Times', '', 10.0)
                pdf.cell(page_width, 0.0, '- end of report -', align='C')

                pdf.output('school.pdf', 'F')

        # the merge the produced pdf above into one
        for items in os.listdir():
            if items.endswith('.pdf'):
                merge.append(items)
        merge.write("School_DB.pdf")
        merge.close()



def read_pdf(n):
    if n==1:
        # creating a pdf file object
        pdfFileObj = open('student.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
    elif n==2:
        # creating a pdf file object
        pdfFileObj = open('teachers.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()
    elif n==3:
        # creating a pdf file object
        pdfFileObj = open('school.pdf', 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # printing number of pages in pdf file
        print(pdfReader.numPages)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        print(pageObj.extractText())

        # closing the pdf file object
        pdfFileObj.close()

def main():
    n=int(input("enter 1=student.pdf\n 2=teacher.pdf\n 3=school.pdf\n"))
    while n <=3:
        read_pdf(n)
    print("wrong choice")
if __name__ == '__main__':
    main()