class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        return f'{self.title} - Запуск отрисовки.'


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__()

    def draw(self):
        return f'{self.title} - Запуск отрисовки ручкой.'


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__()

    def draw(self):
        return f'{self.title} - Запуск отрисовки карандашом.'


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__()

    def draw(self):
        return f'{self.title} - Запуск отрисовки маркером.'


a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

arr = [a, b, c, d]

for i in range(len(arr)):
    print(arr[i].draw())
