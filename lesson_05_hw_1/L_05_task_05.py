print("Для определения значака числа с помощью функции sign() введите х:")

x = float(input("x = "))

def formulka(a):
    if a > 0:
        return "sign(x) = 1"
    elif a < 0:
        return "sign(x) = -1"
    else:
        return "sign(x) = 0"

formulka(x)

q = formulka(x)

print("Ответ будет:", q)