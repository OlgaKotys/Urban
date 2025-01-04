import time
import threading

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')

        while enemies > 0:
            days += 1
            enemies -= self.power
            time.sleep(1)
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')

        print(f'{self.name} одержал победу спустя {days} день(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Lafayet", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")