import time
from keyboard_logic import KBHit
from logger import logger


class Teapot():
    """Класс, описывающий электрический чайник"""
    def __init__(
        self,
        max_amount_of_water,
        boil_time,
        stop_temperature,
        temperature=0,
        amount_of_water=0,
        is_on=False
    ):
        self.max_amount_of_water = max_amount_of_water
        self.boil_time = boil_time
        self.temperature = temperature
        self.stop_temperature = stop_temperature
        self.amount_of_water = amount_of_water
        self.is_on = is_on

    def fill(self, water):
        """Метод наполнения чайника водой.
        Возвращает True, если указанное количество воды влезет в чайник,
        иначе возвращает False"""
        if water <= self.max_amount_of_water + self.amount_of_water:
            self.amount_of_water = water
            return True
        else:
            logger.error(f"В чайнике недостаточно места для {water}л. воды!")
            return False

    def turn_on(self):
        """Метод включения чайника.
        Возвращает метод выключения чайника в случае кипения
        или нажатия клавиши Enter на клавиатуре."""
        self.is_on = True
        logger.info('Чайник включен.')

        # Создание экземпляра класса KBHit
        kb = KBHit()

        for _ in range(self.boil_time):

            # Проверка нажатия клавиши Enter
            if kb.kbhit():
                if ord(kb.getwch()) in (10, 13):
                    break

            time.sleep(1)
            self.temperature += 10
            logger.info(self.temperature)

            # Проверка установленной температуры для выключения чайника
            if self.temperature == self.stop_temperature:
                break

        # Проверка кипения
        if self.temperature == 100:
            logger.info(f'Вода в чайнике вскипела ({self.amount_of_water}л.)')
        return self.turn_off()

    def turn_off(self):
        """Метод выключения чайника"""
        self.is_on = False
        logger.info('Чайник выключен.')
