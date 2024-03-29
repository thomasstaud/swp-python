from collections.abc import Iterator, Iterable


class LinkedList(Iterator):
    def __init__(self):
        self.head = None

    @staticmethod
    def from_list(lst):
        """
        Creates a linked list from a regular list.
        :param lst: list of integers
        """
        length = len(lst)
        next_node = None
        for i in range(length):
            node = Node(lst[length - i - 1])
            node.next = next_node
            next_node = node

        lst = LinkedList()
        lst.head = node
        return lst

    def prepend(self, value):
        """
        Inserts a value at the beginning of the list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """
        Appends a value to the end of the list.
        :param value: can be an integer or a list of integers
        """
        if value is LinkedList:
            new_node = value.head
        elif isinstance(value, Iterable):
            new_node = LinkedList.from_list(value).head
        else:
            new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def insert_at(self, position, value):
        """
        Inserts a value at the specified position.
        """
        if position == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        node = self.head
        index = 0
        while (index + 1) != position:
            if node.next is None:
                raise Exception

            index += 1
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def pop(self):
        """
        Removes the last element of the list and returns it.
        """
        if self.head.next is None:
            raise Exception

        prev_node = None
        node = self.head
        while node.next is not None:
            prev_node = node
            node = node.next
        prev_node.next = None
        return node.value

    def remove_at(self, position):
        """
        Inserts the element at the specified position.
        """
        index = 0
        prev_node = None
        node = self.head
        while index != position:
            if node.next is None:
                raise Exception

            index += 1
            prev_node = node
            node = node.next
        prev_node.next = node.next

    def __next__(self):
        if self.head is None:
            raise StopIteration
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def __len__(self):
        length = 1
        node = self.head
        while node.next is not None:
            node = node.next
            length += 1
        return length

    def __str__(self):
        node = self.head
        string = f"{node.value}"
        while node.next is not None:
            node = node.next
            string += f" -> {node.value}"
        return string


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value} -> {self.next}"
