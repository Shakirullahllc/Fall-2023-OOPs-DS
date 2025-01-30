# Problem 1
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Cube(Square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def surface_area(self):
        return 6 * super().area()

    def volume(self):
        return self.width ** 3

#---------------------------------------------------------------------------------------------------
# Problem 2

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        pass

    def work(self, hours):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

    def work(self, hours):
        print(f"Salaried employee {self.name} worked {hours} hours.")


class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_worked, hourly_rate):
        super().__init__(id, name)
        self.hourly_worked = hourly_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hourly_worked

    def work(self, hours):
        print(f"Hourly employee {self.name} worked for {hours} hours.")


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission

    def work(self, hours):
        print(f"Commission employee {self.name} made sales calls for {hours} hours.")


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"Manager {self.name} is managing for {hours} hours.")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"Secretary {self.name} is organizing paperwork for {hours} hours.")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"Salesperson {self.name} is making sales calls for {hours} hours.")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"Factory worker {self.name} is manufacturing products for {hours} hours.")
#---------------------------------------------------------------------------------------------------