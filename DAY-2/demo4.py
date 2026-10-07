'''
Write a program :
(i) Create an empty dictionary
(ii) Display number of elements in the dictionary # use len() function
(iii) Use while loop - limit is 5
  -> Read a hostname and IP address from user input
  -> Add the hostname and IP address to the dictionary
(iv) display the number of elements in the dictionary # use len() function
(v) Use for loop to iterate the dictionary
(vi) Read a hostname from user input
(vii) Test input hostname is existing or not in the dictionary, if existing then update it else display that it does not exist
(viii) Display the final dictionary
'''

hosts = {}
print(f"Initial number of items: {len(hosts)}")
count = 0

while count < 5:
  hostname = input("Enter hostname: ").strip()
  ip_address = input("Enter IP address: ").strip()
  hosts[hostname] = ip_address
  count += 1

print(f"Number of items after input: {len(hosts)}")

for hostName, ip_address in hosts.items():
  print(f"{hostName} -> {ip_address}")

searchHostName = input("Enter hostname to update: ").strip()
if searchHostName in hosts:
  hosts[searchHostName] = "127.0.0.1"
  print(f"Updated {searchHostName} to 127.0.0.1")
else:
  print(f"{searchHostName} does not exist")

print("Final dictionary:")
print(hosts)
