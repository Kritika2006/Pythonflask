class FirstClass:
    def __init__(self, name):
        self.name = name
        print(name)
    
    def display(self):
        print(f"Name: {self.name}")

class SecondClass:
    def __init__(self, age):
        self.age = age
        print(age)
    
    def display(self):
        print(f"Age: {self.age}")

instance1 = FirstClass("niyati")
instance2 = SecondClass(19)
arr = []
arr.append(instance1)
arr.append(instance2)

for obj in arr:
    obj.display()