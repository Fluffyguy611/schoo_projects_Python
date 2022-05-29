samples = [{'od': 1,
            'do': 10,
            'expected': {'wynik': [2, 3, 5, 7]},
            'actual': None
            },
           ]


for sample in samples:
    result = {'wynik': []}
    min_val = (sample['od'])
    max_val = (sample['do'])
    for i in range(min_val, max_val):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                result['wynik'].append(i)
        sample['actual'] = result

for sample in samples:
    if sample['expected'] == sample['actual']:
        print(sample, "OK")
    else:
        print(sample, "NOT OK")

