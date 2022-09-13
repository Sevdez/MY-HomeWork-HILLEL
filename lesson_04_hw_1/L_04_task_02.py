import math

AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")

AB = float(AB)
AC = float(AC)

def triangle_square_and_perimeter(a, b):
    BC = math.sqrt(AB ** 2 + AC ** 2)
    S = (AB * AC) / 2
    P = AB + AC + BC
    return S, P

print("Площадь треугольника: %.2f" % S)
print("Периметр треугольника: %.2f" % P)
