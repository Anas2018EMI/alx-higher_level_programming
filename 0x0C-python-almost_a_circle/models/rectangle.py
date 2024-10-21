#!/usr/bin/python3
""" Defines a Rectangle module
    """
from models.base import Base


class Rectangle(Base):
    """Rectangle class taht inherits from Base class

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilizing instances (class constructor)

        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of the width

        Returns:
            int: _description_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter of the width

        Args:
            width (int): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter of the height

        Returns:
            int: _description_
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter of the height

        Args:
            height (int): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter of the position x

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Setter of the position x

        Args:
            x (int): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter of the position y

        Returns:
            int: _description_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Setter of position y

        Args:
            y (int): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of a rectangle

        Returns:
            _type_: _description_
        """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle
        instance with the character #
        """
        [print() for _ in range(self.y)]
        [print(" " * self.x + "#" * self.width) for _ in range(self.height)]

    def __str__(self) -> str:
        """Custom printing of Rectangle instances

        Returns:
            str: _description_
        """
        a = self.height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{a}"

    def update(self, *args, **kwargs):
        """assigns each argument to its correspondant attribute
        """
        att = ['id', 'width', 'height', 'x', 'y']
        if args is not None and args != ():
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
