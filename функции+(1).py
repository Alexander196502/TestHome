"""подпрограмма которая ждет вызова для работы"""


def proba():  # процедура
    print('Ura-ura')


def summator(x: int, y: int) -> int:  # x, y - параметры функции summator
    """Описание функции"""
    z = x + y  # тело функции
    return z  # возврат результата


n = summator(20, 15)  # передача аргументов при вызове функции
print(n)
print(summator(20, 20))
print(summator.__doc__)
print(__doc__)


# def adding(x=4, y=15, z=16, g=33):
#     return x + y

# print(adding(2, 15)
# print(adding(2))
# print(adding(2, 14))
# print(adding())
# print(adding(y=30, z=1))

# n,  *z = 7, 5, 12, 77, 88, 99
# print(n, type(n))
# print(z, type(z))
# print(*z)
# d = {}
# n = 3
# for _ in range(n):
#     name, *marks = input('> ').split()
#     marks = [int(m) for m in marks]
#     d[name] = round(sum(marks) / len(marks), 2)
# print(d)

# def adding(*args, **kwargs):  # разное количество позиционных и ключевых аргументов
#     print(args)
#     print(kwargs, list(kwargs.values()))
#     sumkw = sum(list(kwargs.values()))
#     # return sum(args), sumkw
#     return sum(list(args) + list(kwargs.values()))
#
# print(adding(2, 15, 17, 33, x=12, y=33, z=18))
# print(adding())

