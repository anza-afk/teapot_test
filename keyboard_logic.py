import platform
from logger import logger

# Если ОС Windows
if platform.system() == "Windows":
    import msvcrt
    
# Если ОС Linux, OS X
else:
    import sys
    import termios
    import atexit
    from select import select

logger.info(f"OS: {platform.system()}")

class KBHit:
    def __init__(self):
        """Создаёт экземпляр классаа для отслеживания нажатий клавиш"""

        if platform.system() == "Windows":
            pass
        
        else:
    
            # Сохранение настроек терминала
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
    
            # Восстановление настроек терминала после выхода
            atexit.register(self.set_normal_term)
    
    def set_normal_term(self):
        """Возврат к нормальному терминалу."""
        
        if platform.system() == "Windows":
            pass
        
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getwch(self):
        """Метод для чтения нажатой клавиши клавиатуры,
        если операционная система не Windows.
        Возвращает символ, соответствующий клавише.
        """
        
        if platform.system() == "Windows":
            return msvcrt.getwch()
        
        else:
            return sys.stdin.read(1)
                        

    def kbhit(self):
        """Метод для ожидания чтения нажатия клавиши
        клавиатуры, если операционная система не Windows.
        Возвращает True, если какая-либо клавиша нажата,
        в остальных случаях возвращает False."""
        if platform.system() == "Windows":
            return msvcrt.kbhit()
        
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []
    
    
