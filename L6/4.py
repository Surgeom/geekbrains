class Car:
    def __init__(self, car_speed, car_color, car_name):
        self.speed = car_speed
        self.color = car_color
        self.name = car_name
        if self.__class__.__name__ == "PoliceCar":
            self.is_police = True
        else:
            self.is_police = False

    def go(self):
        return f'{self.name} start'

    def stop(self):
        return f'{self.name} stop'

    def turn(self, direction):
        return f'{self.name} turn {direction}'

    def show_speed(self):
        return f'{self.name} speed= {self.speed}'


class TownCar(Car):
    def __init__(self, car_speed, car_color, car_name):
        super(TownCar, self).__init__(car_speed, car_color, car_name)
        self.toofast = 60

    def show_speed(self):
        if int(self.speed) <= self.toofast:
            return f'  {self.name} speed= {self.speed}'
        else:
            return f'Warning! Too fast >{self.toofast}'


class WorkCar(TownCar):
    def __init__(self, car_speed, car_color, car_name):
        super(WorkCar, self).__init__(car_speed, car_color, car_name)
        self.toofast = 40


class SportCar(Car):
    def __init__(self, car_speed, car_color, car_name):
        super(SportCar, self).__init__(car_speed, car_color, car_name)


class PoliceCar(Car):
    def __init__(self, car_speed, car_color, car_name):
        super(PoliceCar, self).__init__(car_speed, car_color, car_name)


a = TownCar(70, 'yel', 'Mazda')
b = PoliceCar(100, 'blue', 'Mers')
c = SportCar(120, 'green', 'Lex')
d = WorkCar(70, 'grey', 'audi')
arr = [a, b, c, d]
for i in range(len(arr)):
    print(arr[i].name)
    print(arr[i].color)
    print(arr[i].speed)
    print(f'is police == {arr[i].is_police}')
    print(arr[i].go())
    print(arr[i].turn('right'))
    print(arr[i].show_speed())
    print(arr[i].stop())
    print()
