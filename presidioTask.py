import sqlite3

# for a decent representation of table

try:
    from prettytable import PrettyTable

    print("PrettyTable is installed.")
except ImportError:
    print("PrettyTable is not installed.")


# for entering the Employee records into the database's table named EMPLOYEES

def insertIntoTable(mycursor, mydb):
    mycursor.execute('''CREATE TABLE IF NOT EXISTS employees(emp_id INTEGER PRIMARY KEY,emp_name VARCHAR,age INTEGER, 
    date_of_birth DATE, salary REAL, emp_dept VARCHAR)''')
    print("Enter Employee id")
    emp_id = int(input())
    print("Enter Employee Name")
    emp_name = input()
    print("Enter the age of Employee")
    age = int(input())
    print("Enter DOB of the Employee")
    dob = input()
    print("Enter the salary of Employee")
    salary = float(input())
    print("Enter the department of Employee")
    emp_dept = input()
    employee_data = (emp_id, emp_name, age, dob, salary, emp_dept)
    mycursor.execute(
        'INSERT INTO employees(emp_id, emp_name, age, date_of_birth, salary, emp_dept) VALUES(?,?,?,?,?,?)',
        employee_data)
    mydb.commit()


# for updating the records in the EMPLOYEES table

def updateEmployeeDetails(mycursor, mydb):
    print("What do you want to update in the Employee record:")
    print("1.Employee Name \n2.Employee Age \n3.Employee DOB \n4.Employee Salary \n5.Employee Department")
    ch = int(input())

    if (ch == 1):
        print("Enter the Employee Id whose name has to be Updated")
        emp_id = int(input())
        print("Enter Employee's Updated Name")
        emp_name = input()
        mycursor.execute("UPDATE employees SET emp_name = ? WHERE emp_id = ?", (emp_name, emp_id))
        mydb.commit()

    elif (ch == 2):
        print("Enter the Employee Id whose Age has to be Updated")
        emp_id = int(input())
        print("Enter Employee's Updated Age")
        age = int(input())
        mycursor.execute("UPDATE employees SET age = ? WHERE emp_id = ?", (age, emp_id))
        mydb.commit()

    elif (ch == 3):
        print("Enter the Employee Id whose DOB has to be Updated")
        emp_id = int(input())
        print("Enter Employee's Updated DOB")
        dob = input()
        mycursor.execute("UPDATE employees SET date_of_birth = ? WHERE emp_id = ?", (dob, emp_id))
        mydb.commit()

    elif (ch == 4):
        print("Enter the Employee Id whose salary has to be Updated")
        emp_id = int(input())
        print("Enter Employee's Updated salary")
        salary = float(input())
        mycursor.execute("UPDATE employees SET salary = ? WHERE emp_id = ?", (salary, emp_id))
        mydb.commit()

    elif (ch == 5):
        print("Enter the Employee Id whose Department has to be Updated")
        emp_id = int(input())
        print("Enter Employee's Updated Department")
        dept = input()
        mycursor.execute("UPDATE employees SET emp_dept = ? WHERE emp_id = ?", (dept, emp_id))
        mydb.commit()

    else:
        print("Invalid Choice")

    print("Employee Records Updated Successfully")


# for printing all the attributes of employee table

def printEmployeeDetails(t):
    table = PrettyTable(["emp_id", "emp_name", "age", "dob", "salary", "emp_dept"])
    for i in t:
        table.add_row(i)
    print(table)


# def printEmployeeDetails(t):
#     print("emp_id\temp_name\tage\tdob\tsalary\temp_dept")
#     for i in t:
#         for j in i:
#             print(j, end="\t")
#         print()

def showAllEmployees(mycursor):
    mycursor.execute('SELECT * FROM employees')
    t = mycursor.fetchall()
    printEmployeeDetails(t)


# for searching employee records based on different criteria

def searchEmployee(mycursor):
    print("How do you want to search an Employee record:")
    print("1.Using Employee Id \n2.Using Employee Name \n3.Using Department")
    ch = int(input())

    if (ch == 1):
        print("Enter Employee Id")
        emp_id = int(input())
        mycursor.execute('SELECT * FROM employees WHERE emp_id = ?', (emp_id,))
        t = mycursor.fetchall()
        printEmployeeDetails(t)

    elif (ch == 2):
        print("Enter Employee Name")
        emp_name = input()
        mycursor.execute('SELECT * FROM employees WHERE emp_name = ?', (emp_name,))
        t = mycursor.fetchall()
        printEmployeeDetails(t)

    elif (ch == 3):
        print("Enter Department")
        emp_dept = input()
        mycursor.execute('SELECT * FROM employees WHERE emp_dept = ?', (emp_dept,))
        t = mycursor.fetchall()
        printEmployeeDetails(t)

    else:
        print("Invalid Choice")


# for printing all the employees working in the company with their respective employee ID

def printEmployees(t, emp_id, emp_name):
    table = PrettyTable([emp_id, emp_name])
    for i in t:
        table.add_row(i)
    print(table)


def employeesInCompany(mycursor):
    mycursor.execute("SELECT emp_id, emp_name FROM employees")
    t = mycursor.fetchall()
    printEmployees(t, "ID", "Employee Name")


# for printing average salary of respective departments

def printDeptAvg(t, dept, avg):
    table = PrettyTable([dept, avg])
    for i in t:
        table.add_row(i)
    print(table)


def averageSalaryInDept(mycursor):
    mycursor.execute("SELECT emp_dept AS Department, AVG(salary) AS Avg_salary FROM employees GROUP BY emp_dept")
    t = mycursor.fetchall()
    printDeptAvg(t, "Department", "Avg_salary")


# for printing overall average salary of all the employees in the company

def printAverage(t, avg):
    table = PrettyTable([avg])
    for i in t:
        table.add_row(i)
    print(table)


def averageSalaryOfEmployee(mycursor):
    mycursor.execute("SELECT AVG(salary) AS avg_salary FROM employees")
    t = mycursor.fetchall()
    printAverage(t, "Average Salary")


# for deleting the records of the employee based on its employee Id

def deleteEmployeeRecord(mycursor, mydb):
    print("Enter the Employee Id to delete the records")
    reg = int(input())
    mycursor.execute("DELETE FROM employees WHERE emp_id = ?", (reg,))
    mydb.commit()
    print("The Record with Employee id = ", reg, " is Deleted successfully")


def main():
    mydb = sqlite3.connect('Employeedatabase.db')
    mycursor = mydb.cursor()
    print('Database Connected Successfully')

    while (True):
        print("1-Create an Employee Record")
        print("2-Update an Employee Record")
        print("3-Show all the Employee Records")
        print("4-Show all Employees in Company")
        print("5-Search for a particular Employee Record")
        print("6-Delete an Employee Record")
        print("7-Average salary of the Department")
        print("8-Average salary of the Employee in the Company")
        print("Enter 0 to exit")
        ch = int(input())

        if (ch == 1):
            insertIntoTable(mycursor, mydb)
        elif (ch == 2):
            updateEmployeeDetails(mycursor, mydb)
        elif (ch == 3):
            showAllEmployees(mycursor)
        elif (ch == 4):
            employeesInCompany(mycursor)
        elif (ch == 5):
            searchEmployee(mycursor)
        elif (ch == 6):
            deleteEmployeeRecord(mycursor, mydb)
        elif (ch == 7):
            averageSalaryInDept(mycursor)
        elif (ch == 8):
            averageSalaryOfEmployee(mycursor)
        else:
            break
    mydb.commit()
    mydb.close()


if __name__ == '__main__':
    main()
