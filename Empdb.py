#Employee Management System

import tkinter.messagebox
from tkinter import *
import mysql.connector

database = mysql.connector.connect(host='localhost', user='root', db='edb')
cursor = database.cursor()

employee = Tk()
employee.geometry('1100x800')
employee.title('Employee Management System')
employee.configure(bg='gray')

def calculate():
    EmpAnnualSalary.set(EmpSalary.get()*12)

def add():
    id = EmpId.get()
    name = EmpName.get()
    mail = EmpMail.get()
    designation = EmpDesignation.get()
    salary = EmpSalary.get()
    annual_salary = EmpAnnualSalary.get()
    cursor.execute('insert into empdata values(%s,%s,%s,%s,%s,%s)', [id, name, mail, designation, salary, annual_salary])
    database.commit()
    tkinter.messagebox.showinfo('Access Control', 'Details Added')

def view():
    id = EmpId.get()
    cursor.execute('select * from empdata where Employee_Id=%s', [id])
    data = cursor.fetchone()
    if data != None:
        EmpName.set(data[1])
        EmpMail.set(data[2])
        EmpDesignation.set(data[3])
        EmpSalary.set(data[4])
        EmpAnnualSalary.set(data[5])
    else:
        tkinter.messagebox.showwarning('View Data', 'No Data')

def update():
    id = EmpId.get()
    name = EmpName.get()
    mail = EmpMail.get()
    designation = EmpDesignation.get()
    salary = EmpSalary.get()
    annual_salary = EmpAnnualSalary.get()
    cursor.execute('Update empdata set Employee_Name=%s,Employee_Mail=%s,Employee_Designation=%s,Employee_Salary=%s,Employee_Annual_Salary=%s where Employee_Id=%s',
                   [name,mail,designation,salary,annual_salary,id])
    database.commit()
    tkinter.messagebox.showinfo('Employee Entry', 'Details Updated')

def delete():
    id = EmpId.get()
    cursor.execute('delete from empdata where id=%s',[id])
    database.commit()
    tkinter.messagebox.showinfo('Employee Deletion', 'Deleted')

def clear():
    EmpId.set('')
    EmpName.set('')
    EmpMail.set('')
    EmpDesignation.set('')
    EmpSalary.set('')
    EmpAnnualSalary.set('')

def overall():
    global viewpage
    viewpage = Toplevel(employee)
    viewpage.geometry('900x400')
    viewpage.title('Employee Details')
    viewpage.configure(bg='lightblue')
    cursor.execute('select * from empdata')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewpage, text='Emp Id', font=('times new roman',13,'bold'),bg='lightblue').grid(row=0,column=0)
    Label(viewpage, text='Emp Name', font=('times new roman', 13, 'bold'), bg='lightblue').grid(row=0, column=1)
    Label(viewpage, text='Emp Mail', font=('times new roman', 13, 'bold'), bg='lightblue').grid(row=0, column=2)
    Label(viewpage, text='Emp Designation', font=('times new roman', 13, 'bold'), bg='lightblue').grid(row=0, column=3)
    Label(viewpage, text='Emp Salary', font=('times new roman', 13, 'bold'), bg='lightblue').grid(row=0, column=4)
    Label(viewpage, text='Emp AnnualSalary', font=('times new roman', 13, 'bold'), bg='lightblue').grid(row=0, column=5)

    for i in range(rows):
        for j in range(cols):
            s = Entry(viewpage, font=('times new roman',11))
            s.grid(row=i+1,column=j)
            s.insert(END,data[i][j])

Label(employee, text='Employee Management System', font=('times new roman',30,'bold'), bg='white', fg='black').place(x=250,y=30)

EmpId_label = Label(employee, text='EmpId ', font=('times new roman', 30), bg='gray').place(x=80, y=150)
EmpId = IntVar()
EmpId_entry = Entry(employee, textvariable=EmpId, font=('times new roman',30)).place(x=400, y=150)

EmpName_label = Label(employee, text='EmpName ', font=('times new roman', 30), bg='gray').place(x=80, y=230)
EmpName = StringVar()
EmpName_entry = Entry(employee, textvariable=EmpName, font=('times new roman',30)).place(x=400, y=230)

EmpMail_label = Label(employee, text='EmpMail ', font=('times new roman', 30), bg='gray').place(x=80, y=310)
EmpMail = StringVar()
EmpMail_entry = Entry(employee, textvariable=EmpMail, font=('times new roman',30)).place(x=400, y=310)

Empdesignation_label = Label(employee, text='EmpDesignation ', font=('times new roman', 30), bg='gray').place(x=80, y=390)
EmpDesignation = StringVar()
EmpDesignation_entry = Entry(employee, textvariable=EmpDesignation, font=('times new roman',30)).place(x=400, y=390)

EmpSalary_label = Label(employee, text='EmpSalary ', font=('times new roman', 30), bg='gray').place(x=80, y=470)
EmpSalary = IntVar()
EmpSalary_entry = Entry(employee, textvariable=EmpSalary, font=('times new roman',30)).place(x=400, y=470)

EmpAnnualSalary_label = Label(employee, text='EmpAnnualSalary ', font=('times new roman', 30), bg='gray').place(x=80, y=550)
EmpAnnualSalary = IntVar()
EmpAnnualSalary_entry = Entry(employee, textvariable=EmpAnnualSalary, font=('times new roman',30)).place(x=400, y=550)

Button(employee, text='Calculate', font=('times new roman', 20), bg='#5adbb5', fg='red', command=calculate).place(x=850, y=470)

addData = Button(employee, text='Add', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=add).place(x=200, y=620)
viewData = Button(employee, text='View', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=view).place(x=400, y=620)
updateData = Button(employee, text='Update', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=update).place(x=600, y=620)
deleteData = Button(employee, text='Delete', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=delete).place(x=200, y=690)
clearData = Button(employee, text='Clear', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=clear).place(x=400, y=690)
overallData = Button(employee, text='Overall', bg='#5adbb5', fg='red', font=('times new roman', 20), width=10, command=overall).place(x=600, y=690)

employee.mainloop()