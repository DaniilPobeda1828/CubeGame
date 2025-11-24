import tkinter as tk
from tkinter import ttk
import random
import time


def roll_dice():
    """
    Функция генерации случайного числа от 1 до 6
    
    Returns:
        int: Случайное число от 1 до 6 (результат броска кубика)
    """
    return random.randint(1, 6)


class DiceGame:
    """
    Основной класс приложения игрового кубика.
    
    Отвечает за создание графического интерфейса и управление
    игровой логикой.
    """
    
    def __init__(self, root):
        """
        Инициализация главного окна приложения.
        
        Args:
            root (tk.Tk): Корневое окно Tkinter
        """
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.initialize_game()
    
    def setup_window(self):
        """Настройка параметров главного окна"""
        self.root.title("CubeGame - Бросок кубика")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
    
    def create_widgets(self):
        """Создание и размещение элементов интерфейса"""
        # Заголовок приложения
        title_label = tk.Label(
            self.root,
            text="🎲 ИГРОВОЙ КУБИК 🎲",
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=20)
        
        # Область отображения кубика
        self.create_dice_area()
        
        # Панель управления
        self.create_control_panel()
        
        # Область статистики
        self.create_stats_area()
    
    def create_dice_area(self):
        """Создание области отображения кубика"""
        dice_frame = tk.Frame(self.root, bg='#ffffff', relief='raised', bd=3)
        dice_frame.pack(pady=20, padx=50, fill='both', expand=True)
        
        # Отображение текущего значения кубика
        self.dice_label = tk.Label(
            dice_frame,
            text="🎲",
            font=("Arial", 80),
            bg='white'
        )
        self.dice_label.pack(pady=30)
        
        # Метка результата
        self.result_label = tk.Label(
            dice_frame,
            text="Нажмите кнопку для броска",
            font=("Arial", 14),
            bg='white',
            fg='#7f8c8d'
        )
        self.result_label.pack(pady=10)
    
    def create_control_panel(self):
        """Создание панели управления"""
        control_frame = tk.Frame(self.root, bg='#f0f0f0')
        control_frame.pack(pady=20)
        
        # Основная кнопка броска
        self.roll_button = tk.Button(
            control_frame,
            text="🎲 БРОСИТЬ КУБИК 🎲",
            command=self.roll_dice,
            font=("Arial", 14, "bold"),
            bg='#3498db',
            fg='white',
            padx=30,
            pady=15,
            cursor='hand2',
            relief='raised',
            bd=3
        )
        self.roll_button.pack()
    
    def create_stats_area(self):
        """Создание области статистики"""
        stats_frame = tk.LabelFrame(
            self.root,
            text=" 📊 СТАТИСТИКА ИГРЫ ",
            font=("Arial", 12, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        stats_frame.pack(pady=10, padx=50, fill='x')
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Всего бросков: 0",
            font=("Arial", 11),
            bg='#f0f0f0'
        )
        self.stats_label.pack(pady=10)
    
    def initialize_game(self):
        """Инициализация игровых переменных"""
        self.roll_count = 0
        self.current_value = 0
        
        # Символы кубиков для отображения
        self.dice_symbols = {
            1: "⚀", 2: "⚁", 3: "⚂", 
            4: "⚃", 5: "⚄", 6: "⚅"
        }
    
    def roll_dice(self):
        """
        Основная функция броска кубика с анимацией
        
        Включает генерацию случайного числа и визуальную
        анимацию вращения кубика.
        """
        # Блокировка кнопки во время анимации
        self.roll_button.config(state='disabled')
        self.result_label.config(text="Кубик вращается...")
        
        # Воспроизведение анимации
        self.animate_roll()
        
        # Генерация финального результата
        self.current_value = roll_dice()
        
        # Обновление интерфейса
        self.update_display()
        self.update_stats()
        
        # Разблокировка кнопки
        self.roll_button.config(state='normal')
    
    def animate_roll(self):
        """
        Анимация вращения кубика
        
        Создает визуальный эффект случайного вращения
        путем быстрой смены значений.
        """
        for i in range(12):
            temp_value = random.randint(1, 6)
            self.dice_label.config(text=self.dice_symbols[temp_value])
            self.root.update()
            time.sleep(0.08)
    
    def update_display(self):
        """Обновление отображения результата на экране"""
        self.dice_label.config(text=self.dice_symbols[self.current_value])
        self.result_label.config(text=f"Выпало: {self.current_value}")
    
    def update_stats(self):
        """Обновление статистики бросков"""
        self.roll_count += 1
        self.stats_label.config(text=f"Всего бросков: {self.roll_count}")


def main():
    """
    Главная функция запуска приложения.
    
    Создает экземпляр Tkinter и запускает главный цикл
    обработки событий.
    """
    try:
        root = tk.Tk()
        app = DiceGame(root)
        root.mainloop()
    except Exception as e:
        print(f"Ошибка запуска приложения: {e}")


# Точка входа в программу
if __name__ == "__main__":
    main()