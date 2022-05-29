# proba stworzenia programu przy pomocy wrozy Eulera

def friend(a, b):
    k = a
    n = b
    print(k, n)
    if k <= n:
        p = ((2**k) + 1)*(2**(n+1)-k) - 1
        q = ((2**k) + 1)*(2**(n+1)) - 1
        r = (((2 ^ k) + 1) ^ 2) * (2 ^ (2*n + 2-k)) - 1
        prime1 = (2 ^ n+1) * p * q
        prime2 = (2 ^ n+1) * r

        for i in range(prime1):
            if i % prime1 == 0:
                return False
        for i in range(prime2):
            if j % prime2 == 0:
                return False
            else:
                return True


min_val = 1
max_val = 287
for i in range(min_val, max_val):
    for j in range(1, i):
        if friend(j, i):
            print("%d i %d to liczby zaprzyjaznione", i, j)








