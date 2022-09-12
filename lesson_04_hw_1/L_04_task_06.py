a=int(input("Введите количество чисел, которые нужно суммировать:"))
sum=0
print("Введите сами числа:")
for i in range(a):
    x=int(input())
    sum+=x
print ("Сумма введённых чисел:", sum)
