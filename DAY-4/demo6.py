class Person:
    def __init__(self, name):
        self.name = name

class Vendor(Person):
    def __init__(self, name, vId):
        super().__init__(name)
        self.vId = vId

obj = Vendor("Zlabs", "V1234")
print(obj.name)
print(obj.vId)