import time
from termcolor import colored, cprint
class TrafficLight:
    __color_limit = [['red', 7], ['yellow', 2], ['green', 4], ['yellow', 2]]
    __tm = time.time()
    __color_limit_ln = len(__color_limit)
    def running(self):
        __position = 0
        while(time.time() < TrafficLight.__tm + 30):
            __position = __position + 1 if __position + 1 < TrafficLight.__color_limit_ln else 0
            self.__color = TrafficLight.__color_limit[__position][0]
            cprint(self.__color, self.__color)
            time.sleep(TrafficLight.__color_limit[__position][1])
a = TrafficLight()
a.running()
