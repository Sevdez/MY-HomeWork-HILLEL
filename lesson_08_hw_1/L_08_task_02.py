my_list = [750, 4546, 787]

def copydeep(lst):
    new_list = []
    for elem in lst:
        new_list.append(elem)
    return new_list

NL = copydeep(my_list)
print (NL)