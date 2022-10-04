my_list = [750, 4546, 787]
my_dict = {1:"Лапшичка", 2:"Супец", 3:"Борщик" }
my_tuple = ("колбаска", "рисик", "пивасик")

def copy_deep(nested_content):
  return eval(repr(nested_content))

NL = copy_deep(my_list)
ND = copy_deep(my_dict)
NT = copy_deep(my_tuple)

print(NL)
print(ND)
print(NT)