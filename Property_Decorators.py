"""
Property Decorators- Getters, Setters and Deleters
Explaination:-
Defin and access the attribute like other programming langague
like C++, java etc.
"""
class Employee:


    #Constructor of Class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    #Method who return  fullname
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property  #Getter Access to attribute of class
    def email(self):
        return '{} {}@gmail.com'.format(self.first, self.last)

    @fullname.setter #Setting the value of attribute of class
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter #Delete the attribute of class
    def fullname(self):
        print('Delete Name of class')
        self.first = None
        self.last = None

emp1 = Employee('samir', 'mast', 1500)      #Instance of class

emp1.fullname= 'Samir Mastekar'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname