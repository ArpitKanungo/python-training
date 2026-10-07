''' 
Write a program :
(i) Create an empty list
(ii) Display number of elements in the list # use len() function
(iii) Use while loop - limit is 5
       -> Read a hostname from user input
       -> Append the hsotname to the list
(iv) display the number of elements in the list # use len() function
(v) Use for loop to iterate the list 
(vi) Read a hostname from user input
(vii) Test input hostname is existing or not in the list, if existing then modify it else add the hostname to the list
(viii) Display the final list of hostnames using for loop
'''

hosts = []

print(len(hosts))

counter = 5
while counter > 0:
    hostname = input("Enter a hostname: ")
    hosts.append(hostname)
    counter -= 1

print(len(hosts))

for i in hosts:
    print(f"{i}\n")

hostName = input("Enter a hostname to check: ")
if hostName in hosts:
    index = hosts.index(hostName)
    newHostName = input(f"Hostname '{hostName}' exists. Enter new hostname to replace it: ")
    hosts[index] = newHostName
else:
    hosts.append(hostName)

print("Final list of hostnames:")
for i in hosts:
    print(f"{i}\n")
