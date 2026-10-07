import time

devices = ['switches', 'routers', 'ethernet', 'rs232']
configData = {'ID': 'A-123', 'app': 'demoApp', 'port': 3030, 'fname': '/etc/app.cfg'}
wobj = open('r2.log', 'w')
for var in devices:
    wobj.write(f"Device name: {var}\n")
wobj.write("-----done------\n")
'''
ID = 'A-123'
app = 'demoApp'
port = 3030
fname = '/etc/app.cfg'
'''
for var in configData:
    wobj.write(f"{var}: {configData[var]}\n")
wobj.write("-----config done------\n")
wobj.write(f"Created on {time.ctime()}\n")

wobj.close()