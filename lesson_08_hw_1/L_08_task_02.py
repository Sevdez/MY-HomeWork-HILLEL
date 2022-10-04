my_list = [750, 4546, 787]

def copy_deep(nested_content):
  return repr(nested_content)

NL = copy_deep(my_list)

print(NL)
