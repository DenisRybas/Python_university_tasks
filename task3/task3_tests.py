import unittest
import task3


# https://www.triangle-calculator.com/?what=vc&a=-5&a1=-5&3dd=3D&a2=0&b=-1&b1=-1&b2=0&c=15&c1=14&c2=0&submit=Solve&3d=0

class TestTask3(unittest.TestCase):

    def test_example1(self):
        test_list = []
        with open("task3/input1.txt") as textFile:
            for item in textFile:
                test_list.append([int(i) for i in item.split()])
            self.assertEqual(task3.find_triangle_with_max_area(test_list), 0.49999999999999967)

    def test_example2(self):
        test_list = []
        with open("task3/input2.txt") as textFile:
            for item in textFile:
                test_list.append([int(i) for i in item.split()])
            self.assertEqual(task3.find_triangle_with_max_area(test_list), 145.99999999987486)

    def test_collinear(self):
        test_list = []
        with open("task3/input3.txt") as textFile:
            for item in textFile:
                test_list.append([int(i) for i in item.split()])
        self.assertEqual(task3.find_triangle_with_max_area(test_list), 0)

    def test_one_point(self):
        test_list = []
        with open("task3/input4.txt") as textFile:
            for item in textFile:
                test_list.append([int(i) for i in item.split()])
            self.assertEqual(task3.find_triangle_with_max_area(test_list), 0)

    def test_negative_points(self):
        test_list = []
        with open("task3/input5.txt") as textFile:
            for item in textFile:
                test_list.append([int(i) for i in item.split()])
            self.assertEqual(task3.find_triangle_with_max_area(test_list), 2.0000000000004747)

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
