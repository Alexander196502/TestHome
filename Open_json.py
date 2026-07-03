import json

d = {'black':'черный',
     'white':'белый'}
with open('dict.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    #json.dump(d, f, indent=4)
while True:
    word = input('Введите слова для перевода: ')
    if word in d:
        print(f' {word} - {d[word]}')
    elif word == 'q':
        break
    else:
        transl = input(f'Ввдите перевод слова - {word}')
        d[word] = transl
        with open('dict.json', 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2)