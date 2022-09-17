print("Данна программа SEVDEZ может проверить високосный ли год, для этого:")

s = float(input("Введите год:"))

def year(a):
    if a % 400 == 0:
        return "високосный"
    elif a % 100 == 0:
        return "не високосный"
    elif a % 4 == 0:
        return "%d високосный"
    else:
        return "не високосный"


year(s)

q = year(s)

print("Введённый год ", q)