from random import randint


def date_sorting(dates):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if dates[i]['rok'] > dates[j]['rok']:
                dates[i], dates[j] = dates[j], dates[i]
            elif dates[i]['rok'] == dates[j]['rok']:
                if dates[i]['miesiac'] > dates[j]['miesiac']:
                    dates[i], dates[j] = dates[j], dates[i]
                elif dates[i]['miesiac'] == dates[j]['miesiac']:
                    if dates[i]['dzien'] > dates[j]['dzien']:
                        dates[i], dates[j] = dates[j], dates[i]


if __name__ == "__main__":
    n = 8
    dates = [{'dzien': randint(1, 28), 'miesiac': randint(1, 12), 'rok': randint(1800, 2022)} for i in range(n)]
    for date in dates:
        print(date)
    date_sorting(dates)
    print('\n')
    for date in dates:
        print(date)
