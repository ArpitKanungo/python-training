'''
Modify ATM pin test
1 . Create a pin_hostory.log file - append mode
2. Use ATM pin number validation - maximum attempt limit 3
    -> Valid pin -> update pin details to pin_history.log - Success - <count> + Date/time <== time.ctime()
    -> Invalid pin -> update pin details user_input_pin + Date/time to pin_history.log - Failure - <count> + Date/time <== time.ctime()
3. Pin is blocked - update pin details to pin_history.log - Blocked - Date/time <== time.ctime()
4. Create a new function - pin_test()
'''
import time

default_pin = "1234"

def enter_user_pin():
    return input("Enter your ATM pin: ")

def validate_pin(pin, correct_pin):
    if not pin or len(pin) != 4 or not pin.isdigit():
        print("Invalid pin format. Pin must be 4 digits.")
        return False
    return pin == correct_pin

def pin_test():
    pin_history_file = 'pin_history.log'
    correct_pin = input("Set your ATM pin (default is 1234): ")
    if not correct_pin or len(correct_pin) != 4 or not correct_pin.isdigit():
        print("Invalid pin format. Using default pin.")
        correct_pin = default_pin
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        user_input_pin = enter_user_pin()
        if validate_pin(user_input_pin, correct_pin):
            with open(pin_history_file, 'a') as f:
                f.write(f"Success - {attempts + 1} - date/time - {time.ctime()}\n")
            print("Pin validated successfully.")
            return True
        else:
            attempts += 1
            with open(pin_history_file, 'a') as f:
                f.write(f"Failure - {attempts} - date/time - {time.ctime()}\n")
            print("Invalid pin.")
    with open(pin_history_file, 'a') as f:
        f.write(f"Blocked - date/time - {time.ctime()}\n")
    print("Pin is blocked.")
    return False

pin_test()
