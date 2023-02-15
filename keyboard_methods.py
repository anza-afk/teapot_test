import platform
from logger import logger

# Проверка типа операционной системы для проверки кнопки с клавиатуры
# Если система Windows:
if platform.system() == "Windows":
    from msvcrt import kbhit, getwch

    logger.info(f"OS: {platform.system()}")

# Если система не WIndows:
else:
    import tty
    import termios
    import fcntl
    import sys
    import os

    logger.info(f"OS: {platform.system()}")

    def getwch():
        """Метод для чтения нажатой клавиши клавиатуры,
        если операционная система не Windows.
        Возвращает символ, соответствующий клавише.
        """
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, oldterm)
        return ch

    def kbhit():
        """Метод для ожидания чтения нажатия клавиши
        клавиатуры, если операционная система не Windows.
        Возвращает True, если какая-либо клавиша нажата,
        в остальных случаях возвращает False."""
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            while True:
                try:
                    ch = sys.stdin.read(1)
                    return True
                except IOError:
                    return False
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
