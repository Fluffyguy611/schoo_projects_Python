import zad3_00
# import zad4_00
import zad2_01
import unittest


class FlawiuszTest(unittest.TestCase):
    def test_positive_numer_soldiers(self):
        number_of_soldiers = 13
        standing_position = 5

        actual_value = zad3_00.jozef(number_of_soldiers, standing_position)

        self.assertEqual(5, actual_value)


# proba zrobienia testu do zadanie 4
#class SortdDatesTest(unittest.TestCase):
#    def test_two_dates(self):
#        number_of_dates = 2
#        dates = [{'dzien': 31, 'miesiac': 12, 'rok': 2001},
#                 {'dzien': 12, 'miesiac': 11, 'rok': 1999}]

#        actual_value = zad4_00.daty(dates, number_of_dates)

#        self.assertEqual(4, actual_value)


class FriendsTest(unittest.TestCase):
    def test_positive_friend_numbers(self):
        min_range_number = 110
        max_range_number = 300

        actual_value = zad2_01.zaprzyjaznione(min_range_number, max_range_number)

        self.assertEqual((284, 220), actual_value)
