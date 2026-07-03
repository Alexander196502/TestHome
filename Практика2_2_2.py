st_e = input('Введите строку: ')

# Список гласных букв (русские)
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# Список согласных букв (русские)
consonants = 'бвгджзйклмнпрстфхцчшщ'

# Инициализация счётчиков
count_vow = 0
count_con = 0
count_num = 0

# Словарь для подсчёта частоты каждого символа
char_count = {}

# Один цикл для всех подсчётов
for i in st_e:
    # Подсчёт гласных
    if i in vowels:
        count_vow += 1
    # Подсчёт согласных (только буквы, не гласные и не пробелы)
    elif i.isalpha() and i in consonants:
        count_con += 1
    # Подсчёт цифр
    elif i.isdigit():
        count_num += 1

    # Подсчёт частоты всех символов (кроме пробелов)
    if i != ' ':
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

# Поиск самого частого символа
max_count = 0
max_ch = ''
for char, count in char_count.items():
    if count > max_count:
        max_count = count
        max_ch = char

# Вывод результатов
print(f"Количество гласных: {count_vow}")
print(f"Количество согласных: {count_con}")
print(f"Количество цифр: {count_num}")
print(f"Самый частый символ: '{max_ch}'")
print(f"Встречается в строке: {max_count} раз(а)")