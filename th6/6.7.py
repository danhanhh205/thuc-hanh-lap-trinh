print("Nguyễn Danh Ánh")
print("235752021610023")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

circle = Circle(6)

area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("Diện tích hình tròn:", area)
print("Chu vi hình tròn:", perimeter)
