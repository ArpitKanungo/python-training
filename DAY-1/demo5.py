'''
Write a python program:
initialize employee details including name, age, cost, login_status
to variables
using print() to display employee details using f-string and multi-line string

Expected output:
Employee Name: John Doe
-----------------------------------
Employee Age: 30
------------------------
Employee Cost: 50000
------------------------
Employee Login Status: True
-----------------------------------
'''
ename = 'Mr Lee'
eage = 45
ecost = 75000.50
eloginStatus = True

print(f'''Employee Name: {ename}
-----------------------------------
Employee Age: {eage}
------------------------
Employee Cost: {ecost}
------------------------
Employee Login Status: {eloginStatus}
-----------------------------------''')