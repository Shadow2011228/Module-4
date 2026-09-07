# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QMessageBox
from loguru import logger as log
from PIL import Image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Кнопка загрузки
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 181, 61))
        self.pushButton.setStyleSheet("""
            QPushButton {
                font: 75 14pt "MS Shell Dlg 2";
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.pushButton.setObjectName("pushButton")

        # Слайдер размера шрифта
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 140, 161, 31))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(30)
        self.horizontalSlider.setValue(2)

        # Кнопка черно-белого
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 210, 181, 61))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                font: 75 14pt "MS Shell Dlg 2";
                background-color: #555555;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:pressed {
                background-color: #444444;
            }
        """)
        self.pushButton_2.setObjectName("pushButton_2")

        # Кнопка цветного
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 290, 181, 61))
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                font: 75 14pt "MS Shell Dlg 2";
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1e87db;
            }
            QPushButton:pressed {
                background-color: #1a78c2;
            }
        """)
        self.pushButton_4.setObjectName("pushButton_4")

        # Кнопка сохранения
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 430, 181, 61))
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                font: 75 14pt "MS Shell Dlg 2";
                background-color: #FF9800;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #e68a00;
            }
            QPushButton:pressed {
                background-color: #cc7a00;
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")

        # Кнопка сброса
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 520, 181, 61))
        self.pushButton_5.setStyleSheet("""
            QPushButton {
                font: 75 14pt "MS Shell Dlg 2";
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
            QPushButton:pressed {
                background-color: #c41608;
            }
        """)
        self.pushButton_5.setObjectName("pushButton_5")

        # Метка для отображения изображения
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 700, 680))
        self.label.setText("Загрузите изображение\n\nНажмите кнопку 'Загрузить фото'")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            border: 2px solid #cccccc;
            background-color: #f8f9fa;
            font-size: 18pt;
            color: #666;
            border-radius: 10px;
        """)
        self.label.setObjectName("label")

        # Метки для подписей
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 151, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #333;")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 161, 31))
        self.label_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #333;")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 370, 151, 21))
        self.label_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #333;")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 400, 200, 21))
        self.label_5.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #28a745;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 500, 181, 21))
        self.label_6.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #333;")
        self.label_6.setText("Действия:")
        self.label_6.setObjectName("label_6")

        # Метка для отображения текущего режима
        self.label_mode = QtWidgets.QLabel(self.centralwidget)
        self.label_mode.setGeometry(QtCore.QRect(20, 600, 181, 21))
        self.label_mode.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\"; color: #2196F3;")
        self.label_mode.setText("Режим: Цветной")
        self.label_mode.setObjectName("label_mode")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASCII Конвертер изображений"))
        self.pushButton.setText(_translate("MainWindow", "📁 Загрузить фото"))
        self.pushButton_2.setText(_translate("MainWindow", "⚫ Черно-белый"))
        self.pushButton_3.setText(_translate("MainWindow", "💾 Сохранить"))
        self.pushButton_4.setText(_translate("MainWindow", "🎨 Цветной"))
        self.pushButton_5.setText(_translate("MainWindow", "🔄 Сбросить"))
        self.label_2.setText(_translate("MainWindow", "Режим отображения:"))
        self.label_3.setText(_translate("MainWindow", "Размер шрифта (1-30):"))
        self.label_4.setText(_translate("MainWindow", "Глубина цвета: 8"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, path='img/wolf.jpg', font_size=2, color_lvl=8):
        super().__init__()
        self.setupUi(self)

        # Инициализация переменных
        self.path = path
        self.font_size = max(1, font_size)
        self.color_lvl = max(2, color_lvl)
        self.color_mode = 'color'  # 'color' или 'gray'
        self.ascii_image = None
        self.image_loaded = False
        self.current_file_path = None

        # Переменные для изображений
        self.gray_image = None
        self.rgb_image = None
        self.original_image = None

        # Параметры ASCII
        self.ASCII_CHARS = '@%#*+=-:. '
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)

        # Подключение сигналов
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_2.clicked.connect(self.apply_grayscale)
        self.pushButton_4.clicked.connect(self.apply_color)
        self.pushButton_3.clicked.connect(self.save_image)
        self.pushButton_5.clicked.connect(self.reset_image)
        self.horizontalSlider.valueChanged.connect(self.change_font_size)

        # Устанавливаем начальное значение слайдера
        self.horizontalSlider.setValue(self.font_size)
        self.label_3.setText(f"Размер шрифта ({self.font_size}):")

        # Показываем приглашение
        self.label.setText("Загрузите изображение\n\nНажмите кнопку '📁 Загрузить фото'")
        self.label_5.setText("Готов к загрузке")
        self.label_mode.setText("Режим: Цветной")

    def get_desktop_path(self):
        """Получение пути к рабочему столу"""
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if os.path.exists(desktop):
                return desktop
            desktop = os.path.join(os.path.expanduser("~"), "Рабочий стол")
            if os.path.exists(desktop):
                return desktop
            return os.path.expanduser("~")
        except:
            return os.path.expanduser("~")

    def open_file_dialog(self):
        """Открытие диалога выбора файла с компьютера"""
        desktop_path = self.get_desktop_path()

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            desktop_path,
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.tif *.webp *.ico);;Все файлы (*.*)"
        )

        if file_path:
            try:
                file_size = os.path.getsize(file_path) / (1024 * 1024)
                if file_size > 50:
                    reply = QMessageBox.question(
                        self,
                        "Большой файл",
                        f"Файл размером {file_size:.1f} МБ. Это может занять время.\nПродолжить?",
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )
                    if reply == QMessageBox.No:
                        return
            except:
                pass

            self.load_image(file_path)
        else:
            self.label.setText("Выбор отменён")

    def load_image(self, path):
        """Загрузка изображения с поворотом через BGR2RGB"""
        try:
            self.current_file_path = path
            self.label_5.setText(f"Загрузка: {os.path.basename(path)}...")

            log.info(f"Загрузка изображения: {path}")

            if not os.path.exists(path):
                self.label.setText(f"❌ Файл не найден\n{os.path.basename(path)}")
                self.image_loaded = False
                self.label_5.setText("Ошибка: файл не найден")
                return

            if os.path.getsize(path) == 0:
                self.label.setText(f"❌ Файл пустой\n{os.path.basename(path)}")
                self.image_loaded = False
                self.label_5.setText("Ошибка: файл пустой")
                return

            # Пробуем загрузить через OpenCV
            cv2_image = cv2.imread(path)

            # Если OpenCV не смог загрузить, пробуем через PIL
            if cv2_image is None:
                try:
                    log.info("Попытка загрузки через PIL...")
                    pil_image = Image.open(path)
                    if pil_image.mode == 'RGBA':
                        pil_image = pil_image.convert('RGB')
                    pil_array = np.array(pil_image)
                    cv2_image = cv2.cvtColor(pil_array, cv2.COLOR_RGB2BGR)
                    log.info("Изображение успешно загружено через PIL")
                except Exception as pil_error:
                    log.error(f"Ошибка загрузки через PIL: {pil_error}")
                    self.label.setText(f"❌ Не удалось загрузить изображение\n{os.path.basename(path)}")
                    self.image_loaded = False
                    self.label_5.setText("Ошибка: неподдерживаемый формат")
                    return

            if cv2_image is None:
                self.label.setText(f"❌ Не удалось загрузить\n{os.path.basename(path)}")
                self.image_loaded = False
                self.label_5.setText("Ошибка: файл поврежден")
                return

            if cv2_image.shape[0] == 0 or cv2_image.shape[1] == 0:
                self.label.setText(f"❌ Изображение повреждено\n{os.path.basename(path)}")
                self.image_loaded = False
                self.label_5.setText("Ошибка: изображение повреждено")
                return

            # ПОВОРОТ ИЗОБРАЖЕНИЯ ЧЕРЕЗ BGR2RGB
            # Конвертируем BGR в RGB для правильного отображения
            rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

            # Сохраняем оригинальное изображение (уже в RGB)
            self.original_image = rgb_image.copy()

            # Для ASCII используем BGR изображение (транспонируем для правильной ориентации)
            transposed = cv2.transpose(cv2_image)
            self.gray_image = cv2.cvtColor(transposed, cv2.COLOR_BGR2GRAY)

            # RGB изображение для цветного режима (транспонируем для правильной ориентации)
            rgb_transposed = cv2.transpose(rgb_image)
            self.rgb_image = rgb_transposed

            # Отмечаем, что изображение загружено
            self.image_loaded = True

            # Сразу создаем и показываем ASCII арт
            self.create_ascii_art()

            self.label_5.setText(f"✅ Загружено: {os.path.basename(path)}")

            h, w = cv2_image.shape[:2]
            self.statusBar().showMessage(f"Размер: {w}x{h} пикселей")

        except Exception as e:
            log.error(f"Ошибка загрузки: {e}")
            self.label.setText(f"❌ Ошибка: {str(e)}")
            self.image_loaded = False
            self.label_5.setText("Ошибка загрузки")

    def create_ascii_art(self):
        """Создание ASCII арта"""
        if self.gray_image is None or not self.image_loaded:
            return

        try:
            ascii_image = self.convert_to_ascii()

            if ascii_image is not None:
                self.ascii_image = ascii_image
                self.display_ascii(ascii_image)

        except Exception as e:
            log.error(f"Ошибка создания ASCII: {e}")
            self.label.setText(f"❌ Ошибка: {str(e)}")

    def convert_to_ascii(self):
        """Конвертация в ASCII"""
        try:
            height, width = self.gray_image.shape

            char_step = max(1, self.font_size)

            new_height = max(1, height // char_step)
            new_width = max(1, width // char_step)

            gray_resized = cv2.resize(self.gray_image, (new_width, new_height))

            if self.color_mode == 'color' and self.rgb_image is not None:
                rgb_resized = cv2.resize(self.rgb_image, (new_width, new_height))

            # Создаем ASCII строку
            ascii_lines = []
            colors = []

            for y in range(new_height):
                line = ""
                color_line = []
                for x in range(new_width):
                    pixel_value = gray_resized[y, x]
                    char_index = int(pixel_value // self.ASCII_COEFF)
                    char_index = min(char_index, len(self.ASCII_CHARS) - 1)
                    line += self.ASCII_CHARS[char_index]

                    if self.color_mode == 'color' and self.rgb_image is not None:
                        color_line.append(tuple(rgb_resized[y, x]))
                    else:
                        color_line.append((0, 0, 0))

                ascii_lines.append(line)
                colors.append(color_line)

            # Создаем изображение из текста с цветами
            return self.create_image_from_text(ascii_lines, colors)

        except Exception as e:
            log.error(f"Ошибка конвертации: {e}")
            return None

    def create_image_from_text(self, lines, colors=None):
        """Создание изображения из текста с цветами"""
        try:
            if not lines:
                return None

            max_width = max(len(line) for line in lines) if lines else 1
            text_height = len(lines)

            font_scale = max(0.2, self.font_size / 20)
            thickness = max(1, self.font_size // 6)

            img_width = max(100, max_width * self.font_size * 2)
            img_height = max(100, text_height * self.font_size * 3)

            # Создаем изображение с белым фоном
            img = np.ones((img_height, img_width, 3), dtype=np.uint8) * 255

            # Рисуем текст с цветами
            y_pos = self.font_size * 2
            for i, line in enumerate(lines):
                if y_pos < img_height:
                    # Если есть цвета, рисуем каждый символ с его цветом
                    if colors and i < len(colors):
                        x_pos = 10
                        for j, char in enumerate(line):
                            if j < len(colors[i]):
                                color = colors[i][j]
                                if self.color_mode == 'gray':
                                    color = (0, 0, 0)
                                cv2.putText(img, char, (x_pos, y_pos),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            font_scale,
                                            (int(color[0]), int(color[1]), int(color[2])),
                                            thickness,
                                            cv2.LINE_AA)
                                x_pos += int(self.font_size * 1.2)
                    else:
                        # Если цветов нет, рисуем черным
                        cv2.putText(img, line, (10, y_pos),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    font_scale,
                                    (0, 0, 0),
                                    thickness,
                                    cv2.LINE_AA)
                    y_pos += self.font_size * 2

            return img

        except Exception as e:
            log.error(f"Ошибка создания изображения: {e}")
            return None

    def display_ascii(self, image):
        """Отображение ASCII арта"""
        try:
            if image is None:
                return

            height, width = image.shape[:2]
            bytes_per_line = 3 * width

            qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)

            # Масштабируем с сохранением пропорций
            pixmap = pixmap.scaled(
                700, 680,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.label.setPixmap(pixmap)

        except Exception as e:
            log.error(f"Ошибка отображения: {e}")
            self.label.setText("❌ Ошибка отображения ASCII")

    def apply_grayscale(self):
        """Черно-белый режим"""
        if not self.image_loaded or self.gray_image is None:
            self.label.setText("⚠️ Сначала загрузите изображение")
            return

        self.color_mode = 'gray'
        self.create_ascii_art()
        self.label_5.setText("⚫ Черно-белый режим")
        self.label_mode.setText("Режим: Черно-белый")
        self.statusBar().showMessage("Черно-белый режим активирован")

    def apply_color(self):
        """Цветной режим"""
        if not self.image_loaded or self.gray_image is None:
            self.label.setText("⚠️ Сначала загрузите изображение")
            return

        self.color_mode = 'color'
        self.create_ascii_art()
        self.label_5.setText("🎨 Цветной режим")
        self.label_mode.setText("Режим: Цветной")
        self.statusBar().showMessage("Цветной режим активирован")

    def change_font_size(self, value):
        """Изменение размера шрифта"""
        self.font_size = max(1, value)
        self.label_3.setText(f"Размер шрифта ({self.font_size}):")
        if self.image_loaded and self.gray_image is not None:
            self.create_ascii_art()

    def reset_image(self):
        """Сброс изображения"""
        self.image_loaded = False
        self.gray_image = None
        self.rgb_image = None
        self.ascii_image = None
        self.current_file_path = None
        self.color_mode = 'color'

        self.label.setText("Загрузите изображение\n\nНажмите кнопку '📁 Загрузить фото'")
        self.label_5.setText("Изображение сброшено")
        self.label_mode.setText("Режим: Цветной")
        self.statusBar().showMessage("Готов к загрузке")

    def save_image(self):
        """Сохранение изображения"""
        try:
            if not self.image_loaded or self.label.pixmap() is None:
                self.label.setText("⚠️ Нет изображения для сохранения")
                return

            desktop_path = self.get_desktop_path()

            file_path, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить изображение",
                os.path.join(desktop_path, "ascii_art.png"),
                "Изображения (*.png *.jpg *.jpeg *.bmp);;Все файлы (*.*)"
            )

            if file_path:
                self.label.pixmap().save(file_path)
                self.label_5.setText(f"✅ Сохранено: {os.path.basename(file_path)}")
                self.statusBar().showMessage(f"Изображение сохранено: {file_path}")

        except Exception as e:
            log.error(f"Ошибка сохранения: {e}")
            self.label.setText(f"❌ Ошибка сохранения: {str(e)}")


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = Window(path='img/wolf.jpg', font_size=2, color_lvl=8)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()