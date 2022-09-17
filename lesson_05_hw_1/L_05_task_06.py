#Даная формула действует только для рядка который начинается с единицы. Для рядка с нуля у меня никак не получается =(


print("Данная программа SEVDEZ выведет число Фибоначи от введённого:")

f = input("Введите число:")
f = int (f)

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(f)

q = fibonacci(f)

print("Ответ:", q)