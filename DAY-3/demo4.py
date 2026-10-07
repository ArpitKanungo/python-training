fobj = open("emp.csv", "r")
total = 0
L = fobj.readlines()

for var in L:
    var = var.strip()

for var in L:
    if 'sales' in var:
        var = var.strip()
        eid, name, dept, salary = var.split(",")
        total = total + int(salary)
        print(f"Emp Name is {name.title()}, \t Salary is {salary}, \t Department is {dept.upper()}")

fobj.close()
print("Total salary of sales department:", total)

print("*" * 40)
print(f"Sum of sales department salaries: {total}")
print("-" * 35)