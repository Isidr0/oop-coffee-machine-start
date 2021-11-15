#Python Object-Oriented Programming


class Employee:
    # pass #skips empty class so you don't get an error message

    num_of_employees = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay): #think of as initialize method or other languages call it constructor method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # repr is meant to be an unambiguous representation of an object for other devs
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # str is meant to be a display to an end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # this is a "decorator' that tells the method to receive
    # the class as the first argument instead of the instance.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # this is an alternative constructor for formatting input text
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #use a static method if you don't need to reference an instance or class anywhere in the function.
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# a subclass is created like a normal class. but you enter a class you want to inherit from in the parens.
# the developer class will have all of the attributes and methods of the employee class.
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # passes specified attributes to Employee init method
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) # passes specified attributes to Employee init method
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



# video 2: class variables. should be used for something that won't change between class instances.
# this example is a standard pay raise that applies to all employees


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

str(dev_1)

# help method is useful for determining method resolution order. the order in which python will check classes
# for methods and attributes. it will start at the bottom and work its way up the chain of inheritance.
# print(help(Developer))
#
# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
#
# print(issubclass(Manager, Developer))

# print(mgr_1.email)
# mgr_1.rem_emp(dev_1)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# import datetime
# my_date = datetime.date(2016, 7, 11)
#
# print(Employee.is_workday(my_date))

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"

# splits the string up into three separate arguments
# first, last, pay = emp_str_1.split('-')

# # assign the formatted name and pay to a new instance
# # new_emp_1 = Employee(first, last, pay)
# # this is using the alternative constructor class method to format the hyphenated name
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
#
# # Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

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