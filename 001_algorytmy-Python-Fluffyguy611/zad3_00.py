def jozef(n, k):
    if n == 1:
        return 1
    else:
        return ((jozef(n - 1, k) + k - 1) % n) + 1


n = 50  # ilosc zolnierzy
k = 2  # nastepny zolniez z lewej
print(jozef(n, k))
