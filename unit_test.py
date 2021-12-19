from unittest import TestCase, main
from func_totest import my_func


class TestMyFunc(TestCase):
    def setUp(self):
        self.my_data = 10

    def test_correct1(self):
        self.assertEqual(my_func(1), 2)

    def test_incorrect2(self):
        self.assertFalse(my_func(1) == 3)

    def test_correct3(self):
        self.assertTrue(my_func(2) == 3)

    def test_correct4(self):
        self.assertEqual(my_func(self.my_data), 11)

    def test_exception5(self):
        with self.assertRaises(ValueError) as error:
            my_func('yep')
        the_exception = error.exception
        self.assertEqual(the_exception.args[0], 'wrong type of data inputted')


if __name__ == '__main__':
    main()

