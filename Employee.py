class Employee:
    def __init__(self,firstName,lastName,contact):
        self.firstName = firstName
        self.lastName = lastName
        self.contact = contact

    def getFullName(self):
        return self.firstName+" "+self.lastName
emp_1 = Employee('ZAKIR', 'HASAN', 123)
#emp_2 = Employee()

print(emp_1.lastName)
print(emp_1.getFullName())