with open('r1.log', 'r') as fobj:
    with open('r4.log', 'w') as wobj:
        for line in fobj.readlines():
            wobj.write(line)

fobj.close()
wobj.close()