from sqlalchemy import create_engine        # Движок подключения к БД
from sqlalchemy.orm import sessionmaker, declarative_base  # Сессии и базовый класс моделей
from sqlalchemy import Column, Integer, String, Boolean, PickleType  # Типы колонок
from loguru import logger                  # Логирование

# Класс для работы с БД
class DB:
    @logger.catch  # Перехват ошибок
    def __init__(self, DATABASE_FILE):
        self.engine = create_engine(f"sqlite:///{DATABASE_FILE}")  # Движок SQLite
        Session = sessionmaker(bind=self.engine)  # Фабрика сессий
        self.Base = declarative_base()      # Базовый класс моделей
        self.s = Session()                  # Сессия для работы
        logger.success(f"База данных активирована по адресу → {DATABASE_FILE}")

    @logger.catch
    def setup(self):
        self.Base.metadata.create_all(self.engine)  # Создание таблиц
        logger.success("Таблицы БД настроены")

    @logger.catch
    def merge(self, data):
        self.s.merge(data)  # Добавление/обновление объекта
        logger.info(f"Добавлен объект таблицы {data.__class__.__tablename__}, id={data.id}")

    @logger.catch
    def commit(self):
        self.s.commit()  # Сохранение изменений
        logger.info("Произошёл коммит в БД")

# Глобальный экземпляр БД
db = DB("db.db")

# Модель таблицы users
class Users(db.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)  # ID пользователя
    name = Column(String)                   # Имя
    answers = Column(PickleType)            # Ответы (сериализованные)
    is_admin = Column(Boolean, default=False)  # Администратор

# Модель таблицы manage
class Manage(db.Base):
    __tablename__ = "manage"
    id = Column(Integer, primary_key=True, default=1)  # ID записи
    short_name = Column(String)             # Название опроса
    questions = Column(PickleType)          # Список вопросов

# Создание таблиц
db.setup()