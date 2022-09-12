import math

AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB ** 2 + AC ** 2)


def perimetr(AB, AC):
    res = (AB + AC) * 2
    return res


def area(AB, AC):
    res = AB * AC
    return res


p = perimetr(AB, AC)
print("Периметр = %d" % (p))
s = area(AB, AC)
print("Площадь = %d" % (s))

print("Периметр = %d" % (perimetr(AB, AC)))
print("Площадь = %d" % (area(AB, AC)))
