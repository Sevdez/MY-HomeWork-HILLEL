my_list = [750, 800, 543]

def index(lst, digit):
    if digit not in lst:
        return None
    counter = 0
    for elem in lst:
        if digit == elem:
            print(counter)
        else: counter += 1

index(my_list, 800)
index(my_list, 6454654)