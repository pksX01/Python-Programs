class Employee:
    empCount = 0 #class variable and it's value will be shared across all instances. It can be accessed as Employee.empCount from either inside or outside the class

    def __init__(self,name,salary):  #constructor
        self.name=name;
        self.salary=salary
        Employee.empCount += 1

    def displayCount(self): #first argument needs to be self and Python will pass it
        print("Total Employee %d"%Employee.empCount)

    def displayEmployee(self):
        print("Name : ",self.name)
        print("Salary: ",self.salary)

#create objects
emp1 = Employee("Vinay",2000) 
emp2 = Employee("Akash",4000)

#display objects

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d"%Employee.empCount)

#you can add remove or modify attributes at any time
emp1.age=7
emp1.age=8
#del emp1.age


#show following on shell
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
#delattr(empl, 'age')   # Delete attribute 'age'

print ("Employee.__doc__:", Employee.__doc__) #Class documentation string or none, if undefined.
print ("Employee.__name__:", Employee.__name__)#class name
print ("Employee.__module__:", Employee.__module__)#Module name in which the class is defined.
                                                   #This attribute is "__main__" in interactive mode
print ("Employee.__bases__:", Employee.__bases__)#A possibly empty tuple containing the base classes,
                                                  #in the order of their occurrence in the base class list.


print ("Employee.__dict__:", Employee.__dict__)#Dictionary containing the class's namespace.
