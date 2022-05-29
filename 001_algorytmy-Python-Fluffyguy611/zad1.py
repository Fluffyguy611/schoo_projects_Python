# proba zrobienia kodu przy pomocy sample
samples = [{'zakres': 10,
            'expected': {'wynik': (2, 3, 5, 7)},
            'actual': None
            },
           ]

for sample in samples:
    result = {'wynik': None}
    for i in range(1, sample['zakres']+1):
        if i == 1 or i == 0:
            result['wynik'] = None

        elif sample['zakres'] % i == 0:
            result['wynik'] = None
        else:
            result['wynik'] = i
        sample['actual'] = result

for sample in samples:
    if sample['expected'] == sample['actual']:
        print(sample, "OK")
    else:
        print(sample, "NOT OK")
