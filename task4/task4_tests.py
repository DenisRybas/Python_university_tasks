import unittest
import task4
import string


class TestTask4(unittest.TestCase):

    def test_example1(self):
        test_string = 'Hello, world!'
        self.assertEqual(task4.caesar(test_string, 2, (string.ascii_lowercase,
                                                       string.ascii_uppercase)), 'Jgnnq, yqtnf!')

    def test_example2(self):
        test_string = 'Привет, мир!'
        self.assertEqual(task4.caesar(test_string, 2, ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                                                       'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')), 'Сткджф, окт!')

    def test_empty_string(self):
        test_string = ''
        self.assertEqual(task4.caesar(test_string, 2, ()), '')

    def test_invalid_type_argument(self):
        test_string = 2
        with self.assertRaises(AttributeError):
            self.assertEqual(task4.caesar(test_string, 2, ()), '')

    def test_none_argument(self):
        test_string = None
        with self.assertRaises(AttributeError):
            task4.caesar(test_string, 2, ())


if __name__ == '__main__':
    unittest.main()
