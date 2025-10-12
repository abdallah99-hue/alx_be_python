# polymorphism_demo.py
import math

# الفئة الأساسية
class Shape:
    def area(self):
        """This method should be overridden in derived classes"""
        raise NotImplementedError("Subclasses must implement this method")


# الفئة المشتقة: مستطيل
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# الفئة المشتقة: دائرة
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
