number = int(input("Введите число на проверку четности:"))

def is_even(a):
    return a % 2 != 0

is_even(number)

q = is_even(number)

if (q) == 0:

   print("Чётное", q)

else:

   print("Нечётное", q)