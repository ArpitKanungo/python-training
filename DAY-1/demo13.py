# Demonstrate any 5 common Python string methods

string = "  python programming is fun and easy!  "

print("Original string:", string)
print("1. strip() ->", string.strip())
print("2. upper() ->", string.upper())
print("3. lower() ->", string.lower())
print("4. replace() ->", string.replace("python", "Python"))
print("5. split() ->", string.strip().split())

# Extra example of find()
print("6. find('programming') ->", string.strip().find("programming"))