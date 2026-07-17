import telebot
from telebot import types
from loguru import logger
import db


bot = telebot.TeleBot("8598431910:AAG8zvIUEk7E0N3v1eeOV3kKCtQ8FN6fJM4")
logger.success("Экземпляр бота создан")
m = types.Message

@bot.message_handler(['start'])
def start(msg: m):
    logger.info(f"Пользователь {msg.chat.id} нажал /start")
    bot.send_message(msg.chat.id, "Пройти опрос — /lets_go")


@bot.message_handler(['lets_go'])
def quest(msg: m):
    data = db.db.s.get(db.Manage, 1)
    if data:
        logger.debug(f"Прочитали вопросы из manage: {data.questions}")
        data = ", ".join(data.questions)
        bot.send_message(msg.chat.id, "Вопросы: + " + data)
    else:
        logger.warning(f"Юзер {msg.chat.id} вызвал вопросы, но вопросов в таблице нет")
        bot.send_message(msg.chat.id, "Сейчас вопросов нет.")

bot.infinity_polling()