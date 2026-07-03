# Декораторы
import random
import time


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'На входе функции {func.__name__} - {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__} - {res}, {kwargs}')
        return res
    return wrapper


def time_run(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        duration = round(end - start, 2)
        print(f'Время выполнения {func.__name__} - {duration} сек.')

    return wrap


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper


@time_run
def etalon(n, m):
    print('START')
    time.sleep(n + m)


@decor
def proba():
    print('PROBA')

@in_out
def sumr(x, y):
    return x + y

# print(__name__)
if __name__ == '__main__':
    # proba()
    # etalon(3, 1)

    result = sumr(random.randint(10, 10000), random.randint(10, 10000)) / .35 * .56
    print(result)