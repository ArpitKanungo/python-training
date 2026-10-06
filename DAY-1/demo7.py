'''
Write a python program 
- read a employee details (Name,Age,Cost) from <STDIN>
- use print() to display employee details.
- calculate employee basic salary with 18% tax and display the tax
- calculate tax + basic salary and display the total salary (including tax)
'''
eloginStatus = True

ename = input("Enter employee name: ")

eage = input(f"Enter {ename} age: ")

ecost = input(f"Enter {ename} basic salary: ")

tax = float(ecost) * 0.18 

total_salary = tax + float(ecost)

print(f'''Employee Name:{ename}
---------------------------------------
{ename}'s Age is: {eage}
---------------------------------------
{ename}'s Basic Salary is: {ecost}
---------------------------------------
{ename}'s Login Status is: {eloginStatus}
-----------------------------------------
The tax on {ecost} is: {tax}
-----------------------------------------
The total salary is: {total_salary}
----------------------------------------''')