# Zadanie: Ekologia

| Termin oddania | Punkty     |
|----------------|:-----------|
|    15.05.2022 23:00 |   10        |

--- 
Przekroczenie terminu o **n** zajęć wiąże się z karą:
- punkty uzyskania za realizację zadania są dzielone przez **2<sup>n</sup>**.

--- 
W katalogu `begin` znajduje się definicja świata, w którym rządzą następujące zasady:
* świat jest płaski i posiada wysokość i szerokość
* każdy organizm na świecie posiada: 
    * `power`: zwiększa się co jedną turę o 1; decyduje o sile organizmu
    * `initiative`: priorytet decyduje o  kolejności wykonania ruchu w ramach jednej tury
    * `position`: położenie w świecie
    * `liveLength`: liczba tur do końca życia
    * `powerToReproduce`: granica dolna siły, powyżej której może się rozmnażać; po rozmnożeniu traci połowę siły
    * `sign`: znak reprezentujący organizm w świecie
    * `world`: świat, w którym żyje organizm
* jedynymi organizmemi żyjącym na świecie jest trawa i owca.

## Ryś [3 pkt]
Bazując na definicji zwierzęcia dodać rysia, który posiada następujące atrubuty:
* `power = 6`
* `initiative = 5`
* `liveLength = 18`
* `powerToReproduce = 14`
* `sign = 'R'`


## Antylopa [3 pkt]
Dodać antylopę, która zachowuje się jak owca, z tym, że jeżeli w jej otoczeniu pojawi Ryś, to ucieka od niego o dwa pola (kierunek odwrotny do występowania rysia), jeżeli ucieczka nie jest możliwa, atakuje rysia.
* `power = 4`
* `initiative = 3`
* `liveLength = 11`
* `powerToReproduce = 5`
* `sign = 'A'`


## Plaga [2 pkt]
Dodaj możliwość włączenia trybu plagii, który powoduje skrócenie życia wszystkim organizmów o połowę. Plaga działa tylko dwie tury i nie powoduje zmian w dalszych pokoleniach organizów.

## Dodanie organizmu [2 pkt]
Zaimplementować możliwość dodania po dowolnej turze dowolnego nowego organizmu na dowolne wolne pole.

## Uwaga
Do każdej dodawanej nowej funkcjonalności napisać odpowiednie testy jednostkowe.

