""" ВЫ сели за руль автомобиля. Завели, прогрели,
поехали. В процессе передвижения случаются простои (светофоры,
пробки и.т.д.)  Написать модель хронометра, который
после прибытия в место назначения и выключения двигателя
покажет в консоли общее время движения и общее время стоянки.
Имитация датчика движения: единица в консоли - движение,
0 - стоянка, EXIT - выключение двигателя. Используем time.time()
 для фиксации временных меток.
"""
import time  # Для работы со временем и временными метками
from tkinter import *
from tkinter import ttk, messagebox  # ttk для стилизованных виджетов, messagebox для диалогов


class CarChronometer:
    """
    Класс, реализующий логику хронометра автомобиля
    Отслеживает состояние движения/стоянки и накапливает время
    """

    def __init__(self):
        """
        Инициализация начальных параметров хронометра
        """
        # Флаг, указывает, запущен ли процесс (движение или стоянка)
        # False - процесс не запущен, True - процесс активен
        self.is_running = False

        # Текущий режим: None - не определен, 'moving' - движение, 'stopped' - стоянка
        self.current_mode = None

        # Время начала текущего режима (фиксируется time.time())
        self.mode_start_time = 0

        # Общее накопленное время движения в секундах
        self.total_moving_time = 0.0

        # Общее накопленное время стоянки в секундах
        self.total_stopped_time = 0.0

        # Флаг для отслеживания выхода из программы
        self.is_exit = False

    def process_command(self, command):
        """
        Обработка введенной команды
        command: строка '1', '0' или 'EXIT'
        Возвращает строку с результатом или None при выходе
        """
        # Проверяем команду на выход
        if command.upper() == 'EXIT':
            # Если двигатель работал, фиксируем завершение текущего режима
            if self.is_running:
                self._stop_current_mode()
            self.is_exit = True
            return self.get_final_report()

        # Преобразуем команду к числу для проверки
        try:
            value = int(command)
        except ValueError:
            return "Ошибка: введите 1, 0 или EXIT"

        # Обработка команды в зависимости от значения
        if value == 1:  # Движение
            self._set_mode('moving')
            return "🚗 Движение начато..."
        elif value == 0:  # Стоянка
            self._set_mode('stopped')
            return "🚦 Стоянка начата..."
        else:
            return "Ошибка: введите 1, 0 или EXIT"

    def _set_mode(self, new_mode):
        """
        Установка нового режима (движение или стоянка)
        new_mode: 'moving' или 'stopped'
        """
        # Если уже находимся в этом режиме, ничего не делаем
        if self.current_mode == new_mode and self.is_running:
            return

        # Если был активен другой режим, завершаем его
        if self.is_running:
            self._stop_current_mode()

        # Фиксируем время начала нового режима
        self.current_mode = new_mode
        self.mode_start_time = time.time()  # time.time() возвращает текущее время в секундах с эпохи
        self.is_running = True

    def _stop_current_mode(self):
        """
        Завершение текущего режима и добавление времени к общему счетчику
        """
        if not self.is_running:
            return

        # Вычисляем продолжительность текущего режима
        current_time = time.time()
        duration = current_time - self.mode_start_time

        # Добавляем время к соответствующему общему счетчику
        if self.current_mode == 'moving':
            self.total_moving_time += duration
        elif self.current_mode == 'stopped':
            self.total_stopped_time += duration

        # Сбрасываем состояние режима
        self.is_running = False
        self.current_mode = None
        self.mode_start_time = 0

    def get_final_report(self):
        """
        Формирование итогового отчета по окончании поездки
        Возвращает строку с результатами
        """
        # Округляем время до 1 секунды для удобочитаемости
        moving_min = int(self.total_moving_time // 60)
        moving_sec = int(self.total_moving_time % 60)
        stopped_min = int(self.total_stopped_time // 60)
        stopped_sec = int(self.total_stopped_time % 60)

        # Формируем отчет
        report = (
            f"🏁 ПОЕЗДКА ЗАВЕРШЕНА 🏁\n"
            f"{'=' * 30}\n"
            f"⏱ Общее время движения: {moving_min} мин {moving_sec} сек\n"
            f"⏱ Общее время стоянки: {stopped_min} мин {stopped_sec} сек\n"
            f"📊 Общее время в пути: {moving_min + stopped_min} мин {(moving_sec + stopped_sec) % 60} сек"
        )
        return report

    def get_current_status(self):
        """
        Получение текущего статуса для отображения в интерфейсе
        """
        if self.is_exit:
            return "Двигатель выключен"
        if self.is_running:
            current_time = time.time()
            duration = current_time - self.mode_start_time
            mode_text = "Движение" if self.current_mode == 'moving' else "Стоянка"
            return f"🚗 {mode_text}... {int(duration)} сек"
        return "⏸ Двигатель заведен, ожидание команды"

    def reset(self):
        """
        Сброс всех параметров для новой поездки
        """
        if self.is_running:
            self._stop_current_mode()
        self.total_moving_time = 0.0
        self.total_stopped_time = 0.0
        self.is_exit = False
        self.current_mode = None
        self.is_running = False


# ============ ГРАФИЧЕСКИЙ ИНТЕРФЕЙС ============

class ChronometerGUI:
    """
    Класс для управления графическим интерфейсом хронометра
    """

    def __init__(self, root):
        """
        Инициализация GUI
        root: корневое окно Tkinter
        """
        self.root = root
        self.root.geometry('400x500')
        self.root.title('🚗 Хронометр автомобиля')
        self.root.resizable(False, False)

        # Создаем экземпляр хронометра
        self.chronometer = CarChronometer()

        # Создаем элементы интерфейса
        self._create_widgets()

        # Запускаем обновление статуса в реальном времени
        self._update_status()

    def _create_widgets(self):
        """
        Создание всех виджетов интерфейса
        """
        # Заголовок
        title_label = ttk.Label(
            self.root,
            text="ХРОНОМЕТР АВТОМОБИЛЯ",
            font=('Arial', 14, 'bold')
        )
        title_label.pack(pady=10)

        # Инструкция
        instr_label = ttk.Label(
            self.root,
            text="Команды:\n1 - движение\n0 - стоянка\nEXIT - выключение двигателя",
            justify=CENTER,
            font=('Arial', 10)
        )
        instr_label.pack(pady=5)

        # Разделитель
        ttk.Separator(self.root, orient='horizontal').pack(fill=X, padx=10, pady=10)

        # Поле для ввода команды
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Команда:").pack(side=LEFT, padx=5)

        # Поле ввода
        self.entry_var = StringVar()
        self.entry = ttk.Entry(
            input_frame,
            textvariable=self.entry_var,
            width=15,
            font=('Arial', 12)
        )
        self.entry.pack(side=LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self._process_input())  # Enter для отправки
        self.entry.focus()  # Фокус на поле ввода

        # Кнопка отправки
        self.send_btn = ttk.Button(
            self.root,
            text="▶ Отправить",
            command=self._process_input
        )
        self.send_btn.pack(pady=5)

        # Кнопка сброса
        self.reset_btn = ttk.Button(
            self.root,
            text="🔄 Новая поездка (сброс)",
            command=self._reset_chronometer
        )
        self.reset_btn.pack(pady=5)

        # Разделитель
        ttk.Separator(self.root, orient='horizontal').pack(fill=X, padx=10, pady=10)

        # Статус
        status_frame = ttk.LabelFrame(self.root, text="📊 Текущий статус")
        status_frame.pack(fill=X, padx=10, pady=5)

        self.status_label = ttk.Label(
            status_frame,
            text="⏸ Двигатель заведен, ожидание команды",
            font=('Arial', 11),
            wraplength=350,
            justify=CENTER
        )
        self.status_label.pack(pady=10)

        # Разделитель
        ttk.Separator(self.root, orient='horizontal').pack(fill=X, padx=10, pady=10)

        # Статистика
        stats_frame = ttk.LabelFrame(self.root, text="📈 Накопленная статистика")
        stats_frame.pack(fill=X, padx=10, pady=5)

        self.stats_label = ttk.Label(
            stats_frame,
            text="Движение: 0 сек\nСтоянка: 0 сек",
            font=('Arial', 10),
            justify=CENTER
        )
        self.stats_label.pack(pady=10)

        # Разделитель
        ttk.Separator(self.root, orient='horizontal').pack(fill=X, padx=10, pady=10)

        # Кнопка выхода
        exit_btn = ttk.Button(
            self.root,
            text="❌ Выход",
            command=self._exit_program
        )
        exit_btn.pack(pady=5)

    def _process_input(self):
        """
        Обработка введенной команды
        """
        command = self.entry_var.get().strip()

        # Проверяем, что команда не пустая
        if not command:
            return

        # Очищаем поле ввода
        self.entry_var.set("")
        self.entry.focus()

        # Проверяем, не завершена ли уже поездка
        if self.chronometer.is_exit and command.upper() != 'EXIT':
            messagebox.showinfo(
                "Информация",
                "Двигатель уже выключен. Нажмите 'Новая поездка' для сброса."
            )
            return

        # Обрабатываем команду
        result = self.chronometer.process_command(command)

        # Проверяем, не был ли это выход
        if self.chronometer.is_exit:
            # Показываем итоговый отчет
            messagebox.showinfo(
                "🏁 Поездка завершена",
                result,
                icon='info'
            )
            # Обновляем статус
            self._update_status()
            return

        # Показываем результат в статусе
        self._update_status()

        # Если была ошибка, показываем её
        if "Ошибка" in result:
            messagebox.showerror("Ошибка ввода", result)

    def _update_status(self):
        """
        Обновление информации на экране
        """
        # Обновляем статус
        status_text = self.chronometer.get_current_status()
        self.status_label.config(text=status_text)

        # Обновляем статистику
        moving = self.chronometer.total_moving_time
        stopped = self.chronometer.total_stopped_time
        self.stats_label.config(
            text=f"🚗 Движение: {int(moving)} сек ({int(moving // 60)} мин)\n"
                 f"🅿 Стоянка: {int(stopped)} сек ({int(stopped // 60)} мин)"
        )

        # Если двигатель выключен, меняем цвет кнопки
        if self.chronometer.is_exit:
            self.send_btn.config(state='disabled')
        else:
            self.send_btn.config(state='normal')

        # Планируем следующее обновление через 1 секунду
        if not self.chronometer.is_exit:
            self.root.after(1000, self._update_status)
        else:
            # Если завершено, еще одно обновление через 1 секунду для отображения финального статуса
            self.root.after(1000, lambda: self.status_label.config(text="🏁 Двигатель выключен"))

    def _reset_chronometer(self):
        """
        Сброс хронометра для новой поездки
        """
        if self.chronometer.is_running:
            # Если что-то работает, спрашиваем подтверждение
            if not messagebox.askyesno("Сброс", "Сбросить текущую поездку? Время будет потеряно."):
                return

        # Сбрасываем хронометр
        self.chronometer.reset()

        # Восстанавливаем кнопку отправки
        self.send_btn.config(state='normal')

        # Обновляем интерфейс
        self._update_status()

        # Очищаем поле ввода
        self.entry_var.set("")
        self.entry.focus()

        messagebox.showinfo("Сброс", "Хронометр сброшен. Начинайте новую поездку.")

    def _exit_program(self):
        """
        Выход из программы
        """
        if messagebox.askyesno("Выход", "Вы уверены, что хотите выйти?"):
            self.root.quit()
            self.root.destroy()


# ============ ЗАПУСК ПРОГРАММЫ ============

if __name__ == "__main__":
    # Создаем корневое окно
    root = Tk()

    # Создаем экземпляр GUI
    app = ChronometerGUI(root)

    # Запускаем главный цикл Tkinter
    root.mainloop()
