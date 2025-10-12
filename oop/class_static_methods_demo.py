# class_static_methods_demo.py

class Calculator:
    # سمة الفئة
    calculation_type = "Arithmetic Operations"

    # الطريقة الثابتة
    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers"""
        return a + b

    # طريقة الفئة
    @classmethod
    def multiply(cls, a, b):
        """Prints the class attribute and returns the product"""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
