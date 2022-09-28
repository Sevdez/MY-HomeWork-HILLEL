list = [472, 326, 1, '1101000', 9, '20', 863, '0']

def to_string(x):
    x = str(x)
    return x[0]

print(sorted(list, key = to_string))