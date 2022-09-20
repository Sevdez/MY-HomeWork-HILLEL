import math

r = float(input("Введите радиус конуса: "))
h = float(input("Введите высоту конуса: "))

def cone_square_and_volume (a, b):
    v = math.pi*r*r*h/3
    s = math.pi*r*math.sqrt(r*r+h*h)
    return v, s

v, s = cone_square_and_volume (r, h)

print("Площадь конуса: ", s)
print("Объём конуса: ", v)
