# Raise exception
try:
    n = input("Enter a number: ")
    if int(n) > 100:
        raise ValueError("Number is greater than 100")
except Exception as e:
    print("Error:", e, 'for input:', n)
    
class InsufficientBalanceError(Exception): # Exception is the parent class for custom exceptions
    pass

balance = 1000
withdraw = 1500
try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient balance for the withdrawal")
except Exception as e:
    print("Error:", e)

class InvalidAgeError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
except Exception as e:
    print("Error:", e)
    
    
