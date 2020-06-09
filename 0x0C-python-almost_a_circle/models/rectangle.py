#!/usr/bin/python3
"""
Module of rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter of width
        """
        return self.__width

    @property
    def height(self):
        """
        Getter of height
        """
        return self.__height

    @property
    def x(self):
        """
        Getter of x
        """
        return self.__x

    @property
    def y(self):
        """
        Getter of y
        """
        return self.__y

    @width.setter
    def width(self, width):
        """
        Setter of width
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """
        Setter of height
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """
        Setter of x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """
        Setter of y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Area of the rectangle
        Returns:
            [int]: area
        """
        return self.__width * self.__height

    def display(self):
        """
        Print rectangle
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        String message
        """
        id = str(self.id)
        width = str(self.__width)
        height = str(self.__height)
        x = str(self.__x)
        y = str(self.__y)
        string = "[Rectangle] (" + id + ") " + x + "/" + y + " - "\
            + width + "/" + height
        return string

    def update(self, *args, **kwargs):
        """
        Assigns an argument
        """
        if args:
            list_args = ["id", "width", "height", "x", "y"]
            for i, j in zip(args, list_args):
                setattr(self, j, i)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a Rectangle
        Returns:
            [dict]: [representation of a rectangle]
        """
        dictionary = {}
        for key, values in self.__dict__.items():  # in var(self).items()
            dictionary[key.split("__")[-1]] = values
        return dictionary
