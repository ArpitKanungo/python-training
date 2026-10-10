'''
s = ['120GB', '500GB', 'GB200', '150Gb', '300gb', '400']

Calculate sum of the size - display total size
'''
import re
s = ['120GB', '500GB', 'GB200', '150Gb', '300gb', '400']

total = 0
for var in s:
    size = re.sub('[A-Za-z]', '', var)
    total += int(size)

print(f' Sum of disk sizes: {total}')
print({re.sub('[A-Za-z]', '', var) for var in s})