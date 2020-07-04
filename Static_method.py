"""
Static  Method in Class

1) Regular method takes automatically takes instance of
first argument "self"

2) Class  method clss "cls" as first argument.

3) Class method is act like constructor

4) Static do not data to class 

5) It behave like normal method

"""

class Employee:
    raise_amt = 1.5
    
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
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def constructorfromSplitString(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_working(day):
        if(day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True
        
emp1 = Employee('samir', 'mast', 1500)
emp2 = Employee('sanket', 'Gavade', 10000)
        
print(emp1)
print(emp2)

Employee.set_raise(2.5)   #It setting the all instances of class

print('{} {} {}'.format(Employee.raise_amt,  emp1.raise_amt, emp2.raise_amt))

emp1.set_raise(3.5)      #It also called as Constructor

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

#Assign data to calss from the string
emp_str='SAM-MASTEKAR-50000'
new_emp = Employee.constructorfromSplitString(emp_str)
print(new_emp.email)
print(new_emp.pay)
        
#Checking the static method
import datetime
my_date = datetime.date(2020, 6, 30)
print(Employee.is_working(my_date))
        
    