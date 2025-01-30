# Problem 1
import math

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length, side_length)
#------------------------------------------------------------------------------------------------
# Problem 2

class square:
    def __init__(self, side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length ** 2  
    
class Cube(square):
    def __init__(self, side_length):
        super().__init__(side_length)

    def surface_area(self):
        return 6 * self.area()

    def volume(self):
        return self.side_length ** 3
#------------------------------------------------------------------------------------------------
# Problem 3

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius**2
    
class Sphere(Circle):
    def __init__(self,radius):
        super().__init__(radius)

    def Surface_Area(self):
        return 4 * super().Area()
    
    def Volume(self):
        return (4/3) * math.pi * self.radius**3
    
#------------------------------------------------------------------------------------------------
# Problem 4
import math
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    
class Point3D(Point2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def distance_from_origin3D(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    

#------------------------------------------------------------------------------------------------
# Problem 5

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_worked, hourly_rate):
        super().__init__(id, name)
        self.hourly_worked = hourly_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hourly_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission

# ------------------------------------------------------------------------------------------------