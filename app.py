import configparser
from models import Teapot
from logger import logger

# Импорт настроек из файла config.ini
config = configparser.ConfigParser(interpolation=None)
config.read("config.ini")
max_amount_of_water = float(config['Teapot']['max_amount_of_water'])
boil_time = int(config['Teapot']['boil_time'])
stop_temperature = int(config['Teapot']['stop_temperature'])

if __name__ == "__main__":
    # Создание инстанса чайника с импортированными настройками
    My_Teapot = Teapot(
        max_amount_of_water=max_amount_of_water,
        boil_time=boil_time,
        stop_temperature=stop_temperature,
    )
    while True:
        try:
            water = float(input(
                f"Сколько налить воды? (Максимум - {max_amount_of_water}л.)\n"))
            if My_Teapot.fill(water):
                break
        except (TypeError, ValueError):
            logger.error('Принимаются только числа!')
    My_Teapot.turn_on()
