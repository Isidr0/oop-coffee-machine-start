class Employee:

    raise_amt = 1.04

# double underscores are called dunder. do this init is dunder init.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

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

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))


# print(len(emp_1))
#
# print(emp_1)
#
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# the dunder add method is what happens in the background when you use a plus sign
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))