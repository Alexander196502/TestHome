# a = 'I like python, it is very useful for data analysis'
# b = 'python is the best tool for dealing with big data'
# выписать вторую строку без слов в первой строке

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tool for dealing with big data'

# Шаг 1: Разбиваем строки на списки слов
# Убираем знаки препинания и приводим к нижнему регистру для точного сравнения
import string

# Очищаем строку a от знаков препинания и разбиваем на слова
words_a = set(a.translate(str.maketrans('', '', string.punctuation)).lower().split())

# Очищаем строку b от знаков препинания и разбиваем на слова
words_b = b.translate(str.maketrans('', '', string.punctuation)).lower().split()

# Шаг 2: Оставляем только те слова из b, которых нет в a
result_words = [word for word in words_b if word not in words_a]

# Шаг 3: Собираем результат обратно в строку
result = ' '.join(result_words)

print(result)