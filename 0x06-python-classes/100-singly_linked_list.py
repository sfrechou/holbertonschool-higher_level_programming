#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """instantiation with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter to set data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property to retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property to retrieve next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class that defines a singly linked list"""

    def __init__(self):
        """simple instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """public instance that inserts and sorts a new Node"""
        current_node = self.__head
        if current_node is None:
            new = Node(value)
            new.data = value
            self.__head = new
            return

        if current_node.data > value:
            new = Node(value)
            new.data = value
            new.next_node = current_node
            self.__head = new
            return

        while current_node.next_node is not None:
            if current_node.next_node.data > value:
                break
            current_node = current_node.next_node
        new = Node(value)
        new.data = value
        new.next_node = current_node.next_node
        current_node.next_node = new
        return

    def __str__(self):
        """Convert linked list to string"""
        convertString = []
        current_node = self.__head
        while current_node is not None:
            convertString.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(convertString))
