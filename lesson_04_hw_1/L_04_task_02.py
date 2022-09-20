import math

ab = input("Длина первого катета: ")
ac = input("Длина второго катета: ")

ab = float(ab)
ac = float(ac)

def triangle_square_and_perimeter(a, b):
    bc = math.sqrt(ab ** 2 + ac ** 2)
    s = (ab * ac) / 2
    p = ab + ac + bc
    return s, p

s,p = (triangle_square_and_perimeter(ab, ac))

print("Площадь треугольника: %.2f" % s)
print("Периметр треугольника: %.2f" % p)
