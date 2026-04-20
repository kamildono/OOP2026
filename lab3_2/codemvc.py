import sys
from random import randint

path_to_txt = 'data.txt'
limits = [0, 100]

class Model:
    __a = 0
    __b = 0
    __c = 0

    observers = []
    def __init__(self, subscriber=None):
        if subscriber is not None:
            self.observers.append(subscriber)

        with open(path_to_txt, 'r') as f:
            data = f.readline()
        #print(data, type(data))

        try:
            self.__a, self.__b, self.__c = data.split()
            print("try", self.__a, self.__b, self.__c)
            self.__a = int(self.__a)
            self.__b = int(self.__b)
            self.__c = int(self.__c)
        except:
            print('Something went terribly wrong!')
            sys.exit()
        f.close()
        print('init', self.__a, self.__b, self.__c)
        self.writeValues([self.__a, self.__b, self.__c])
        print(self.observers)

    def writeFile(self):
        print('writeFile', self.__a, self.__b, self.__c)
        with open(path_to_txt, 'w') as f:
            f.write(str(self.__a) + ' ' + str(self.__b) + ' ' + str(self.__c))
        f.close()

    def getAll(self):
        return [self.__a, self.__b, self.__c ]

    def sendValue(self):
        print('***** SENDING TO UI! *****')
        arr_to_send = self.getAll()
        for e in self.observers:
            e.updateFromModel(arr_to_send)

    def recieveValues(self, object):
        print("def recieveValues(self, object):", *object)
        a = object[0]
        b = object[1]
        c = object[2]

        self.writeValues([a,b,c])

    def correctValues(self, data):
        print('checking a')
        a = data[0]
        if a < limits[0]:
            a = limits[0]
        else: a = min(a, limits[1])
        flag_a = (a != self.__a)

        print('checking c')
        c = data[2]
        if c > limits[1]:
            c = limits[1]
        else:
            c = max(c, limits[0])
        flag_c = (c != self.__c)

        print('checking b')
        b = data[1]
        if b < a:
            b = a
        elif b > c:
            b = c
        flag_b = (b != self.__b)

        print("flags:", flag_a, flag_b, flag_c)
        while not a <= b <= c:
            print('chort!')
            if flag_b and (b > c or b < a):
                print("changing b")
                b = self.__b
            if flag_a:
                print("changing a")
                if a <= b:
                    continue
                b = min(a + randint(1, 5), limits[1])
                if a <= c:
                    continue
                c = min(b + randint(1, 5), limits[1])
            if flag_c:
                print("changing c")
                if c >= b:
                    continue
                b = max(c - randint(1, 5), limits[0])
                if c >= a:
                    continue
                a = max(b - randint(1, 5), limits[0])

        changed_data = [a, b, c]
        return changed_data

    def writeValues(self, data):
        arr = self.correctValues(data)
        print("def writeValues(self, data):", arr)
        self.__a = arr[0]
        self.__b = arr[1]
        self.__c = arr[2]
        self.writeFile()
        self.sendValue()

    def __del__(self):
        self.writeFile()


