"""Square module
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

    def __str__(self):
        """Custom printing of Square instances

        Returns:
            _type_: _description_
        """
        print(f"")
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
