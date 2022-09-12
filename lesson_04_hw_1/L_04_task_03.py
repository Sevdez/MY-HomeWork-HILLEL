import math
r = float(input("Введите радиус конуса: "))
h = float(input("Введите высоту конуса: "))

def v (r,h):
    res=(math.pi*r*r*h)/3
    return res
def s (r,h):
    res=math.pi*r*math.sqrt(r*r+h*h)
    return res

ob=v(r,h)
p=s(r,h)

print("Площадь конуса: ", p)
print("Объём конуса: ", ob)
