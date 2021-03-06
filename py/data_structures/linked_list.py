""" This module contains code for a class that represents the
doubly linked list data structure """
from typing import Any
from py.utils.linked_list import DoublyLinkedListNode


class DoublyLinkedList:
    """ This class represents the doubly linked list data
    structure.

    Attributes:
        val:
            Value of any type representing the data initially stored at
            the head node of the doubly linked list data structure

        head:
            Object of type DoublyLinkedListNode representing
            the head node of the data structure

        tail:
            Object of type DoublyLinkedListNode representing the
            tail node of the data structure, which on construction is
            equivalent to the tail node
    """

    def __init__(self, val: Any):
        self.head = DoublyLinkedListNode(val)
        self.tail = self.head

    def get(self, index: int) -> Any:
        """ This method gets the value out of the ith node within the
        linked list.

        Time:
            O(N) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of nodes in the linked list.

        Args:
            index:
                Integer representing the index inside of the linked list to
                fetch the value from

        Returns:
            Value of any type representing the data stored at the ith index
            in the linked list
        """
        curr_index = 0
        node = self.head
        while node and curr_index <= index:
            if curr_index == index:
                return node.val
            curr_index += 1
            node = node.next
        return -1

    def add_at_head(self, val: Any) -> None:
        """ This function creates a doubly linked list node with the
        value given as input, and inserts the node to be the new
        head of the linked list.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            val:
                Data of any type representing the value to be stored
                at the new head node
        """
        new_node = DoublyLinkedListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_tail(self, val: Any) -> None:
        """ This function creates a doubly linked list node with
        the value given as input, and inserts the node to be the
        new tail of the linked list.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            val:
                Data of any type representing the value to be stored
                at the new tail node
        """
        new_node = DoublyLinkedListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def add_at_index(self, index: int, val: Any) -> None:
        """
        This method addes wraps the input val into a DoublyLinkedListNode
        and then inserts it as a node in the data structure at the ith
        index.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            index:
                Integer representing the index at which to insert the node
                within the linked list

            val:
                Data of any type representing the value to store as a node
                at the ith index inside of the linked list
        """
        if index == 0:
            self.add_at_head(val)
        else:
            self._insert_node(val, index)

    def _insert_node(self, val: Any, index: int) -> None:
        node = self.head
        curr_index = 0
        while node and curr_index <= index:
            if curr_index == index:
                self._change_node_pointers_insertion(node.prev, node, val)
                return
            else:
                node = node.next
                curr_index += 1
        # edge case -- inserting node at the end of the linked list
        # means we have a new tail node so pointers have to be change
        # appropriately for that
        if index == curr_index:
            self.add_at_tail(val)

    def _change_node_pointers_insertion(self, saved_prev: DoublyLinkedListNode,
                                        node: DoublyLinkedListNode,
                                        val: int) -> None:
        new_node = DoublyLinkedListNode(val)
        saved_prev = node.prev
        node.prev = new_node
        new_node.prev = saved_prev
        new_node.next = node
        saved_prev.next = new_node
        new_node.next = node

    def delete_at_index(self, index: int) -> None:
        """
        This method deletes the node at the given index out of the
        linked list.

        Time:
            O(N) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            index:
                Integer representing the index of the node to delete from
                the linked list
        """
        if not self.head:
            return
        elif index == 0:
            if not self.head.next:
                self.head = None
                self.tail = None
                return
            else:
                new_head = self.head.next
                new_head.prev = None
                self.head = new_head
        else:
            self._unlink_node(index)

    def _unlink_node(self, index: int) -> None:
        curr_index = 0
        prev_node = None
        curr_node = self.head
        while curr_node and curr_index <= index:
            if index == curr_index:
                if not curr_node.next:
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    next_node = curr_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                return
            else:
                prev_node = curr_node
                curr_node = curr_node.next
                curr_index += 1
