# file = open('text.txt', 'r', encoding='utf-8')  # читаем содержимое
# # файла в переменную file
# # s = file.read(10)  # читаем 10 символов из текста в файле
# # print(s)
# # s = file.read()  # читаем весь текст в файле (что осталось)
# # print(s)
# # s = file.readline()  # читаем строку текста в файле (что осталось)
# # print(s)
# s = file.readlines()  # читаем все строки текста из файла в список
# print(s)
#
# file.close()

# for i in open('text.txt', 'r', encoding='utf-8'):
#     print(i.strip())

with open('text.txt', 'r', encoding='utf-8') as file:
    s = file.read().title()
    ls = s.split()

ls.sort()
print(ls)
with open('text1.txt', 'a', encoding='utf-8') as file: # записываем в
    # TEXT1 информацию -'w' или дописываем -'a'
    for k, i in enumerate(ls, 1):
        file.write(f'{k}. {i}\n')
