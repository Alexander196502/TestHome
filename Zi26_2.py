
"""
Cоздать класс который по числу от 1 до 365 выдаст месяц, день, и день недели(Пн, Вт...)
 """


class DayOfYearSimple:
    """Класс для определения даты по номеру дня без использования datetime"""

    # Дни в месяцах для невисокосного года
    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_NAMES = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]
    WEEKDAY_NAMES = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    def __init__(self, day_number):
        """
        Инициализация с номером дня

        Args:
            day_number (int): номер дня от 1 до 365
        """
        if not 1 <= day_number <= 365:
            raise ValueError("Номер дня должен быть от 1 до 365")
        self.day_number = day_number
        self._calculate_date()

    def _calculate_date(self):
        """Вычисляет месяц, день и день недели"""
        # Определяем месяц и день месяца
        remaining = self.day_number
        for month_idx, days_in_month in enumerate(self.MONTH_DAYS):
            if remaining <= days_in_month:
                self.month = month_idx
                self.day = remaining
                break
            remaining -= days_in_month

        # Определяем день недели (1 января 2023 - воскресенье)
        # 2023-01-01 был воскресеньем (6 в индексации с Пн=0)
        # Но для простоты используем смещение
        # В 2023 году 1 января - воскресенье (Вс=6)
        # Поэтому (day_number + 5) % 7 даст Пн=0, Вт=1, ..., Вс=6
        self.weekday = (self.day_number + 5) % 7

    def get_month(self):
        """Возвращает название месяца"""
        return self.MONTH_NAMES[self.month]

    def get_day(self):
        """Возвращает день месяца"""
        return self.day

    def get_weekday(self):
        """Возвращает день недели (Пн, Вт, ...)"""
        return self.WEEKDAY_NAMES[self.weekday]

    def get_full_date(self):
        """Возвращает полную информацию"""
        return {
            'month': self.get_month(),
            'day': self.get_day(),
            'weekday': self.get_weekday(),
            'full': f"{self.get_weekday()}, {self.get_day()} {self.get_month()}"
        }

    def __str__(self):
        return f"{self.get_weekday()}, {self.get_day()} {self.get_month()}"

    def __repr__(self):
        return f"DayOfYearSimple({self.day_number})"


# Тестирование альтернативной версии
print("\n=== Альтернативная версия ===")
for day_num in [1, 32, 100, 180, 365]:
    d = DayOfYearSimple(day_num)
    print(f"День {day_num}: {d}")