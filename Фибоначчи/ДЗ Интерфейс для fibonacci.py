import tkinter as tk
import time
import fibonacci

class AlgorithmComparisionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x700")
        self.root.title("Ряд Фибоначчи")
        self.create_widgets()

    def create_widgets(self):
        # Увеличиваем размер шрифта для всех элементов
        font = ("Arial", 12)
        # Фрейм для центрирования виджетов
        center_frame = tk.Frame(self.root)
        center_frame.pack(expand=True)
        self.entry_label = tk.Label(center_frame, text="Введите число:", font=font)
        self.entry_label.pack()
        self.entry = tk.Entry(center_frame, font=font)
        self.entry.pack()
        self.run_button = tk.Button(center_frame, text="Запустить", command=self.run_algorithm, font=font)
        self.run_button.pack()
        # Многострочное поле для вывода результата с полосами прокрутки
        self.result_text = tk.Text(center_frame, wrap=tk.WORD, font=font, height=10, width=40)
        self.result_text.pack()
        self.time_label = tk.Label(center_frame, text="Время выполнения:", font=font)
        self.time_label.pack()

    def run_algorithm(self):
        input_number = int(self.entry.get())
        # Здесь нужно вызвать алгоритм и измерить время выполнения
        start_time = time.time()
        result = fibonacci.fibonacci(input_number)
        end_time = time.time()
        # Очищаем многострочное поле и выводим результат
        self.result_text.delete("1.0", tk.END)  # Очистка содержимого
        result = f"Результат: {result}\n"
        self.result_text.insert(tk.END, result)
        self.time_label.config(text=f"Время выполнения: {end_time - start_time:.6f} секунд")

if __name__ == "__main__":
    app = AlgorithmComparisionApp()
    app.root.mainloop()