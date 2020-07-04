"""
Inheritance in Python
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

    def print_emp(self):
        for emp in self.employees:
            print('--->', emp.fullname())


#Inheritage form the Employee class
class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

#Inheritage form the Employee class
class Manager(Employee):

    def __init__(self, first, last, pay, employees =None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees

    def add_empl(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)



emp1 = Employee('Sam', 'mast', 5000)
emp2 = Employee('Jon', 'reh', 4000)

print(emp1.email)
print(emp2.email)

dev1 = Developer('Rani', 'Lad', 554545, 'Python')
dev2 = Developer('Gita', 'alex', 8000, 'JAVA')

print(dev1.email)
print(dev2.email)
print(dev1.pay)
print(dev1.prog_lang)


manage1 = Manager('sam', 'mast', 90000, [dev1])
print(manage1.email)
print(manage1.print_emp())