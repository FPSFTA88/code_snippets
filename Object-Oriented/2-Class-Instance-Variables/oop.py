class Employee:

    raise_amount = 1.04 
    num_of_emp = 0

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emp += 1

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.fullname())
emp_1.raise_amount = 1.10 
print(emp_1.__dict__)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.num_of_emp)
