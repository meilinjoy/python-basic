#!/usr/bin/python3

from multiprocessing import parent_process


class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print('Name:', self.name, ', Salary:', self.salary)



emp1 = Employee('Zara', 2000)
emp1.displayEmployee()

print ("Total Employee %d" % Employee.empCount)


class Parent:
    parentAttr = 100
    def __init__(self):
        print('Calling parent constructor')
    
    def parentMethod(self):
        print('Calling parent method')
    
    def setParentAttr(self,attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print('Parent Attribute:', Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print('Calling child constructor')
    
    def childMethod(self):
        print('Calling child method')

child1 = Child()
child1.childMethod()
child1.parentMethod()
child1.setParentAttr(300)
child1.getAttr()
        
print(issubclass(Child, Parent))
print(isinstance(child1, Child))



 