import pygame
import pygame.gfxdraw

# Инициализация
pygame.init()

# Размер одного квадратика (пиксель-арт-блока)
CELL_SIZE = 20
# Количество ячеек по горизонтали и вертикали
COLS = 20
ROWS = 15

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пиксель-арт в Ривенделле")

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Пример "карты" пикселей (матрица цветов)
# Для простоты используем буквы: 'r' = красный, 'g' = зелёный, 'b' = синий, 'y' = жёлтый, 'p' = фиолетовый, '.' = чёрный
pixel_map = [
    "rrrrr....rrrrr",
    "r...r....r...r",
    "r...r....r...r",
    "rrrrr....rrrrr",
    "r...........r",
    "r...........r",
    "r...........r",
    "yyyyyyyyyyyyyyy",
    "y...........y",
    "y...........y",
    "y...........y",
    "y...........y",
    "yyyyyyyyyyyyyyy",
    "bbbbbbbbbbbbbbb",
    "b.........b",
]

# Преобразование символов в RGB-цвета
color_map = {
    'r': RED,
    'g': GREEN,
    'b': BLUE,
    'y': YELLOW,
    'p': PURPLE,
    '.': BLACK,
}

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливка фона (необязательно, всё равно перекроем)
    screen.fill(WHITE)

    # Рисуем квадратики через gfxdraw.box()
    for row_idx, row in enumerate(pixel_map):
        for col_idx, char in enumerate(row):
            color = color_map.get(char, BLACK)
            x = col_idx * CELL_SIZE
            y = row_idx * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.gfxdraw.box(screen, rect, color)

    pygame.display.flip()

pygame.quit()