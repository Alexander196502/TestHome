# 4
import random
import string

def generate_password(m: int) -> str:
    """
    Генерирует один случайный пароль длиной m символов.

    Пароль состоит из допустимых символов:
    - строчные латинские буквы (исключая 'l')
    - прописные латинские буквы (исключая 'I' и 'O')
    - цифры (исключая '1' и '0')

    Обязательные требования к паролю:
    - как минимум одна цифра
    - как минимум одна строчная буква
    - как минимум одна прописная буква

    Аргументы:
        m (int): длина пароля

    Возвращает:
        str: сгенерированный пароль
    """
    # Определяем допустимые символы, исключая "опасные" (легко перепутать)
    # Исключаем: 'l' (маленькая L), 'I' (большая i), '1' (цифра один),
    # 'o' (маленькая O), 'O' (большая o), '0' (цифра ноль)
    allowed_lower = [c for c in string.ascii_lowercase if c not in 'lo']  # исключаем 'l' и 'o'
    allowed_upper = [c for c in string.ascii_uppercase if c not in 'IO']  # исключаем 'I' и 'O'
    allowed_digits = [c for c in string.digits if c not in '10']          # исключаем '1' и '0'

    # Полный алфавит допустимых символов
    all_allowed = allowed_lower + allowed_upper + allowed_digits

    # Гарантируем, что в пароле будет хотя бы одна цифра, строчная и прописная буква
    # Выбираем по одному обязательному символу каждого типа
    password_parts = [
        random.choice(allowed_digits),   # как минимум одна цифра
        random.choice(allowed_lower),    # как минимум одна строчная буква
        random.choice(allowed_upper)     # как минимум одна прописная буква
    ]

    # Заполняем оставшиеся позиции (m - 3) случайными символами из всего допустимого набора
    for _ in range(m - 3):
        password_parts.append(random.choice(all_allowed))

    # Перемешиваем символы, чтобы обязательные символы не стояли всегда в начале
    random.shuffle(password_parts)

    # Возвращаем собранную строку
    return ''.join(password_parts)


def main(n: int, m: int) -> list[str]:
    """
    Генерирует список из n уникальных паролей длиной m символов каждый.

    Использует вспомогательную функцию generate_password() для создания
    каждого пароля и проверяет уникальность, чтобы все пароли были различны.

    Аргументы:
        n (int): количество требуемых паролей
        m (int): длина каждого пароля

    Возвращает:
        list[str]: список уникальных паролей
    """
    # Множество для хранения уже сгенерированных паролей (быстрая проверка уникальности)
    unique_passwords = set()

    # Список для хранения результата в порядке генерации
    passwords = []

    # Генерируем, пока не наберем n уникальных паролей
    while len(passwords) < n:
        # Создаем новый пароль
        candidate = generate_password(m)

        # Если такой пароль ещё не встречался, добавляем его
        if candidate not in unique_passwords:
            unique_passwords.add(candidate)
            passwords.append(candidate)

    return passwords


# Пример использования (можно раскомментировать для теста)
if __name__ == "__main__":
#     Генерируем 5 паролей длиной 10 символов
    result = main(25, 10)
for i, pwd in enumerate(result, 1):
    print(f"Пароль {i}: {pwd}")

