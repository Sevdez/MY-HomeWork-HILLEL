import random

def diff_odd_even(mas):
    mas = []
    sum = 0
    mas = [random.randint(1, 100) for i in range(1, 18)]
    return mas


q = diff_odd_even


print('Массив: %s' % q)



for i in q:

    if (i%2) == 0:

        sum += i
    elif (i%2) == 1:

        sum += i

print('Сумма четных элементов: %s' % sum)
print('Сумма нечетных элементов: %s' % sum)


#тут я немного застрял, не пойму почему питон ругается на q