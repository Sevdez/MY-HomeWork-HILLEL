from random import randint

n = randint(1, 10)

while 1:
  k = input("Угадай число от 1 до 10: ")

  k = int(k)

  if k == n:
    print("Вы угадали")
    break

  if k > 10:
      print ("Напишите число от 1 до 10")

  if k < 1:
      print("Напишите число от 1 до 10")