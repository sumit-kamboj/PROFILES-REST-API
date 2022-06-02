# def test(d,val):
# 	return dict((k,v) for k,v in d.items())
#
# users = {'Theodore': { 'user': 'Theodore', 'age': 45 },'Roxanne': { 'user': 'Roxanne', 'age': 15 },'Mathew': { 'user': 'Mathew', 'age': 21 },
# }
# orig = {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# print(test(users,15))

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # self.fullname = self.first + ' ' + self.last
        def fullname(self):
            self.fullname = self.first + ' ' + self.last
            return self.fullname

        def applyraise(self):
            self.pay = self.pay * self.raise_amount


e1 = Employee('Rahul', 'Rana', 6000)
e2 = Employee('Rohan', 'Kumar', 7000)
print(e2.pay)
e2.applyraise()
print(e2.pay)
print(Employee.fullname(e1))
print(e1.fullname)