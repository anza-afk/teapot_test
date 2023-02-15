import logging
# создание логгера и настрока уровня сообщений
logger = logging.getLogger("teapot_logger")
logger.setLevel(logging.INFO)

# настройка формата сообщений
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# создание хендлеров для логгера
fh = logging.FileHandler('teapot.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(fh)
logger.addHandler(sh)
