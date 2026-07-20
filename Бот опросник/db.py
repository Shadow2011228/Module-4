from sqlalchemy import create_engine        # Функция для создания движка подключения к БД
from sqlalchemy.orm import sessionmaker, declarative_base  # Для создания сессий и базового класса моделей
from sqlalchemy import Column, Integer, String, Boolean, PickleType  # Типы колонок
from loguru import logger                  # Логирование

# Класс для работы с базой данных
class DB:
    @logger.catch # Декоратор, перехватывающий ошибки и логирующий их
    def __init__(self, DATABASE_FILE):
        # Создаём движок SQLite, указываем файл базы данных
        self.engine = create_engine(f"sqlite:///{DATABASE_FILE}")
        Session = sessionmaker(bind=self.engine)  # Фабрика сессий
        self.Base = declarative_base()      # Базовый класс для объявления моделей
        self.s = Session()                  # Создаём сессию для работы с БД
        logger.success(f"База данных активирована по адресу → {DATABASE_FILE}")

    @logger.catch
    def setup(self):
        # Создаёт все таблицы, описанные в моделях, если их нет
        self.Base.metadata.create_all(self.engine)
        logger.success("Таблицы БД настроены")

    @logger.catch
    def merge(self, data):
        # Добавляет или обновляет объект в сессии (слияние)
        self.s.merge(data)
        logger.info(
            f"В соединение был добавлен объект таблицы "
            f"{data.__class__.__tablename__}, "
            f"id={data.id if data.id else data}"
        )

    @logger.catch
    def commit(self):
        # Фиксирует изменения в базе данных (сохраняет)
        self.s.commit()
        logger.info("Произошёл коммит в БД")

# Создаём глобальный экземпляр БД с именем файла "db.db"
db = DB("db.db")

# Модель таблицы "users" — хранит данные пользователей
class Users(db.Base):
    __tablename__ = "users"                # Имя таблицы в БД
    id = Column(Integer, primary_key=True) # ID пользователя (Telegram ID)
    name = Column(String)                  # Имя пользователя
    answers = Column(PickleType)           # Ответы на вопросы (сериализованный список/словарь)
    is_admin = Column(Boolean, default=False)  # Флаг администратора

# Модель таблицы "manage" — хранит настройки и вопросы опроса
class Manage(db.Base):
    __tablename__ = "manage"               # Имя таблицы
    id = Column(Integer, primary_key=True, default=1)  # ID записи (всегда 1 для одной записи)
    short_name = Column(String)            # Короткое название опроса
    questions = Column(PickleType)         # Список вопросов (сериализованный)

# Выполняем настройку таблиц (создаём, если их нет)
db.setup()