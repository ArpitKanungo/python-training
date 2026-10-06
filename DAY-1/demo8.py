'''
Write a python program:
- Read a port number from <STDIN>

- Test for the input port number range is 5001-5999
	- initialize app name is Flask
	- initialize app name is WebApp

- Display - App name and Running port number
'''

port = int(input("Enter port number: "))

if 5000 < port < 6000:
	appName = "Flask"
else:
	appName = "WebApp"

print(f"The application is running on port {port} with app name {appName}")