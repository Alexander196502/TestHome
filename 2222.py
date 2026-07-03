from string import ascii_letters

import random as rd

#

# nums = [22, 33, 44, 55, 66, 77, 88, 99]

# names = ['Dasha', 'Sasha', 'Glasha', 'Masha', 'Andre']

#

# print('Random -',rd.random())

# print('Uniform -', rd.uniform(0, 1))

# print('Uniform -', rd.uniform(-10, -1))  ## Вещественное число

#

# print('Randint - ', rd.randint(9, 10))  # целое число включая 10

# print('Randrange - ', rd.randrange(2, 100, 2))

#

# print('Choice -', rd.choice(nums))   # выбор случайного объекта из коллекции

# print('Choice -', rd.choice(range(1, 11, 2)))

# print('Choice -', rd.choice(names))


# print('choices -', rd.choices(nums, k=20))

# print('sample -', rd.sample(nums, 8))

# print(ascii_letters)

# # password = rd.choices(ascii_letters, k=8)

# password = rd.sample(ascii_letters, 8)

# print(''.join(password))


# salary = [[60, 80, 70], [99, 102, 122]]

workers = 5

months = 3

salary = []

Elena
Seniut
left
Igor
12: 37

for w in range(workers):
    salary.append(rd.choices(range(60, 151, 5), k=months))

#     for m in range(months):

#         salary[w].append(rd.randint(60, 150))

print(salary)

#


# лист компрэхеншн

# l = [22, 33, 44, 55, 77, 88]

# res = []

# for i in l:

#     res.append(i ** 2)

# print(res)

#

# res = [i ** 2 for i in l ]

# print(res)