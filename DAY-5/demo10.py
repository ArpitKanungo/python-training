import re
fname = "emp.csv"

fobj = open(fname,'r')
for var in fobj:
    if (re.search('sales', var, re.I)):
        s = re.sub('pune', 'HYDERABAD', var)
        if 'HYDERABAD' in s:
            print(s.strip())
