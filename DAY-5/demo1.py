def display():
    '''display list of files'''
    for var in ['f1','f2','f3']:
        print(var)

class Cname:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
    def display(self):
        '''display initialized values'''
        return self.a1,self.a2
#--------------------------------------------------
def connect(dsn):
    class Connection:
        def __init__(self,dsn,dbname,password):
            self.dsn = dsn
            self.dbname = dbname
            self.password = password
        def method1(self):
            return 'Query process'
    obj = Connection(dsn,'sqlite3','password')
    return obj
#---------------------------------------------


#--------------------------------------------------
# file: p1.py
# --------------------
# import demo40
# demo40.display() -> list of files
# ---------------//Direct call

# obj = demo40.Cname('D1','D2')
# obj.display() -> tuple ('D1','D2')


# db_connection_obj = demo40.connect('user:connection')
# db_connection_obj.method1()