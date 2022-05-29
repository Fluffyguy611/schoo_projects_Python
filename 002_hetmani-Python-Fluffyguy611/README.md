# Zadanie nr 2 - Hetmani i Pionek

| Termin oddania | Punkty     |
|----------------|:-----------|
|    10.04.2022 23:00 |   10        |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:
- punkty uzyskanie za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
## Generowanie mapy [3 pkt]
Pierwszy etapem zadania będzie wygenerowanie planszy 8x8. W skład mapy wychodzą:
- k hetmanów rozmieszczonych losowa na mapie,
- jeden pionek rozmieszczony losowa na mapie.

Każdy z elementów zostaje ustawiony na różnej pozycji.
Po włączeniu programu schemat planszy powinien się wyświetlać użytkownikowi.

## Weryfikacja bicia [4 pkt]
Program powinien odpowiadać na pytania: 
Czy pionek zostanie zbity przez któregos z hetmanów?

Dodakowo wyświetlić pozycje wszystkich hetmanów, którzy mają możliwość zbicia pionka (o ile tacy istnieją).

## Dodakowe funkcje [3 pkt]
Po wyświeleniu komunikatu z informacją o biciu, użytkownik programu, powinien mieć możliwość:
- wylosowania nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów;
- usunięcia dowolnego hetmana (wskazanie jego pozycji);
- ponowną weryfikację bicia po ustaleniu zmian.

## Uwagi
1. Hetman może poruszać się pionowo, poziomo lub ukośnie.
2. Maksymalna liczba hetmanów (k) to 5.
3. Napisz testy jednostkowe tam, gdzie to możliwe.
4. Napisz algorytm sortujący od podstaw. Nie korzystaj z gotowych rozwiązań dostępnych w Pythonie.

