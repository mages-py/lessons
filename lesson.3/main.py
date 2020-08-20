from time import time
from functools import wraps

EVEN =  0   # четные числа
ODD =   1   # нечетные числа
PRIME = 2   # простые числа


def time_decor(func, *args):
    
    @wraps(func)
    def wrapper(*args, key = 2):
        time_start = time()
        ret = func(*args, key = key)
        time_end = time()
        print("\nComputed in", func.__name__, time_end - time_start)
        return ret
    return wrapper

def prime_number(val):
    if val % 2 == 0:
        return val == 2
    num = 3
    while pow(num, 2) <= val and val % num != 0:
        num += 2
    return pow(num, 2) > val


@time_decor
def my_pow(*args, key):
    return [pow(v,key) for v in args]

@time_decor
def oep_numbers(*args, key):
    if key == EVEN or key == ODD:
        return list(filter(lambda val: val % 2 == key, args))
    elif key ==PRIME:
        return list(filter(lambda val: prime_number(val) == True, args))
    else:
        return list(args)

print (my_pow(1, 2, 3, 4, 5, 6, 7, 8, 9))                       
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

print (my_pow(1, 2, 3, 4, 5, 6, 7, 8, 9, key = 3))              
# [1, 8, 27, 64, 125, 216, 343, 512, 729]

print (oep_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, key = ODD))       
# [1, 3, 5, 7, 9]

print (oep_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, key = EVEN))      
# [2, 4, 6, 8]

print (oep_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, key = PRIME))
# [1, 2, 3, 5, 7]

print (oep_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, key = 3))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]