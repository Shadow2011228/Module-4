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

@bot.message_handler(['write'])
def write(msg: m):
    data = db.Manage(id=1, short_name="Тестовый опрос", questions=["Ты кто?", "Кто я?"])
    db.db.merge(data)
    db.db.commit()
    data = db.Manage(id=2, short_name="Крутой опрос", questions=["Ты крут?", "Докажи?"])
    db.db.merge(data)
    db.db.commit()
    logger.success(f"Админ {msg.chat.id} записал список вопросов с id={data.id}")

@bot.message_handler(['admin'])
def admin(msg: m):
    user = db.db.s.get(db.Users, msg.chat.id)
    if user.is_admin:
        logger.info(f"Админ {msg.chat.id} зашёл в меню администратора")
        admin_panel(msg)
    else:
        logger.warning(f"Юзер {msg.chat.id} стучится в меню администратора")
        start(msg)

def admin_panel(msg):
    kb = telebot.types.ReplyKeyboardMarkup(True, True) # создали пустую клавиатуру
    kb.row('Посмотреть списки вопросов','Удалить список вопросов') # Добавили кнопки
    kb.row('Добавить список вопросов')

    bot.send_message(msg.chat.id, "Выбери действие:", reply_markup=kb)  # Прикрепили клавиатуру к сообщению
    bot.register_next_step_handler(msg, admin_panel_handler)


def admin_panel_handler(msg: m):
    if msg.text.startswith("Посмотреть"):
        questions = check_questions()
        bot.send_message(msg.chat.id, questions_format(questions), parse_mode="HTML")
    elif msg.text.startswith("Удалить"):
        pass
    elif msg.text.startswith("Добавить"):
        pass
    else:
        admin_panel(msg)

@logger.catch
def check_questions():
    questions = []
    data = db.db.s.query(db.Manage).all()
    for d in data:
        questions.append([d.id, d.short_name, d.questions])
    logger.success("поменяешь")
    return questions

@logger.catch
def questions_format(questions: list):
   text = "Списки вопросов: \n\n"
   for q_list in questions:
       text += f"Список №{q_list[0]}\n"
       text += telebot.formatting.hbold(q_list[1]) + "\n"
       text += f"Вопросы: \n"
       for n, q in enumerate(q_list[2]):
           text += f"Вопрос №{n+1}. {q}\n"
       text += "\n"
   logger.info("Строка отформатирована успешно")
   return text


bot.infinity_polling() # Запускаем бота в режиме бесконечного опроса (постоянно ждём сообщения)