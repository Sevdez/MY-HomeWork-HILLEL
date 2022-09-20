#Данный код написал с использованием функции
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

c = 0
N = float(input("Введите вес в кг: ")) * 1000
i = 35

def mul(a):
    global N
    global c
    while N > i:
        N = N / 2
        c += 1
    a = c // 8
    b = (c % 8) + 1
    t = my_list [a]
    return t, b

q = mul(N)

print("Ответ", q)