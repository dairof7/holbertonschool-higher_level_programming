#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """
    Class that builds a rectangle
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes instance of the rectangle
        Args:
            width: width for __width attribute
            height: height for __height atributte
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """
        Getter function of height
        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function of height
        Args:
            value: value for __height attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """
        Getter function of width
        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function of width
        Args:
            value: value for __width attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Funtion that returns the area of a rectangle instance
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Function that returns the perimeter of a rectangle instance
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return the rectangle in a string representation
        """
        string = ""
        if self.__width != 0 or self.__height != 0:
            for row in range(self.__height):
                for _ in range(self.__width):
                    string += str(self.print_symbol)
                if row < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """
        Returns the string representation of the class instance for
        recreation
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Final process when an instance is killed
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
