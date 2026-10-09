class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self):
        self.engine_obj = Engine() # Has-A relationship: Car Has-A Engine
    def driving(self):
        self.engine_obj.start()
        print("Car is being driven")

obj = Car()
obj.driving()