"""
Syllabus:-
1) Class
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

emp1 = Employee('samir', 'mast', 1500)      #Instance of class
print(emp1)
print(emp1.email)        #Access the attribute of class
print('{} {}'.format(emp1.first, emp1.last))

emp2 = Employee('sanket', 'Gavade', 40000)
print(emp2.fullname())

#print(Employee.fullname()) ---> Error:- "TypeError: fullname() missing 1 required positional argument: 'self'"
#print(Employee.fullname(self))---> Error:- "NameError: name 'self' is not defined"

















