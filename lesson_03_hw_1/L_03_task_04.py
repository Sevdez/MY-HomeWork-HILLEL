a = input("Введите имя и дату рождения: ").split('*')

name = a[0]
birth = a[1].split("-")
death = a[2].split("-")
years = int(death[0]) - int(birth[0])

if birth[1] > death[1]:
    years = years - 1
elif birth[2] > death[2]:
    years = years - 1

print("Name:", name)
print("Age:", years, "years")