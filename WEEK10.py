from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, firstName, initial, lastName):
        self.firstName = firstName
        self.initial = initial
        self.lastName = lastName

    @abstractmethod
    def getSalary(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, firstName, initial, lastName, monthlySalary):
        super().__init__(firstName, initial, lastName)
        self.monthlySalary = monthlySalary

    def getSalary(self):
        return self.monthlySalary


class HourlyEmployee(Employee):
    def __init__(self, firstName, initial, lastName, hoursWorked, ratePerHour):
        super().__init__(firstName, initial, lastName)
        self.hoursWorked = hoursWorked
        self.ratePerHour = ratePerHour

    def getSalary(self):
        return self.hoursWorked * self.ratePerHour


e1 = SalaryEmployee("Talia", "E", "Auma", 80000)
e2 = HourlyEmployee("Louis", "B", "Liyala", 160, 700)

print("Salary Employee Pay:", e1.getSalary())
print("Hourly Employee Pay:", e2.getSalary())