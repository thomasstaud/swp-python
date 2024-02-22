import unittest
import poker_combinations


class TestPoker(unittest.TestCase):

    def test_straight_flush_normal(self):
        draw = [0, 1, 2, 3, 4]
        combination = poker_combinations.check_combinations(draw, 13)
        self.assertEqual(combination, "straight-flush")

    def test_straight_flush_ace(self):
        draw = [0, 1, 2, 3, 12]
        combination = poker_combinations.check_combinations(draw, 13)
        self.assertEqual(combination, "straight-flush")

    def test_four_of_a_kind(self):
        draw = [0, 13, 26, 39, 40]
        combination = poker_combinations.check_combinations(draw, 13)
        self.assertEqual(combination, "four-of-a-kind")


def main():
    unittest.main()


if __name__ == "main":
    main()
