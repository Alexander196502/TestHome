st_e = input('Введите строку :')

vowels = 'а, е, ё, и, о, у, ы, э, ю, я'
consonants = 'бвгджзйклмнпрстфхцчшщ'
numbers = '0123456789'

vowels = [i.strip() for i in vowels.split(",")]
print(vowels)
print(type(vowels))

count_vow = 0
count_con = 0
count_num = 0

for i in st_e:
    if i in vowels:
        count_vow +=1   # если гласная счетчик гл + 1
    elif i.isalpha():
        count_con +=1   #если согл сч согл +1
    elif i.isdigit():
        count_num +=1   #если цифра сч цифр +1

max_count = 0
max_ch =0
count = 0

for i in st_e:
    if i !=" ":
        count = st_e.count(i)
    if count > max_count:
        max_count = count
        max_ch = i

print(f"Количество гласных -{count_vow}\n Количество согласных-{count_con}\n Количество цифр-{count_num}\n Самый частый символ-{max_ch}\n Встречается в строке-{max_count}\n")