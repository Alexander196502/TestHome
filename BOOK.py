import os

HISTORY_FILE = "calculations.txt"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def save_calculation(expression, result):
    """Сохраняет вычисление в файл"""
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"Результат: {expression} = {result}\n")

def show_history():
    """Показывает историю вычислений из файла"""
    if not os.path.exists(HISTORY_FILE):
        print("История вычислений пуста (файл не найден).")
        return

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = file.readlines()

        if not history:
            print("История вычислений пуста.")
        else:
            print("\nИстория вычислений:")
            for line in history:
                print(line.strip())
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def get_number(prompt):
    """Получает число от пользователя с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("Калькулятор с историей вычислений")
    print("=" * 40)

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Просмотр истории вычислений")
        print("0. Выход")

        choice = input("\nВведите номер операции (1/2/3/4/5/0): ").strip()

        if choice == '0':
            print("Выход из программы. До свидания!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")

            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"

            expression = f"{num1} {operation} {num2}"
            print(f"\nРезультат: {expression} = {result}")

            # Сохраняем в историю только успешные вычисления
            if isinstance(result, (int, float)):
                save_calculation(expression, result)

        elif choice == '5':
            show_history()

        else:
            print("Неверный выбор! Пожалуйста, выберите 1, 2, 3, 4, 5 или 0.")

if __name__ == "__main__":
    main()