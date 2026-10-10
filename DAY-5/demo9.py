import re

fobj = open('r1.log','r')
for var in fobj:
    var = var.strip()
    if(re.search("^$",var)):
        continue # Ignore the empty lines
    else:
        print(var) # Display the non-empty lines