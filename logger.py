import logging
import sqlite3
from datetime import datetime

# создание логгера и настрока уровня сообщений
logger = logging.getLogger("teapot_logger")
logger.setLevel(logging.INFO)

# настройка формата сообщений
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# создание класса хендлера в БД SQLite для логгера
class SQLiteHandler(logging.Handler):
    def __init__(self, file):
        super().__init__()
        self.db = sqlite3.connect(file)
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS logs (datetime TEXT, name TEXT, '
            'level TEXT, message TEXT)')

    def emit(self, message):
        # Записываем сообщение в БД
        date_time = datetime.now()
        self.db.execute(
            'INSERT INTO logs(datetime, name, level, message)'
            ' VALUES(?,?,?,?)',
            (
                date_time,
                message.name,
                message.levelname,
                message.message,
            )
        )
        self.db.commit()


# создание хендлеров для логгера
fh = logging.FileHandler('teapot.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
db_handler = SQLiteHandler('sqlite.db')
db_handler.setLevel(logging.INFO)

logger.addHandler(fh)
logger.addHandler(sh)
logger.addHandler(db_handler)
