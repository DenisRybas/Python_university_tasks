import unittest
import task2
import random


class TestTask2(unittest.TestCase):

    def test_example1(self):
        test_arr = [[11, 12, 15, 11, 53, 11, 14, 14],
                    [13, 12, 14, 13, 15, 13, 15, 15],
                    [13, 12, 14, 13, 15, 13, 14, 14],
                    [13, 12, 14, 13, 15, 13, 14, 14],
                    [13, 12, 14, 11, 15, 13, 14, 14]]
        self.assertEqual(task2.remove_equal_columns(test_arr),
                         [[11, 12, 15, 11, 53, 14],
                          [13, 12, 14, 13, 15, 15],
                          [13, 12, 14, 13, 15, 14],
                          [13, 12, 14, 13, 15, 14],
                          [13, 12, 14, 11, 15, 14]])

    def test_example2(self):
        test_arr = [[11, 12, 15, 11, 53, 11, 14, 14],
                    [13, 12, 14, 13, 15, 13, 14, 15],
                    [13, 12, 14, 13, 15, 12, 14, 14],
                    [13, 12, 14, 13, 15, 13, 14, 14],
                    [13, 12, 14, 11, 15, 13, 14, 14]]
        self.assertEqual(task2.remove_equal_columns(test_arr),
                         [[11, 12, 15, 11, 53, 11, 14, 14],
                          [13, 12, 14, 13, 15, 13, 14, 15],
                          [13, 12, 14, 13, 15, 12, 14, 14],
                          [13, 12, 14, 13, 15, 13, 14, 14],
                          [13, 12, 14, 11, 15, 13, 14, 14]])

    def test_empty_array(self):
        test_list = []
        task2.remove_equal_columns(test_list)
        self.assertEqual(test_list, [])

    def test_invalid_type_argument(self):
        test_list = 2
        with self.assertRaises(TypeError):
            task2.remove_equal_columns(test_list)

    def test_none_argument(self):
        test_list = None
        with self.assertRaises(TypeError):
            task2.remove_equal_columns(test_list)


if __name__ == '__main__':
    unittest.main()
