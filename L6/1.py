import time


class TrafficLigh:
    colors = ['red', 'yel', 'green']

    def __init__(self):
        self.__color = ""

    def running(self):
        count_runs = 0
        ind_color = 0
        n = 0
        while True:
            self.__color = self.colors[ind_color]
            print(self.__color)
            if ind_color == 0:
                time.sleep(7)
            elif ind_color == 1:
                time.sleep(2)
            else:
                time.sleep(3)

            if ind_color == 0:
                n = 1
            elif ind_color == 2:
                n = -1
            ind_color += n
            count_runs += 1
            if count_runs == 10:
                break


a = TrafficLigh()
a.running()
