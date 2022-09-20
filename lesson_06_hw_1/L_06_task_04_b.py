def max_dig(n, md=0):
    if n < 10:
        return max(n, md)
    else:
        return max_dig(n // 10, max(md, n % 10))


n = int(input("Введите 12-значное натуральное число: "))
print("Самая большая цифра данного числа это: ", max_dig(n))