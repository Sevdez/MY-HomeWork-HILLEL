import random

pas = ''

for x in range(8):
    q = random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ_'))

    if len(pas) == 0:
        pas += q
    if len(pas) > 0:
        if q != pas[-1]:
            pas += q


print('Ваш пароль, ', pas)