def zaprzyjaznione(a, b):
    for i in range(a, b):
        for j in range(1, i):
            if friend(i, j):
                return i, j


def friend(a, b):
    sum_del_a = 0
    sum_del_b = 0

    for i in range(1, a // 2 + 1):
        if a % i == 0:
            sum_del_a += i
        if sum_del_a > b:
            return False

    for i in range(1, b // 2 + 1):
        if b % i == 0:
            sum_del_b += i
        if sum_del_b > a:
            return False

    return a == sum_del_b and b == sum_del_a


min_val = 1
max_val = 300
# zaprzyjaznione(min_val, max_val)



