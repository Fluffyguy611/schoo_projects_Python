# testy do zadan
import zad1
import unittest

czysta_plasza = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
max_plansza = 8


# test nr 1 Generowanie mapy
# sprawdzanie czy hetmani zostali poprawnie
class CzyBijeTest(unittest.TestCase):
    def testBicie_niepoprawne(self):
        hetmani = [[1, 0], [1, 3], [5, 3], [0, 6], [1, 7]]
        pionek = [[5, 4]]

        actual_value = zad1.bicie(hetmani, pionek)

        self.assertEqual(5, actual_value)

    def testBicie_poprawne(self):
        hetmani = [[6, 1], [7, 2], [4, 3], [7, 4], [1, 7]]
        pionek = [[5, 7]]

        expected_value = [[1, 7]]
        actual_value = zad1.bicie(hetmani, pionek)

        self.assertEqual(expected_value, actual_value)

    def testBicie_zla_odp(self):
        hetmani = [[5, 0], [1, 2], [7, 3], [0, 1], [7, 7]]
        pionek = [[6, 5]]

        expected_value = [[7, 7]]
        actual_value = zad1.bicie(hetmani, pionek)

        self.assertEqual(expected_value, actual_value)

    def testBicie_poprawne2(self):
        hetmani = [[0, 0], [5, 2], [3, 6], [3, 7], [6, 7]]
        pionek = [[4, 3]]

        expected_value = [[5, 2]]
        actual_value = zad1.bicie(hetmani, pionek)

        self.assertEqual(expected_value, actual_value)

    def test_Edge(self):
        hetmani = [[-3, -7], [3, -7], [3, 6], [3, 7], [6, 7]]
        pionek = [[4, 3]]

        expected_value = []
        actual_value = zad1.bicie(hetmani, pionek)

        self.assertEqual(expected_value, actual_value)


class CzyJestHetman(unittest.TestCase):
    def test_Hetman_correct(self):
        hetmani_k = 3
        expected_numb_hetmani = 3
        expected_hetmani = [[8, 8], [8, 8], [8, 8]]
        expec_het = [[0, 0], [0, 0], [0, 0]]

        actual_plansza, actual_hetmani = zad1.add_hetmani(czysta_plasza, max_plansza, hetmani_k)
        x = len(actual_hetmani)

        self.assertEqual(expected_numb_hetmani, x)
        self.assertGreater(expected_hetmani, actual_hetmani)
        self.assertLessEqual(expec_het, actual_hetmani)


class CzyJestPionek(unittest.TestCase):
    def test_Pionek_correct(self):
        actual_matrix, actual_pionek = zad1.add_pionek(czysta_plasza, max_plansza)

        self.assertIsNotNone(actual_pionek)


class CzyJestPlansza(unittest.TestCase):
    def test_Plansza(self):
        actual_value = zad1.plansza(max_plansza)
        self.assertIsNotNone(zad1.plansza(max_plansza))
        for i in range(max_plansza):
            for j in range(max_plansza):
                self.assertEqual(0, actual_value[i][j])


class user_input(unittest.TestCase):
    def test_User(self):
        min_val = 0
        max_val = 10
        k = 4

        expected_value = 4
        actual_value = zad1.user_input_control(min_val, max_val)

        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()
