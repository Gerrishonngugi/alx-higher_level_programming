#!/usr/bin/python3
"""Defines the class Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets/Sets value for rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets value for rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle."""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Print the rectangle with the character #"""
        my_string = ''

        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    my_string += str(self.print_symbol)
                if (i != self.__height - 1):
                    my_string += '\n'
            return my_string
        else:
            return ""

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return ("Rectangle(" + str(self.__width)
                + ", " + str(self.__height) + ")")

    def __del__(self):
        """Deletes rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
