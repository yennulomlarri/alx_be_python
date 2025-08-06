# oop/polymorphism_demo.py
import math

class Shape:
    """
    Base class for geometric shapes.
    Defines a common interface for calculating the area.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        """Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base method to calculate the area of the rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, inheriting from Shape."""
    def __init__(self, radius):
        """Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """
        Overrides the base method to calculate the area of the circle.
        """
        return math.pi * (self.radius ** 2)