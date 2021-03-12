import unittest
import task5
import random


class TestTask5(unittest.TestCase):

    def test_example1(self):
        test_list = [1, 5, 3, -1, 4, -2, 5, -3]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [-1, -2, -3, 1, 5, 3, 4, 5])

    def test_example2(self):
        test_list = [-1, 5, 3, -1, 4, -2, 5, -1]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [-1, -1, -2, -1, 5, 3, 4, 5])

    def test_example3(self):
        test_list = [-1, -5, -3, -1, 4, 2, 5, 3]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [-1, -5, -3, -1, 4, 2, 5, 3])

    def test_example4(self):
        test_list = [1, 5, 3, 1, 4, -2, -5, -3]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [-2, -5, -3, 1, 5, 3, 1, 4])

    def test_example5(self):
        test_list = [1, 5, 3, 1, 4, 2, 5, 3]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [1, 5, 3, 1, 4, 2, 5, 3])

    def test_example6(self):
        test_list = [-1, -5, -3, -1, -4, -2, -5, -3]
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [-1, -5, -3, -1, -4, -2, -5, -3])

    def test_empty_list(self):
        test_list = []
        task5.move_negative_numbers_to_start_of_list(test_list)
        self.assertEqual(test_list, [])

    def test_invalid_type_argument(self):
        test_list = 2
        with self.assertRaises(TypeError):
            task5.move_negative_numbers_to_start_of_list(test_list)

    def test_none_argument(self):
        test_list = None
        with self.assertRaises(TypeError):
            task5.move_negative_numbers_to_start_of_list(test_list)


if __name__ == '__main__':
    unittest.main()
