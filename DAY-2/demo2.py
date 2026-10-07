'''
Given List
Emp = ['101,john,sales,1000', '102,ram,prod,2000', '103,raju,hr,3000', '104,bibu,sales,4000']
-> Iterate the list.
-> Split each employee record into individual fields using ',' as the delimiter.
-> Display empName in the title case and emp department in uppercase.
-> Calculate the sum of emp salary and display the total salary.
'''
Emp = ['101,john,sales,1000', '102,ram,prod,2000', '103,raju,hr,3000', '104,bibu,sales,4000']
totalSalary = 0
for employee in Emp:
    empId, empName, empDept, empSalary = employee.split(',')
    print(f"Employee Name: {empName.title()}, Department: {empDept.upper()}")
    totalSalary += int(empSalary)
print(f"Total Salary: {totalSalary}")