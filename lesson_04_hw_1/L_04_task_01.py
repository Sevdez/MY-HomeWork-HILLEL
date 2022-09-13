import math

a = float(input("Введите градусы:"))

def degrees2radians (a):
    q = (a*(math.pi)/180)
    return q

degrees2radians (a)

g = degrees2radians(a)

print(a, "Градусов в радианах будет:", g)