""" dict - неупорядоченный набор пар ключ:значение, в котором ключи уникальны """

d = {}

d = {

    'Pb': 'свинец',

    'Au': 'Золото',

}

print(d)

print(len(d))  # размер словаря d

print(d['Au'])  # получение значения по ключу в словаре d

print(d.get('Pb1'))  # получение значения по ключу в словаре d None при отсутствии ключа

print(d.get('Pb1', 'my value'))  # получение значения по ключу в словаре d my value при отсутствии ключа

d['Pb'] = 'Свинец'  # Изменение значения по ключу

d[10] = 100  # Добавление новой пары, так как ключ отсутствует

d.setdefault(10, 200)  # добавляет пару только в случае отсутствия ключа 10 в словаре d

value = d.setdefault(10, 200)  # value получает значение по ключу (100)

print(value)

d.setdefault(20, 200)  # добавляет пару только в случае отсутствия ключа 20 в словаре d

value = d.setdefault(20, 200)  # value получает значение по ключу (200)

print(value)

# d.update({3: 300, 10: 10})
dd = d | {3: 300, 10: 10}
print(d)
print(dd)
n = d.pop(20)
nn = d.popitem()
print(n, nn)
print(d)

# создание словарей

# ls = [22, 33, 44]

# dd = dict.fromkeys(ls, 1000)  # создание словаря из объектов списка

# print(dd)

# dd = {i: i ** 2 for i in range(10, 20)}

# print(dd)

people = (('Mary', 22), ('Cherry', 26), ('Berry', 30))

dd = dict(people)

# print(dd)

people = {

    12030291020: {'name': 'Irina',

                  'age': 24

                  },

    34265171827: {'name': 'Dasha',

                  'age': 25

                  }

}

#

# lst = [

#     {'name': 'Dasha', 'inn': 123456, 'age': 24},

#     {'name': 'Sasha', 'inn': 546383, 'age': 25}

# ]

print(dd)

print(dd.keys())

print(list(dd))  # если словарь в функции по умолчанию предполагаются только ключи

print(list(dd.values()))  # вернет только значения

print(list(dd.items()))  # вернет всё

for i in dd:
    print(i, end='...')

print()

for i in dd.values():
    print(i, end='......')

print()

for i in dd.items():
    print(i, end='..')

print()

s = 'aaaaaaabaaaaaaaaaaaaaaytaaaaalaaaaaaaaha'

symbols = {}

for i in s:

    # if i not in symbols:

    #     symbols[i] = 1

    # else:

    #     symbols[i] += 1

    symbols[i] = symbols.get(i, 0) + 1

print(symbols)