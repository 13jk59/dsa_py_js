""" This module contains code for a class representing the deque
data structure """
from py.utils.linked_list import DoublyLinkedListNode
from typing import Any


class Deque:
    """ This class represents the deque data structure, implemented
    using doubly linked nodes.

    A deque is a linear collection that has support for lookup, insertion
    and deletion in O(1) time and space at the both the front and at
    the back of the data structure.

    Attributes:
        head:
            Object of type DoublyLinkedListNode representing the element
            stored as the first element of the deque

        tail:
            Object of type DoublyLinkedListNode representing the element
            stored as the last element of the deque
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def peek_first(self) -> Any:
        """ This method returns the value contained inside the head
        node of the deque.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside the
            head node of the deque

        Raises:
            IndexError:
                An IndexError will be raised if there are no nodes inside
                of the deque
        """
        if self.head:
            return self.head.val
        else:
            raise IndexError("peek first in empty deque")

    def peek_last(self) -> Any:
        """ This method returns the value contained inside the tail
        node of the deque.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside the
            tail node of the deque

        Raises:
            IndexError:
                An IndexError will be raised if there are no nodes inside
                of the deque
        """
        if self.tail:
            return self.tail.val
        else:
            raise IndexError("peek last in empty deque")

    def add_first(self, val: Any) -> None:
        """ This method wraps the input val, which can be of any type,
        inside of a DoublyLinkedListNode and adds it to the deque as
        the first node.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst
        """
        new_head = DoublyLinkedListNode(val)
        if self.head:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head

    def add_last(self, val: Any) -> None:
        """ This method wraps the input val, which can be of any type,
        inside of a DoublyLinkedListNode and adds it to the deque as
        the last node.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst
        """
        new_tail = DoublyLinkedListNode(val)
        if self.tail:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        else:
            self.head = new_tail
            self.tail = new_tail

    def pop_first(self) -> Any:
        """ This method removes the first node from the deque, retrieves the
        value stored inside it and returns it.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside the
            head node of the deque

        Raises:
            IndexError:
                An IndexError will be raised if there are no nodes inside
                of the deque
        """
        if self.head:
            saved_val = self.head.val
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = new_head
            return saved_val
        else:
            raise IndexError("pop from empty deque")

    def pop_last(self) -> Any:
        """ This method removes the last node from the deque, retrieves the
        value stored inside it and returns it.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside the
            tail node of the deque

        Raises:
            IndexError:
                An IndexError will be raised if there are no nodes inside
                of the deque
        """
        if self.tail:
            saved_val = self.tail.val
            if not self.tail.prev:
                self.head = None
                self.tail = None
            else:
                new_tail = self.tail.prev
                new_tail.next = None
                self.tail = new_tail
            return saved_val
        else:
            raise IndexError("pop from empty deque")

    def __len__(self) -> int:
        """ This method returns the number of nodes inside of the deque.

        Time:
            O(N) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of nodes currently stored inside the deque

        Returns:
            Integer representing the number of nodes stored inside the deque
        """
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length
