#Python Object-Oriented Programming


class Employee:
    # pass #skips empty class so you don't get an error message

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay): #think of as initialize method or other languages call it constructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# video 2: class variables. should be used for something that won't change between class instances.
# this example is a standard pay raise that applies to all employees


print(Employee.num_of_employees)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_employees)

# print(Employee.__dict__)

# assigning the class attribute to the instance creates it in the instance's namespace
# # this can effect methods that reference self vs the class (Employee in this case). self will use the instance variable.
# emp_1.raise_amount = 1.05
#
# print(emp_1.__dict__)
#
# # class variable can be accessed from both the class itself and the instance
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount
# Employee.raise_amount

# video 1: classes and instances
# #unique instances of employee class
# emp_1 = Employee('Corey', 'Schafer', 50000) #emp_1 replaces self in class instance.
# # so it does the same thing as variables below
# emp_2 = Employee('Test', 'User', 60000)
#
# # print(emp_1)
# # print(emp_2)
#
# # class instance assignments replace this
# # emp_1.first = 'Corey'
# # emp_1.last = 'Schafer'
# # emp_1.email = 'Corey.Schafer@company.com'
# # emp_1.pay = 50000
# #
# # emp_2.first = 'Test'
# # emp_2.last = 'User'
# # emp_2.email = 'Test.User@company.com'
# # emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)
#
# # the line below formats the employee full name with first and last. you can use a class instance to do this.
# # print('{} {}'.format(emp_1.first, emp_1.last))
# # print(emp_1.fullname())
# # print(emp_2.fullname())
# # the line below does the same thing as above.
# # the line above passes instance self automatically. the line below passes it manually because it doesn't know which
# # instance you want to use
# print(Employee.fullname(emp_1))