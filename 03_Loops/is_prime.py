number = 39

is_prim = True

if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prim = False
                break
print(is_prim)
            