import tkinter as tk
from tkinter import messagebox
import unittest


# ==========================================
# 1. ФУНКЦИИ ПРОВЕРКИ (Логика)
# ==========================================

def is_valid_name(name):
    """
    Проверяет имя на наличие цифр и других знаков.
    Возвращает True, если имя состоит только из букв и пробелов.
    """
    # Убираем пробелы и проверяем, что оставшаяся строка состоит только из букв
    return name.replace(" ", "").isalpha()


def is_valid_phone(phone):
    """
    Проверяет номер телефона.
    Разрешает только цифры, пробелы, знак плюса и дефис.
    """
    allowed_chars = set("0123456789 +-")
    # Проверяем, что каждый символ в строке входит в разрешенный набор
    return all(char in allowed_chars for char in phone) and len(phone) > 0


# ==========================================
# 2. ЛОГИКА ИНТЕРФЕЙСА (Tkinter)
# ==========================================

def check_login():
    """Функция, вызываемая при нажатии кнопки 'Вход'"""
    name = entry_name.get()
    phone = entry_phone.get()

    # 1. Проверка имени (согласно второму слайду)
    if not is_valid_name(name):
        messagebox.showwarning("Предупреждение", "Имя содержит цифры или другие знаки! Введите только буквы.")
        return  # Прерываем выполнение, если имя неверное

    # 2. Проверка номера телефона (запускается только если имя верное)
    if not is_valid_phone(phone):
        messagebox.showwarning("Предупреждение", "Номер телефона содержит недопустимые символы!")
        return

    # 3. Если обе проверки пройдены (согласно второму слайду)
    root.title("Всё верно!")


# --- Создание визуального интерфейса (согласно первому слайду) ---
root = tk.Tk()
root.title("Форма входа")
root.geometry("350x250")
root.configure(bg="#f0f0f0")

# Заголовок
label_title = tk.Label(root, text="Форма входа", font=("Arial", 14, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

# Поле "Имя"
label_name = tk.Label(root, text="Имя", bg="#f0f0f0", anchor="w")
label_name.pack(fill="x", padx=20)
entry_name = tk.Entry(root)
entry_name.pack(fill="x", padx=20, pady=5)

# Поле "Номер телефона"
label_phone = tk.Label(root, text="Номер телефона", bg="#f0f0f0", anchor="w")
label_phone.pack(fill="x", padx=20)
entry_phone = tk.Entry(root)
entry_phone.pack(fill="x", padx=20, pady=5)

# Кнопка "Вход"
btn_login = tk.Button(root, text="Вход", bg="#7c4dff", fg="white", font=("Arial", 10, "bold"), command=check_login)
btn_login.pack(pady=20, fill="x", padx=20)


# ==========================================
# 3. ТЕСТЫ (Согласно второму слайду)
# ==========================================

class TestValidationFunctions(unittest.TestCase):

    # Тесты для имени
    def test_name_valid(self):
        """Тест: корректное имя должно проходить проверку"""
        self.assertTrue(is_valid_name("Иван"))
        self.assertTrue(is_valid_name("Анна Мария"))

    def test_name_invalid(self):
        """Тест: имя с цифрами или знаками не должно проходить проверку"""
        self.assertFalse(is_valid_name("Иван123"))
        self.assertFalse(is_valid_name("Иван!"))

    # Тесты для телефона
    def test_phone_valid(self):
        """Тест: корректный номер телефона"""
        self.assertTrue(is_valid_phone("+7 900 123 45 67"))
        self.assertTrue(is_valid_phone("89001234567"))

    def test_phone_invalid(self):
        """Тест: телефон с буквами или недопустимыми символами"""
        self.assertFalse(is_valid_phone("+7 900 ABC 45 67"))
        self.assertFalse(is_valid_phone("8900(123)"))


if __name__ == "__main__":
    # Если запускаем файл напрямую, открывается интерфейс программы
    root.mainloop()

    # Чтобы запустить тесты, в терминале нужно выполнить команду:
    # python -m unittest main.py