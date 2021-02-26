import unittest
import task3

class TestTask3(unittest.TestCase):

    def test_example1(self):
        test_list = [[1, 2], [1, 3], [2, 4]]
        self.assertEqual(task3.find_triangle_with_max_area(test_list), 0.49999999999999967)

    def test_example2(self):
        test_list = [[1, 2], [1, 3], [2, 4], [1, 100], [2, 150], [3, 200]]
        self.assertEqual(task3.find_triangle_with_max_area(test_list),145.99999999987486)

    def test_collinear(self):
        test_list = [[1, 2], [1, 3], [1, 4]]
        self.assertEqual(task3.find_triangle_with_max_area(test_list), 0)

    def test_empty_list(self):
        test_list = []
        self.assertEqual(task3.find_triangle_with_max_area(test_list), 0)

    def test_invalid_type_argument(self):
        test_list = 2
        with self.assertRaises(TypeError):
            task3.find_triangle_with_max_area(test_list)

    def test_none_argument(self):
        test_list = None
        with self.assertRaises(TypeError):
            task3.find_triangle_with_max_area(test_list)

if __name__ == '__main__':
    unittest.main()