# instalowanie dodatku numpy (tworzenie planszy)
import numpy as np
# instalowanie dodatku randomizacji
import random


# Generowanie planszy z k hetmanow i ustawanie ludzika
# zadanie 1
def plansza(max_plansza):
    matrix = np.zeros((max_plansza, max_plansza))
    return matrix


def user_input_control(min_val, max_val):
    counter = 0
    while counter < 1:
        user_input = int(input())
        if min_val <= user_input <= max_val:
            return user_input
        else:
            print('Podany zly zakres, prawidlowy to', min_val, max_val)


def add_hetmani(matrix, max_plansza, k):
    hetman = []
    counter = 0
    while counter < k:
        rand_row = random.randint(0, max_plansza-1)
        rand_column = random.randint(0, max_plansza-1)
        if matrix[rand_row][rand_column] != 1:
            matrix[rand_row][rand_column] = 1
            counter = counter + 1
            hetman.append([rand_row, rand_column])
    hetman.sort()
    return matrix, hetman


def add_pionek(matrix, max_plansza):
    pionek = []
    counter = 0
    while counter < 1:
        rand_row = random.randint(0, max_plansza - 1)
        rand_column = random.randint(0, max_plansza - 1)
        if matrix[rand_row][rand_column] == 0:
            matrix[rand_row][rand_column] = 5
            counter = counter + 1
            pionek.append([rand_row, rand_column])
    return matrix, pionek


# Zadanie 2 Weryfikacja bicia
# Hetman porusza sie na skosy, w gore/dol i w boki
# skosy == wartosc wezwzgledna kolumn i wierszy
def bicie(hetmani, pionek):
    i = 0
    j = 1
    jest_bicie = []
    pionek_row = pionek[i][i]
    pionek_column = pionek[i][j]
    for hetman in hetmani:
        hetman_row = hetman[i]
        hetman_column = hetman[j]
        if hetman_row == pionek_row or hetman_column == pionek_column:
            jest_bicie.append(hetman)
        elif abs(hetman_row - pionek_row) == abs(hetman_column - pionek_column):
            jest_bicie.append(hetman)
    return jest_bicie


# zadanie 3 - interface i wybor
# jedna fukcja jest warunek
# druga jest interface
def warunek(matrix, hetman, pionek, x, wyjsce):
    max_plansza = 8
    if wyjsce == 1:
        i = 0
        counter = 0
        pionek_row = pionek[i][i]
        pionek_column = pionek[i][i + 1]
        while counter < 1:
            rand_row = random.randint(0, max_plansza - 1)
            rand_column = random.randint(0, max_plansza - 1)
            if matrix[rand_row][rand_column] == 0:
                matrix[rand_row][rand_column] = 5
                matrix[pionek_row][pionek_column] = 0
                pionek.clear()
                pionek.append([rand_row, rand_column])
                counter = counter + 1
    if wyjsce == 2:
        k = user_input_control(0, x-1)
        matrix_row = hetman[k][0]
        matrix_column = hetman[k][1]
        matrix[matrix_row][matrix_column] = 0
        x = x - 1
        hetman.pop(k)
    return matrix, hetman, pionek, x


def interface():
    max_plansza = 8
    min_hetman = 1
    max_hetman = 5
    matrix = plansza(max_plansza)
    print('Ile hatmanow chcesz miec?,\nmin = 1, max = 5')
    k_hetmanow = user_input_control(min_hetman, max_hetman)
    matrix, hetman = add_hetmani(matrix, max_plansza, k_hetmanow)
    matrix, pionek = add_pionek(matrix, max_plansza)
    wyjsce = None
    while wyjsce != 0:
        czy_bije = bicie(hetman, pionek)
        min_option = 0
        max_option = 2
        print(matrix)
        print('Hetmani sa na polach: ', hetman)
        print('Pionek jest na polu: ', pionek)
        print('Hetmani bija pionek z pozycji: ', czy_bije)
        print('\nWcisnij 1 aby wylosowac nowa pozycje pionka')
        print('Wcisnij 2 aby usunac wskazanego hetmana')
        print('Jesli chcesz wyjsc, wpisz: ''0''')
        wyjsce = user_input_control(min_option, max_option)
        matrix, hetman, pionek, k_hetmanow = warunek(matrix, hetman, pionek, k_hetmanow, wyjsce)


if __name__ == "__main__":
    interface()
