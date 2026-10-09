try:
    open("non_existent_file.txt", "r")
except PermissionError as e:
    print("Permission error occurred:", e)
except FileNotFoundError as e:
    print("File not found error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("File operation attempt finished")

print(" ")

try:
    fobj = open("Invalid_File.txt", "r")
except Exception as e:
    import sys
    sys.exc_info()
    print("An unexpected error occurred:", e)