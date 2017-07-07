class Employee():
    employeeCount=0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount = Employee.employeeCount + 1
    def countEmployee(self):
        return Employee.employeeCount
    def getEmployeeName(self):
        return self.name
    def getEmployeeSalary(self):
        return self.salary

class Manager(Employee):
    def __init__(self,name,salary):
        super(Manager,self).__init__(name,salary)

employee = Employee('anil',9923489)
print("Employee Name:"+employee.getEmployeeName())
print("Salary:%d"%(employee.getEmployeeSalary()))
print("Number of Employee:%d"%(employee.countEmployee()))
print("\n")

employee = Employee('Sai',12345)
print("Employee Name:"+employee.getEmployeeName())
print("Salary:%d"%(employee.getEmployeeSalary()))
print("Number of Employee:%d"%(employee.countEmployee()))
print("\n")

manager = Manager('Ravi',123456)
print("Employee Name:"+employee.getEmployeeName())
print("Salary:%d"%(employee.getEmployeeSalary()))
print("Number of Employee:%d"%(employee.countEmployee()))
print("\n")