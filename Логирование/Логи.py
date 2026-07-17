from loguru import logger

logger.add('logfile.log', compression = 'zip', rotation = '1 minute')

logger.success("Мы запустились!")
logger.debug("Для дебага")
logger.info("Для простой инфы")
logger.warning("Внимание! Неожиданное поведение!")
logger.error("Ошибка! Бим Бим Бам Бам")
logger.critical("Дантес, что ты наделал...")

