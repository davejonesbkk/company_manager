""""
Company Manager - Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay is calculated differently, research a bit about it. After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees.
"""

class Employee:
	def __init__(self, firstname, lastname, age, sex, dob):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age 
		self.sex = sex
		self.dob = dob

	


class Hourly(Employee):
	def __init__(self, firstname, lastname, age, sex, dob, rate, hours):
		self.rate = rate
		self.hours = hours
		super().__init__(firstname, lastname, age, sex, dob)

	def __str__(self):
		return "{} {}\nAge: {}\nSex: {}".format(self.firstname, self.lastname, self.age, 
			self.sex, self.dob, self.rate, self.hours)





class Salaried(Employee):
	def __init__(self, firstname, lastname, age, sex, dob, salary, contract):
		self.salary = salary
		self.contract = contract
		super().__init__(firstname, lastname, age, sex, dob)

	def __str__(self):
		return "{} {}\nAge: {}\nSex: {}\nDOB: {}\nSalary: {}".format(self.firstname, self.lastname, self.age, 
			self.sex, self.dob, self.salary, self.contract)



hourlystaff1 = Hourly('Bob', 'Foo', '23', 'M', '12/1/1980', '$15', '30')

salariedstaff1 = Salaried('Jane', 'Bar', '34', 'F', '1/1/1987', '$40,000', 'yes')

print(hourlystaff1)

print('---------')

print(salariedstaff1)






