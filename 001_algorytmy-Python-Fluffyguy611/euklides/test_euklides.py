import unittest
import Euklides




class EuklidesTest(unittest.TestCase):
    def test_two_negative_numbers(self):
        first_number = -7
        second_number = - 13

        actual_value = Euklides.euklides(first_number, second_number)

        self.assertEqual(1, actual_value)

    def test_two_prime_numbers(self):
        first_number = 7
        second_number = 13

        actual_value = Euklides.euklides(first_number, second_number)

        self.assertEqual(1, actual_value)

    def test_two_numbers_with_same_multiplication(self):
        first_number = 127*4
        second_number = 13 * 4

        actual_value = Euklides.euklides(first_number, second_number)

        self.assertEqual(4, actual_value)

    def test_two_big_numbers_with_same_power(self):
        first_number = 127 ** 4
        second_number = 13 ** 4

        actual_value = Euklides.euklides(first_number, second_number)

        self.assertEqual(4, actual_value)

    def test_for_two_big_composed_numbers(self):
        # Arrange
        first_prime_number = 64781
        second_prime_number = 68041
        third_prime_number = 71429
        # Act
        actual_value = Euklides.euklides(
            first_prime_number * second_prime_number,
            second_prime_number * third_prime_number
        )
        # Assert
        self.assertEqual(second_prime_number, actual_value)
