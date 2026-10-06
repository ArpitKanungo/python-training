'''
Write a python program:
- read the employee details including name, age, cost, login_status
to variables from <STDIN>
- using print() to display employee details using f-string and multi-line string

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
ename = input('Enter employee name: ')
eage = int(input('Enter employee age: '))
ecost = float(input('Enter employee cost: '))
eloginStatus = input('Enter login status (True/False): ').strip().lower() == 'true'

print(f'''Employee Name: {ename}
-----------------------------------
Employee Age: {eage}
------------------------
Employee Cost: {ecost}
------------------------
Employee Login Status: {eloginStatus}
----------------------------------------''')
