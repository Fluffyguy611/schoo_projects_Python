import unittest
import Euklides


class EuklidesMultiTest(unittest.TestCase):
    def test_list_positive_numbers(self):
        list_of_numbers = [12, 16, 36, 41]
        actual_value = Euklides.euklides_multi(*list_of_numbers)
        self.assertEqual(4, actual_value)

