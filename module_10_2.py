import time
from threading import Thread
import requests


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemys = 100
        count = 1
        print(f"{self.name}, на нас напали!")
        while enemys > 0:
            print(f'{self.name} сражается {count} день(дня)..., осталось {enemys - self.power} воинов.')
            count += 1
            enemys -= self.power
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {count - 1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.run()