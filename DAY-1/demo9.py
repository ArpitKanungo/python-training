'''
Write a python program:
- Read application name from <STDIN>

- Test for the input using membership test flask is running
   -> The port number is 5000 else it is 8080
- Display - App name and Running port number
'''

appName = input("Enter application name: ")

if appName in 'crm application running in flask web app':
    port = 5000
else:
    port = 8080


print(f"The application is running on port {port} with app name {appName}")