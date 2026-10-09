print("Welcome")
print("Test-1")
print("Test-2")
print("Test-3")
try:
    print("Test-4")
except Exception as e:
    print("An error occurred:", e)
else:
    print("Test-4 executed successfully")
finally:
    print("Test-4 try-except block finished")
for var in range(5):
    print(var)
    print('-'*20)
print("Loop finished")
total = 10 + 20
print("Total:", total)