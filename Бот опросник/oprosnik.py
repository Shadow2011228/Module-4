import random
import time

import telebot  # Импорт библиотеки для работы с Telegram Bot API
from telebot import types  # Импорт типов данных (клавиатуры, кнопки и т.д.)
from loguru import logger  # Импорт библиотеки для удобного логирования (вывод информации в консоль)
import db  # Импорт нашего модуля db.py (работа с базой данных)
from logtail import LogtailHandler


logtail_handler = LogtailHandler(source_token='UHFayoDqfLHhJUYoK5AbJrJX')

logger.add("log.log", level="DEBUG", compression='zip', rotation='1 hour', retention='1 week')
logger.add("warn.log", level="WARNING", delay=True, rotation='1 hour')
logger.add(logtail_handler, level="DEBUG")
# Создание экземпляра бота с использованием токена (уникальный ключ для доступа к боту)
bot = telebot.TeleBot("8598431910:AAG8zvIUEk7E0N3v1eeOV3kKCtQ8FN6fJM4")
logger.success("Экземпляр бота создан")  # Логируем успешное создание бота

m = types.Message  # Создаём псевдоним для класса Message (используется для аннотации типов)
temp = {}


# Декоратор, который регистрирует функцию-обработчик команды /start
@bot.message_handler(['start'])
def start(msg: m):  # Функция принимает сообщение от пользователя
    logger.info(f"Пользователь {msg.chat.id} нажал /start")  # Логируем действие пользователя по его ID
    old = db.db.s.get(db.Users, msg.chat.id)
    if not old:
        user = db.Users(id=msg.chat.id, name=msg.from_user.full_name, answers=None, is_admin=False)
        db.db.merge(user)
        db.db.commit()
    bot.send_message(msg.chat.id, "Пройти опрос — /lets_go")


# Декоратор, который регистрирует функцию-обработчик команды /lets_go
@bot.message_handler(['lets_go'])
def quest(msg: m):
    questions = check_questions()
    ids = []
    keyboard = types.ReplyKeyboardMarkup(True, True)
    for q in questions:
        ids.append(q[0])
        keyboard.row(str(q[0]))
        text = "Выберите опрос: \n"
        for q in questions:
            text += telebot.formatting.hbold(f"Номер {q[0]}. {q[1]} \n")
            bot.send_message(msg.chat.id, text, parse_mode="HTML", reply_markup=keyboard)

    bot.register_next_step_handler(msg, first_question, ids)


def first_question(msg: m, ids: list):
    if not msg.text.isnumeric():
        logger.warning(f"Юзер {msg.chat.id} ввёл неверный номер списка")
        bot.send_message(msg.chat.id, "Введён неправильный номер списка")
        start(msg)
        return
    if int(msg.text) not in ids:
        logger.warning(f"Юзер {msg.chat.id} ввёл неверный номер списка")
        bot.send_message(msg.chat.id, "Введён неправильный номер списка")
        start(msg)
        return

    temp[msg.chat.id] = {
        'list': int(msg.text),
        'queue': 0,
        'answers': []
    }
    logger.info(f"Клиент {msg.chat.id} инициализировал переменную - {temp[msg.chat.id]}")
    questions = db.db.s.get(db.Manage, int(msg.text)).questions
    bot.send_message(msg.chat.id, questions[0])
    bot.register_next_step_handler(msg, next_question, questions)


@logger.catch
def next_question(msg: m, questions):
    global temp
    temp[msg.chat.id]['answers'].append(msg.text)
    logger.info(f"Юзер {msg.chat.id} ответил на вопрос №{temp[msg.chat.id]['queue']} "
                f"списка №{temp[msg.chat.id]['list']}")

    if temp[msg.chat.id]['queue'] == len(questions) - 1:
        bot.send_message(msg.chat.id, "Спасибо за ответы!")
        logger.success(f"Юзер {msg.chat.id} завершил опрос!")
        save_client(msg)
        return

    temp[msg.chat.id]['queue'] += 1
    question = questions[temp[msg.chat.id]['queue']]
    bot.send_message(msg.chat.id, question)
    bot.register_next_step_handler(msg, next_question, questions)


def save_client(msg: m):
    user = db.db.s.get(db.Users, msg.chat.id)
    if user.answers is None:
        answers = [temp[msg.chat.id]['answers']]
    else:
        answers = user.answers
        answers.append(temp[msg.chat.id]['answers'])
    db.db.s.query(db.Users).filter_by(id=msg.chat.id).update({"answers": answers})
    db.db.commit()


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
    kb = telebot.types.ReplyKeyboardMarkup(True, True)

    kb.row('Посмотреть списки вопросов', 'Удалить список вопросов')
    kb.row('Добавить список вопросов', 'Посмотреть ответы')

    bot.send_message(msg.chat.id, "Выбери действие:", reply_markup=kb)

    bot.register_next_step_handler(msg, admin_panel_handler)


# Обработчик выбора действия в панели администратора
def admin_panel_handler(msg: m):
    # Проверяем, начинается ли текст с "Посмотреть"
    if msg.text.startswith("Посмотреть списки"):
        questions = check_questions()  # Получаем список всех вопросов
        bot.send_message(msg.chat.id, questions_format(questions),
                         parse_mode="HTML")  # Отправляем отформатированный список
    # Проверяем, начинается ли текст с "Удалить"
    elif msg.text.startswith("Удалить"):
        delete_questions(msg)
    # Проверяем, начинается ли текст с "Добавить"
    elif msg.text.startswith("Добавить"):
        ask_question(msg)
    # Проверяем, начинается ли текст с "Посмотреть ответы"
    elif msg.text.startswith("Посмотреть ответы"):
        view_answers(msg)
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


@logger.catch
def delete_questions(msg: m):
    questions = check_questions()
    ids = []

    keyboard = types.ReplyKeyboardMarkup(True, True)
    for q in questions:
        ids.append(q[0])
        keyboard.row(str(q[0]))

    text = "Выберите список для удаления: \n"
    for q in questions:
        text += telebot.formatting.hbold(f"Номер {q[0]}. {q[1]} \n")

    bot.send_message(msg.chat.id, text, parse_mode="HTML", reply_markup=keyboard)
    bot.register_next_step_handler(msg, delete_questions_handler, ids)


@logger.catch
def delete_questions_handler(msg: m, ids: list):
    if not msg.text.isnumeric() or int(msg.text) not in ids:
        logger.warning(f"Админ {msg.chat.id} ввёл неверный номер списка")
        bot.send_message(msg.chat.id, "Введён неправильный номер списка")
        admin_panel(msg)
        return

    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row("я передумал")
    keyboard.row("УДАЛИТЬ")

    bot.send_message(msg.chat.id, f"Вы точно хотите удалить список №{msg.text}?", reply_markup=keyboard)
    bot.register_next_step_handler(msg, delete, int(msg.text))


@logger.catch
def delete(msg: m, num: int):
    if msg.text == "УДАЛИТЬ":
        db.db.s.query(db.Manage).filter(db.Manage.id == num).delete()
        db.db.commit()
        bot.send_message(msg.chat.id, f"Список №{num} успешно удалён!")
        logger.success(f"Список №{num} успешно удалён!")

    else:
        bot.send_message(msg.chat.id, "Удаление отменено.")
        admin_panel(msg)


@logger.catch
def ask_question(msg: m):
    global temp
    temp[msg.chat.id] = []
    logger.success(f"Админ {msg.chat.id} добавил новый опрос")
    bot.send_message(msg.chat.id, "Введи первый вопрос:")
    bot.register_next_step_handler(msg, ask_next_question)


@logger.catch
def ask_next_question(msg: m):
    global temp
    if msg.text != "всё!":
        temp[msg.chat.id].append(msg.text)
        bot.send_message(msg.chat.id, "Введи следующий вопрос:")
        bot.register_next_step_handler(msg, ask_next_question)
    else:
        bot.send_message(msg.chat.id, "Напишите краткое имя опроса")
        bot.register_next_step_handler(msg, obrabochik)


@logger.catch
def obrabochik(msg: m):
    num = len(check_questions()) + 1
    data = db.Manage(id=num, short_name=msg.text, questions=temp[msg.chat.id])
    db.db.merge(data)  # Добавляем/обновляем объект в сессии БД
    db.db.commit()  # Сохраняем изменения в БД (фиксируем транзакцию)
    logger.success(f"Админ {msg.chat.id} записал новый список №{num}")
    bot.send_message(msg.chat.id, "Список успешно записан")
    time.sleep(2)
    admin_panel(msg)


@logger.catch
def view_answers(msg: m):
    # Получаем список всех вопросов для выбора
    questions = check_questions()
    if not questions:
        bot.send_message(msg.chat.id, "Нет доступных опросов!")
        admin_panel(msg)
        return

    ids = []
    keyboard = types.ReplyKeyboardMarkup(True, True)
    for q in questions:
        ids.append(q[0])
        keyboard.row(str(q[0]))

    text = "Выберите опрос для просмотра ответов: \n"
    for q in questions:
        text += telebot.formatting.hbold(f"Номер {q[0]}. {q[1]} \n")

    bot.send_message(msg.chat.id, text, parse_mode="HTML", reply_markup=keyboard)
    bot.register_next_step_handler(msg, view_answers_handler, ids)


@logger.catch
def view_answers_handler(msg: m, ids: list):
    if not msg.text.isnumeric() or int(msg.text) not in ids:
        logger.warning(f"Админ {msg.chat.id} ввёл неверный номер списка")
        bot.send_message(msg.chat.id, "Введён неправильный номер списка")
        admin_panel(msg)
        return

    list_id = int(msg.text)
    users = db.db.s.query(db.Users).all()

    respondents = []
    for user in users:
        if user.answers:
            for answer_list in user.answers:
                survey = db.db.s.get(db.Manage, list_id)
                if survey and len(answer_list) == len(survey.questions):
                    respondents.append({
                        'user': user,
                        'answers': answer_list
                    })

    if not respondents:
        bot.send_message(msg.chat.id, f"На опрос №{list_id} пока никто не ответил.")
        admin_panel(msg)
        return

    survey = db.db.s.get(db.Manage, list_id)
    text = f"Ответы на опрос: {survey.short_name}\n\n"

    for i, respondent in enumerate(respondents, 1):
        user = respondent['user']
        answers = respondent['answers']
        text += f"{i}. {user.name} (ID: {user.id})\n"
        for j, (question, answer) in enumerate(zip(survey.questions, answers), 1):
            text += f"   Вопрос {j}: {answer}\n"
        text += "\n"

        if len(text) > 4000:
            bot.send_message(msg.chat.id, text)
            text = ""

    if text:
        bot.send_message(msg.chat.id, text)

    admin_panel(msg)

bot.infinity_polling()