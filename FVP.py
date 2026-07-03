from functools import reduce


def power(n):
    return n ** 2


lst = [22, 33, 44, 55]
lss = [2, 3, 49, 5]
# res = list(map(str, lst))
# res = list(map(power, lst))  # применяет функцию power ко всем объектам списка lst
# res1 = [power(i) for i in lst]
# res = list(map(lambda n: n ** 2, lst))  # лямбда функция (унарная функция) в
# # памяти не лежит, возникает в строке и пропадает после выполнения
# # print(next(res))
# res = list(map(lambda n, m: n - m, lst, lss))
# res = list(map(lambda n, m: n > m, lst, lss))
# print(res)
# print(res1)
# res = list(filter(lambda n: n % 2 == 0, lst))
# print(res)
def conc(x, y):
    print('X -', x)
    print('Y -', y)
    print('X+Y', str(x) + str(y))
    return str(x) + str(y)

city = ['У', 'ф', 'а', '-', 4, 5]
# print(' '.join(city)) нельзя, т.к. присутствуют не строковые объекты
# res = reduce(lambda x, ystr(x) + str(y): str(y) + str(x), city)
res = reduce(lambda x, y: x + y, lst)
# res = reduce(conc, city)
print(res)