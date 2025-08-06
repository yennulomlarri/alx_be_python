# oop/class_static_methods_demo.py

class Calculator:
    """
    A Calculator class to showcase static and class methods.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method to add two numbers.
        It does not have access to class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method to multiply two numbers.
        It has access to class-level attributes via the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b