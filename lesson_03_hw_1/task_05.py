n = input("Введите трехзначное число: ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10

print("Сумма цифр числа:", n + d2 + d2)
input("by Sevdez")