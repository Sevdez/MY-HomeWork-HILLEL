from math import sqrt

print("Программа SEVDEZ проверит пересекаются ли окружности, для этого введите следующие данные:")

x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
r1 = float(input("r1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
r2 = float(input("r2 = "))

def circles_intersect(x1, y1, r1, x2, y2, r2):
    cen_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if not cen_dist:
        return "Нет" if r1 != r2 else "Да"
    else:
        return "Нет" if cen_dist > r1 + r2 else "Да"


circles_intersect(x1, y1, r1, x2, y2, r2)

q = circles_intersect(x1, y1, r1, x2, y2, r2)

print("Ответ:", q)