# Q1. Extract "code" from the given string
S = "Sample python code"
print(S[-4:])

# Q2. Given a string S = "x:y:z"
S = "x:y:z"
# (i) Display last 2 characters of the string
print(S[-2:])
# (ii) Calculate string total length
print(len(S))

# Q3. Remove \n, \t and : chars from the strings
S1 = "root:x:bin:bash\n"
S2 = "root:x:bin:bash\t"
S3 = "root:"

print(S1.replace("\n", "").replace(":", ""))
print(S2.replace("\t", "").replace(":", ""))
print(S3.replace(":", ""))
