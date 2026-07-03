import random as rd
from string import ascii_letters
nums = [22, 33, 44, 55, 66, 77, 88, 99]
names = ['Dasha', 'Sasha', 'Glasha', 'Misha', 'Andre']

print('Random',rd.random())
print('Uniform - ', rd.uniform(0, 1))
print('Uniform - ', rd.uniform(-10, -1)) #вещественное число

print('Randint - ', rd.randint(0, 10)) #целое чтслдо включая 10

print('Randrange - ', rd.randrange(2, 100, 2)) #

print('Choice - ', rd.choice(nums)) #выбор сл объекта коллекции
print('Choice - ', rd.choice(range(1, 11, 2)))
print('Choice - ', rd.choice(names))

print('Choices - ', rd.choices(nums, k=20))
print('Sample - ', rd.sample(nums, 3))
print(ascii_letters)
password = rd.choices(ascii_letters, k=8)
password = rd.sample(ascii_letters, k=8)
print(''.join(password))

salary = [[60, 80, 70], [99, 102, 122]]
workers = 12
months = 3
salary =[]
for w in range(workers):
#    salary.append([])
#    for m in range(months):
#        salary[w].append(rd.randint(60, 150))
#print(salary)
    salary.append(rd.choices(range(60, 151, 5), k=months))
print(salary)

#лист компрахеншн
l = [22, 33, 44]
res = []
for i in l:
    if i ** 2 % 2 == 0:
        res.append(i ** 2)
print(res)

res - [i ** 2 for i in l if i ** 2 % 2 == 0]
print(res)