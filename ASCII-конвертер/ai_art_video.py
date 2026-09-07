import numpy as np
import pygame as pg
import cv2
import os


class ArtConverter:
    def __init__(self, path='video/madagaskar.mp4', font_size=4):
        # Инициализация Pygame
        pg.init()

        # Настройки ASCII - больше символов для лучшего качества
        self.ASCII_CHARS = ' .:-=+*#%@$&8WM'
        self.font_size = font_size
        self.ASCII_COEFF = 255 // (len(self.ASCII_CHARS) - 1)
        self.CHAR_STEP = max(2, int(font_size * 0.8))

        # Создаем шрифт
        try:
            self.font = pg.font.SysFont('Consolas', font_size, bold=True)
        except:
            self.font = pg.font.Font(None, font_size * 10)

        # Проверяем наличие видео
        self.video_path = path

        # Если видео не существует, создаем тестовое
        if not os.path.exists(self.video_path):
            print(f"Видео {self.video_path} не найдено!")
            if not os.path.exists('video'):
                os.makedirs('video')
            self.create_video()
            self.video_path = 'video/test_video.mp4'

        # Открываем видео
        self.cap = cv2.VideoCapture(self.video_path)

        if not self.cap.isOpened():
            print(f"Не удалось открыть видео: {self.video_path}")
            self.create_video()
            self.cap = cv2.VideoCapture('video/test_video.mp4')

        # Получаем информацию о видео
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Видео: {self.video_path}")
        print(f"FPS: {self.fps}, Кадров: {self.total_frames}")

        # Получаем первый кадр для определения размера
        ret, frame = self.cap.read()
        if not ret:
            print("Ошибка чтения первого кадра!")
            frame = np.zeros((300, 400, 3), dtype=np.uint8)

        # НЕ транспонируем! Просто берем как есть
        height, width = frame.shape[:2]

        # Уменьшаем размер для скорости
        self.scale = 1
        max_size = 600
        if width > max_size or height > max_size:
            self.scale = max(width / max_size, height / max_size)
            new_w = int(width / self.scale)
            new_h = int(height / self.scale)
            frame = cv2.resize(frame, (new_w, new_h))
            height, width = frame.shape[:2]

        # Сохраняем размеры
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()

        # Переменные для записи
        self.recording = False
        self.video_writer = None
        self.frame_count = 0

        # Создаем палитру
        self.create_palette()

        # Возвращаемся к началу видео
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        print(f"Размер экрана: {width}x{height}")
        print("Управление:")
        print("  R - Запись видео")
        print("  ESC - Выход")
        print("  SPACE - Изменить размер шрифта")
        print("  F - Переключить режим (цветной/черно-белый)")

    def create_video(self):
        """Создание тестового видео"""
        print("Создание тестового видео...")
        if not os.path.exists('video'):
            os.makedirs('video')

        fps = 30
        duration = 10
        total_frames = fps * duration
        w, h = 640, 480

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('video/test_video.mp4', fourcc, fps, (w, h))

        for i in range(total_frames):
            img = np.zeros((h, w, 3), dtype=np.uint8)

            # Движущийся градиент
            for y in range(h):
                for x in range(w):
                    img[y, x] = [(x + i * 2) % 255, (y + i * 3) % 255, (i * 4) % 255]

            # Движущийся круг
            cx = int(w / 2 + 150 * np.sin(i * 0.05))
            cy = int(h / 2 + 100 * np.cos(i * 0.04))
            cv2.circle(img, (cx, cy), 80, (0, 255, 255), -1)

            # Текст
            cv2.putText(img, f"Frame {i}", (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
            cv2.putText(img, "ASCII ART CONVERTER", (50, 180),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
            cv2.putText(img, "Press R to record", (50, 280),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            out.write(img)

        out.release()
        print("Тестовое видео создано: video/test_video.mp4")

    def create_palette(self):
        """Создание палитры символов"""
        self.palette = {}
        self.color_mode = 'color'  # 'color' или 'gray'

        # Создаем палитру для каждого символа
        for char in self.ASCII_CHARS:
            self.palette[char] = {}
            # Для каждого цвета создаем рендеринг
            for r in range(0, 256, 64):
                for g in range(0, 256, 64):
                    for b in range(0, 256, 64):
                        color = (r, g, b)
                        try:
                            self.palette[char][color] = self.font.render(char, True, color)
                        except:
                            self.palette[char][color] = self.font.render(char, True, (255, 255, 255))

    def get_frame(self):
        """Получение следующего кадра"""
        ret, frame = self.cap.read()
        if not ret:
            # Перематываем видео
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = self.cap.read()
            if not ret:
                frame = np.zeros((300, 400, 3), dtype=np.uint8)

        # НЕ транспонируем! Оставляем как есть
        # frame = cv2.transpose(frame)  # УБРАЛИ!

        # Изменяем размер под экран
        if self.scale > 1:
            new_w = int(frame.shape[1] / self.scale)
            new_h = int(frame.shape[0] / self.scale)
            frame = cv2.resize(frame, (new_w, new_h))

        return frame

    def draw(self):
        """Отрисовка кадра"""
        frame = self.get_frame()

        # Проверяем размер
        if frame.shape[1] != self.width or frame.shape[0] != self.height:
            frame = cv2.resize(frame, (self.width, self.height))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        self.screen.fill((0, 0, 0))

        # Отрисовка
        step = self.CHAR_STEP
        for y in range(0, self.height - step, step):
            for x in range(0, self.width - step, step):
                if y < self.height and x < self.width:
                    brightness = gray[y, x]
                    char_index = brightness // self.ASCII_COEFF
                    char_index = min(char_index, len(self.ASCII_CHARS) - 1)

                    if char_index > 0:
                        char = self.ASCII_CHARS[char_index]

                        if self.color_mode == 'color':
                            # Цветной режим
                            b, g, r = frame[y, x]
                            # Округляем цвета до ближайших в палитре
                            r = (r // 64) * 64
                            g = (g // 64) * 64
                            b = (b // 64) * 64
                            color = (r, g, b)
                        else:
                            # Черно-белый режим
                            color = (brightness, brightness, brightness)

                        # Отрисовка
                        try:
                            if char in self.palette:
                                # Ищем ближайший цвет
                                if color in self.palette[char]:
                                    self.screen.blit(self.palette[char][color], (x, y))
                                else:
                                    # Используем белый если цвет не найден
                                    white_color = (255, 255, 255)
                                    if white_color in self.palette[char]:
                                        self.screen.blit(self.palette[char][white_color], (x, y))
                        except:
                            pass

    def toggle_color_mode(self):
        """Переключение режима цвета"""
        if self.color_mode == 'color':
            self.color_mode = 'gray'
            print("Режим: Черно-белый")
        else:
            self.color_mode = 'color'
            print("Режим: Цветной")

    def start_recording(self):
        """Начать запись"""
        if not self.recording:
            self.recording = True
            self.frame_count = 0
            filename = f'output/record_{np.random.randint(1000, 9999)}.mp4'
            self.video_writer = cv2.VideoWriter(
                filename,
                cv2.VideoWriter_fourcc(*'mp4v'),
                30,
                (self.width, self.height)
            )
            print(f"Запись начата: {filename}")

    def stop_recording(self):
        """Остановить запись"""
        if self.recording:
            self.recording = False
            if self.video_writer:
                self.video_writer.release()
                self.video_writer = None
            print(f"Запись остановлена. Кадров: {self.frame_count}")

    def record_frame(self):
        """Запись текущего кадра"""
        if self.recording and self.video_writer:
            try:
                frame = pg.surfarray.array3d(self.screen)
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                frame = cv2.transpose(frame)
                self.video_writer.write(frame)
                self.frame_count += 1
            except Exception as e:
                print(f"Ошибка записи: {e}")

    def run(self):
        """Основной цикл"""
        running = True
        fps_counter = 0
        fps_display = 0
        last_time = pg.time.get_ticks()
        frame_number = 0

        while running:
            # Обработка событий
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        if not self.recording:
                            self.start_recording()
                        else:
                            self.stop_recording()
                    elif event.key == pg.K_ESCAPE:
                        running = False
                    elif event.key == pg.K_SPACE:
                        # Меняем размер шрифта
                        if self.CHAR_STEP < 10:
                            self.CHAR_STEP += 1
                        else:
                            self.CHAR_STEP = 2
                        print(f"Шаг: {self.CHAR_STEP}")
                    elif event.key == pg.K_f:
                        # Переключение цветного/черно-белого
                        self.toggle_color_mode()

            # Отрисовка
            self.draw()

            # Запись
            if self.recording:
                self.record_frame()

            # Подсчет FPS
            fps_counter += 1
            frame_number += 1
            current_time = pg.time.get_ticks()
            if current_time - last_time > 1000:
                fps_display = fps_counter
                fps_counter = 0
                last_time = current_time

            # Обновление экрана
            mode = "Color" if self.color_mode == 'color' else "Gray"
            status = f"ASCII | FPS: {fps_display} | Rec: {'ON' if self.recording else 'OFF'} | Mode: {mode} | Step: {self.CHAR_STEP}"
            pg.display.set_caption(status)
            pg.display.flip()
            self.clock.tick(30)

        # Очистка
        if self.recording:
            self.stop_recording()
        self.cap.release()
        pg.quit()
        print("Программа завершена")


if __name__ == '__main__':
    try:
        # Указываем путь к вашему видео
        video_path = 'video/madagaskar.mp4'

        # Если видео не существует, создаем тестовое
        if not os.path.exists(video_path):
            print(f"Видео {video_path} не найдено!")
            if not os.path.exists('video'):
                os.makedirs('video')
            print("Создаю тестовое видео...")

        app = ArtConverter(path=video_path, font_size=4)
        app.run()

    except Exception as e:
        print(f"Ошибка: {e}")
        import traceback

        traceback.print_exc()
        input("Нажмите Enter для выхода...")