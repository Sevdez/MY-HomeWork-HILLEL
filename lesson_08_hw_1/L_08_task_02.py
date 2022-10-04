my_list = [750, 4546, 787]

def copy_deep(nested_content):
  return eval(repr(nested_content))

NL = copy_deep(my_list)

print(NL)
