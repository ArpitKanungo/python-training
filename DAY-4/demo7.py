'''
Method overriding in Python
-----------------------------
Method overriding is a fundamental pillar of Runtime Polymorphism in object-oriented programming. 
It allows a child class to provide a specific, customized implementation of a method that it has 
already inherited from its parent class
'''


class Animal:
    def speak(self):
        print("Animal makes Sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak() # Invokes parent class of Dog to avoid method overriding


# Creating objects

#obj = Animal()
#obj.speak()

obj1 = Dog()
obj1.speak()