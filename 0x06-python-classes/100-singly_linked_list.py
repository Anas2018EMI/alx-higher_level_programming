#!/usr/bin/python3
"""_summary_
    Defining Singly linked lists in Python
    """


class Node:
    """
    This is a class that defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __n_node (Node): The next node in the linked list.
    """

    def __init__(self, data, n_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            n_node (Node): The next node in the linked list. Defaults:None.
        """
        self.data = data
        self.n_node = n_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def n_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__n_node

    @n_node.setter
    def n_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("n_node must be a Node object")
        else:
            self.__n_node = value


class SinglyLinkedList:
    """
    This is a class that defines a singly linked list.

    Attributes:
        __head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.n_node
        return result.strip()

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.n_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.n_node is not None and value > current.n_node.data:
                current = current.n_node
            new_node.n_node = current.n_node
            current.n_node = new_node
