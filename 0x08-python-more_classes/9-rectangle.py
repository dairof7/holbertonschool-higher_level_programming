#!/usr/bin/python3
""" this module create the class Reactangle"""


class Rectangle:
    """ Class Rectangle with constuctor and other methods
    Arg
        number_of_instances
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class Rectangle
        Arg
            width: width of the rectangle
            height: height of the retangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter function of width
        Returns:
            width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function of attribute width
        Args:
            value: value for __width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        getter function of height
        Returns:
            height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function of attribute height
        Args:
            value: value for __height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of a Rectangle
        Returns:
            The area of the Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate the perimeter of a Rectangle
        Returns:
            The perimeter of the Rectangle
        """
        if self.__height == 0 or self.__height == 0:
            return 0
        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        """Create the string of the rectangle
        Returns:
        The string of the rectangle"""

        string = ""
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            for j in range(self.__height):
                for i in range(self.__width):
                    string += str(self.print_symbol)
                if j < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """Create the string of the rectangle
        Returns:
        The string of the rectangle"""
        return "Rectangle({:d},{:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete a instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """verify which one is bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """create a new instance with a rectangle"""
        return Rectangle(size, size)
