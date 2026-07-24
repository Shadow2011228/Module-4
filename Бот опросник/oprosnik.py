import telebot                     # Импорт библиотеки для работы с Telegram Bot API
from telebot import types          # Импорт типов данных (клавиатуры, кнопки и т.д.)
from loguru import logger          # Импорт библиотеки для удобного логирования (вывод информации в консоль)
import db                          # Импорт нашего модуля db.py (работа с базой данных)

# Создание экземпляра бота с использованием токена (уникальный ключ для доступа к боту)
bot = telebot.TeleBot("8598431910:AAG8zvIUEk7E0N3v1eeOV3kKCtQ8FN6fJM4")
logger.success("Экземпляр бота создан")  # Логируем успешное создание бота

m = types.Message # Создаём псевдоним для класса Message (используется для аннотации типов)

# Декоратор, который регистрирует функцию-обработчик команды /start
@bot.message_handler(['start'])
def start(msg: m): # Функция принимает сообщение от пользователя
    logger.info(f"Пользователь {msg.chat.id} нажал /start")  # Логируем действие пользователя по его ID
    old = db.db.s.get(db.Users, msg.chat.id)
    if not old:
        user = db.Users(id=msg.chat.id, name=msg.from_user.full_name, answers=None, is_admin=False)
        db.db.merge(user)
        db.db.commit()
    bot.send_message(msg.chat.id, "Пройти опрос — /lets_go")

# Декоратор, который регистрирует функцию-обработчик команды /lets_go
@bot.message_handler(['lets_go'])
def quest(msg: m): # Функция для обработки команды начала опроса
    # Обращаемся к базе данных: ищем запись в таблице Manage с id=1
    data = db.db.s.get(db.Manage, 1)
    if data: # Если запись найдена (существует)
        logger.debug(f"Прочитали вопросы из manage: {data.questions}")  # Логируем вопросы
        data = ", ".join(data.questions)  # Преобразуем список вопросов в строку через запятую
        bot.send_message(msg.chat.id, "Вопросы: + " + data)  # Отправляем вопросы пользователю
    else: # Если запись не найдена
        logger.warning(f"Юзер {msg.chat.id} вызвал вопросы, но вопросов в таблице нет")  # Предупреждение в лог
        bot.send_message(msg.chat.id, "Сейчас вопросов нет.")  # Уведомляем пользователя

# Декоратор, который регистрирует функцию-обработчик команды /write
@bot.message_handler(['write'])
def write(msg: m):
    # Создаём объект Manage с id=1 (если существует - обновится, если нет - создастся)
    data = db.Manage(id=1, short_name="Тестовый опрос", questions=["Ты кто?", "Кто я?"])
    db.db.merge(data)  # Добавляем/обновляем объект в сессии БД
    db.db.commit()  # Сохраняем изменения в БД (фиксируем транзакцию)

    # Создаём второй объект Manage с id=2
    data = db.Manage(id=2, short_name="Крутой опрос", questions=["Ты крут?", "Докажи?"])
    db.db.merge(data)  # Добавляем/обновляем второй объект
    db.db.commit()  # Сохраняем изменения

    # Логируем успешное действие администратора с его ID и ID последнего добавленного объекта
    logger.success(f"Админ {msg.chat.id} записал список вопросов с id={data.id}")


# Обработчик команды /admin (вход в панель администратора)
@bot.message_handler(['admin'])
def admin(msg: m):
    # Получаем пользователя из БД по его Telegram ID
    user = db.db.s.get(db.Users, msg.chat.id)

    # Проверяем, есть ли у пользователя права администратора
    if user.is_admin:
        # Если да - логируем вход и вызываем панель администратора
        logger.info(f"Админ {msg.chat.id} зашёл в меню администратора")
        admin_panel(msg)
    else:
        # Если нет - логируем предупреждение и отправляем пользователя в стартовое меню
        logger.warning(f"Юзер {msg.chat.id} стучится в меню администратора")
        start(msg)


# Функция отображения панели администратора
def admin_panel(msg):
    # Создаём клавиатуру с двумя рядами кнопок (True, True - автоизменяемый размер, одна клавиша на строку)
    kb = telebot.types.ReplyKeyboardMarkup(True, True)

    # Добавляем кнопки в первый ряд
    kb.row('Посмотреть списки вопросов', 'Удалить список вопросов')
    # Добавляем кнопку во второй ряд
    kb.row('Добавить список вопросов')

    # Отправляем сообщение с прикреплённой клавиатурой
    bot.send_message(msg.chat.id, "Выбери действие:", reply_markup=kb)

    # Устанавливаем следующий обработчик для ответа пользователя
    bot.register_next_step_handler(msg, admin_panel_handler)


# Обработчик выбора действия в панели администратора
def admin_panel_handler(msg: m):
    # Проверяем, начинается ли текст с "Посмотреть"
    if msg.text.startswith("Посмотреть"):
        questions = check_questions()  # Получаем список всех вопросов
        bot.send_message(msg.chat.id, questions_format(questions),
                         parse_mode="HTML")  # Отправляем отформатированный список
    # Проверяем, начинается ли текст с "Удалить"
    elif msg.text.startswith("Удалить"):
        pass  # Пока ничего не делаем (заглушка)
    # Проверяем, начинается ли текст с "Добавить"
    elif msg.text.startswith("Добавить"):
        pass  # Пока ничего не делаем (заглушка)
    else:
        # Если текст не соответствует ни одной кнопке - возвращаем в панель
        admin_panel(msg)


# Декоратор для перехвата и логирования ошибок в функции
@logger.catch
def check_questions():
    questions = []  # Создаём пустой список для хранения данных
    # Получаем все записи из таблицы Manage
    data = db.db.s.query(db.Manage).all()

    # Проходим по каждой записи
    for d in data:
        # Добавляем в список [id, короткое_название, список_вопросов]
        questions.append([d.id, d.short_name, d.questions])

    logger.success("поменяешь")  # Логируем успешное выполнение (странное сообщение, возможно опечатка)
    return questions  # Возвращаем собранные данные


# Декоратор для перехвата и логирования ошибок в функции
@logger.catch
def questions_format(questions: list):
    # Начало форматированного текста
    text = "Списки вопросов: \n\n"

    # Проходим по каждому списку вопросов
    for q_list in questions:
        text += f"Список №{q_list[0]}\n"  # Добавляем номер списка (id)
        text += telebot.formatting.hbold(q_list[1]) + "\n"  # Добавляем название жирным шрифтом (HTML)
        text += f"Вопросы: \n"  # Заголовок "Вопросы:"

        # Проходим по каждому вопросу в списке
        for n, q in enumerate(q_list[2]):
            text += f"Вопрос №{n + 1}. {q}\n"  # Добавляем вопрос с порядковым номером

        text += "\n"  # Добавляем пустую строку между списками

    logger.info("Строка отформатирована успешно")  # Логируем успешное форматирование
    return text  # Возвращаем готовый текст


bot.infinity_polling() # Запускаем бота в режиме бесконечного опроса (постоянно ждём сообщения)