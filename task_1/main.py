from datetime import datetime


def is_even_source(x):
    return x % 2 == 0


def is_even_my_solution(x):
    return False if x & 1 else True


array = range(1000000)
for f in (is_even_source, is_even_my_solution):
    start_time = datetime.now()
    for num in array:
       f(num)
    print(datetime.now() - start_time)

