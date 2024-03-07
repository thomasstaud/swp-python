import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def create_from_list(self):
        liste = LinkedList()
        # todo: test

    def test_length(self):
        liste = LinkedList()
        liste.append(1)
        liste.append(2)
        liste.append(3)

        self.assertEqual(len(liste), 3)

    def test_methods(self):
        liste = LinkedList()

        liste.append(999)
        liste.insert_at(0, 1)
        liste.append(999)
        liste.insert_at(2, 2)
        liste.pop()
        liste.remove_at(1)

        self.assertEqual(str(liste), "1 -> 2")


if __name__ == '__main__':
    unittest.main()
