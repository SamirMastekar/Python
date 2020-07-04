"""
Special Method:-
Magic methods in Python are the special methods which add "magic" to your class.
Magic methods are not meant to be invoked directly by you, but the invocation 
happens internally from the class on a certain action. 
For example, when you add two numbers using the + operator, internally, the __add__() method 
will be called.

1) __repr__():-

2) __str__():- 

"""
class Employee:


    #Constructor of Class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@seimens.com'

    #Method who return  fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay *1.5)

    def __repr__(self):        #To display the object of class
        return "Employee('{}, '{}')".format(self.first, self.last, self.pay)

    def __str__(self):         #Used to string representation of the object
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):   #'+' Operator overloader
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Employee('samir', 'mast', 1500)      #Instance of class
emp2 = Employee('samir', 'mast', 2000)

print(emp1 + emp2)
print(len(emp1))