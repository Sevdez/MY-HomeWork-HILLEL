def gen_primes():
    my_list = []
    for i in range(2, 100):
        for j in range(2, 99):
            if i % j == 0:
                break
            elif i not in my_list:
                my_list.append(i)
    print(my_list)

gen_primes()