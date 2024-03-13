import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_create_from_list(self):
        lst = LinkedList.from_list([1, 2, 3])
        self.assertEqual(str(lst), "1 -> 2 -> 3")

    def test_length(self):
        lst = LinkedList.from_list([1, 2, 3])
        self.assertEqual(len(lst), 3)

    def test_methods(self):
        lst = LinkedList()

        lst.append(999)
        lst.insert_at(0, 1)
        lst.append(999)
        lst.insert_at(2, 2)
        lst.pop()
        lst.remove_at(1)

        self.assertEqual(str(lst), "1 -> 2")


if __name__ == '__main__':
    unittest.main()
