"""""set - неупорядоченный набор уникальных объектов"""

# 'Значение1' -> Хэш-функция -> Хэш-код -> Хэш-таблица
# 'Значение2' -> Хэш-функция -> Хэш-код -> Хэш-таблица
""" 1 = 'Значение2' 5 = 'Значение1' Поиск в списке - O(n) Поиск в множестве - O(1) объекты множества - любой неизменяемый тип данных """
st = {22, 33, 44, 44}
st.clear()
st = set() # создание пустого множества
ls = [22, 33, 44, 44]
st = set(ls)
print(st)
st.add(100)  # Добавление в множество одного объекта
st.update([1, 2])  # Добавление в множество объектов (элементов списка, множества, кортежа)
n = st.pop()
print(st)
nn = st.pop()
print(st, n, nn)
st.remove(2)  # удаление из множества указанного объекта (отсутствие объекта - ошибка)
st.discard(21)  # удаление из множества указанного объекта (отсутствие объекта - нет ошибки)
print(22 in st)
print(st)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
# res = st1.union(st2) # объединение множеств
# res = st1 | st2

# res = st1.intersection(st2) # пересечение множеств
# res = st1 & st2

# res = st1.difference(st2) # вычитание множеств
# res = st2 - st1

res = st1.symmetric_difference(st2)
res = st1 ^ st2
print(res)

st1 = {1, 2, 33}
st2 = {1, 2, 44}
st3 = {1, 2}
# print(st1.issuperset(st3))
# print(st3.issubset(st2))
# res = st1.differense(st2)
print(res)
print(st1)
print(st2)
st1.difference_update(st2)
print(st1)
print(st2)

ice_cream = ['клубника','малина','банан','клубника']
result = []
for n in ice_cream:
    if n not in result:
        result.append(n)
print(result)
set = set(ice_cream)
# result = [n for n in set(ice_cream)]
# print(result)

a = 'I kike pytin, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'

a = a.replace(',','')
sta = set(a.split())
stb = set(b.split())
print(' '.join(list(stb - sta)))

la = a.split()
lb = b.split()
res = [w for w in lb if w]
res = []
for w in lb:
    if w not in la:
        res.append(w)
peint(' '.join(res))