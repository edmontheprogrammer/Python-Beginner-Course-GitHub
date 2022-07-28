# Define a new type called Person
# - name attriubte 
# = talk() method 

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self, message):
        self.message = message
        return message


john = Person('john')
print(john.name)
message = "Hi, how are you?"
print(john.talk(message))