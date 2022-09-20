from    random  import randint

print("Данная программа SEVDEZ найдет максимум и минимум из случайно сгенерированных чесел")

N = int(input("Введите количество чисел: "))

nums = [randint(1, 100) for i in range(N)]

print (nums)

myMax = nums[0]
myMin = nums[0]

for i in range(N):
    if nums[i] > myMax : myMax=nums[i]
    if nums[i] < myMin : myMin=nums[i]

print ('Max:', myMax, 'Min:', myMin)