#!/usr/bin/python3

"""Module for Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter of x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter of y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def display(self):
        """
        Print the square checking position
        """
        if self.__width == 0 and self.__height == 0:
            print("")
        else:
            print("\n" * self.__y, end="")
            for i in range(self.__height):
                print(" " * self.__x, end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """return a string"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update attributes"""
        if args is not () and args is not None:
            listname = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, listname[i], value)
        else:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    setattr(self, name, value)

    def to_dictionary(self):
        """Dictionary"""
        new_dictionary = {}
        for key, value in self.__dict__.items():
            new_dictionary[key.split("__")[-1]] = value
        return new_dictionary
