#!/usr/bin/python3
""" Define the Square module
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class

    Args:
        Rectangle (_type_): _description_
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initilizing instances (class constructor)

        Args:
            size (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Custom printing of Square instances

        Returns:
            _type_: _description_
        """
        print(f"")
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Setter of size

        Returns:
            _type_: _description_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Getter o size

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """assigns each argument to its correspondant attribute
        """
        att = ['id', 'size', 'x', 'y']
        if args is not None and args != ():
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square

        Returns:
            _type_: _description_
        """
        dict_rec = {"id": self.id, "size": self.size,
                    "x": self.x, "y": self.y}
        return dict_rec
