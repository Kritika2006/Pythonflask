class Firsst_class:
    def __init__(self,name):
        self.name=name
        print(name)

class Second_class():
    def __init__(self,age):
        self.age=age
        print(age)


instance1=Firsst_class("Kritika")
instance=Second_class(25)
arr=[]
arr.append(instance1)
arr.append(instance)
#constructor without call krne pe bhi run krega 
#encapsulation: data hiding     #abstraction: data hiding
#inheritance: parent child relation
#polymorphism: same name different work
#abstraction: data hiding
