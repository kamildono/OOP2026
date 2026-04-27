import sys
from random import randint

PATH_TO_TXT = 'data.txt'
LIMIT_LEFT = 0
LIMIT_RIGHT = 100

class Model:

    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.__observers = list()
        self.__counter = 0
        self.load()

    def load(self):
        with open(PATH_TO_TXT, 'r') as f:
            data = f.readline()
        try:
            self.__a, self.__b, self.__c = data.split()
            print("try", self.__a, self.__b, self.__c)
            self.__a = int(self.__a)
            self.__b = int(self.__b)
            self.__c = int(self.__c)
        except:
            print('Something went terribly wrong!')
            sys.exit()
        self._startingSetValues(self.__a, self.__b, self.__c)

    def addObersver(self, obs):
        print("adding obs:", obs)
        if obs not in self.__observers:
            self.__observers.append(obs)

    def save(self):
        print('save', self.__a, self.__b, self.__c)
        with open(PATH_TO_TXT, 'w') as f:
            f.write(f"{self.__a} {self.__b} {self.__c}")

    def notify(self):
        print('***** SENDING TO UI! *****')
        self.__counter += 1
        for e in self.__observers:
            e.setValues(self.__a, self.__b, self.__c)
        print("times called", self.__counter)

    def setA(self, new_value):
        self._correctA(new_value)
        self.notify()
        self.save()

    def setB(self, new_value):
        self._correctB(new_value)
        self.notify()
        self.save()

    def setC(self, new_value):
        self._correctC(new_value)
        self.notify()
        self.save()

    def _correctA(self, a):
        a = self._limitValue(a)

        self.__a = a
        if self.__a <= self.__b <= self.__c:
            return

        if self.__a > self.__b:
            self.__b = min(self.__a, LIMIT_RIGHT)
        if self.__a > self.__c:
            self.__c = min(self.__b, LIMIT_RIGHT)


    def _correctB(self, b):
        b = self._limitValue(b)

        if b < self.__a:
            b = self.__a
        elif b > self.__c:
            b = self.__c
        self.__b = b

    def _correctC(self, c):
        c = self._limitValue(c)

        self.__c = c
        if c >= self.__b >= self.__a:
            return

        if self.__b > self.__c:
            self.__b = max(self.__c, LIMIT_LEFT)
        if self.__a > self.__c:
            self.__a = max(self.__b, LIMIT_LEFT)

    def _limitValue(self, val):
        if val < LIMIT_LEFT:
            val = LIMIT_LEFT
        else: val = min(val, LIMIT_RIGHT)
        return val

    def _startingSetValues(self, a, b, c):
        self._correctA(a)
        self._correctB(b)
        self._correctC(c)
        self.save()

    def __del__(self):
        self.save()


