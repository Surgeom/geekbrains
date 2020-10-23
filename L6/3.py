class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return f"{sum(self._income.values())}"


a = Position('kirill', 'ush', 'gen', 10, 20)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
print(a.get_full_name())
print(a.get_total_income())
