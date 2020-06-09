#!/usr/bin/python3

"""Module for Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor Class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return s string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter of size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update attributes"""
        if args is not () and args is not None:
            listname = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, listname[i], value)
        else:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    setattr(self, name, value)

    def to_dictionary(self):
        """Dictionary"""
        new = {}
        for key, value in self.__dict__.items():
            if key.split("__")[-1] == "width" or\
            key.split("__")[-1] == "height":
                new["size"] = value
            else:
                new[key.split("__")[-1]] = value
        return new
