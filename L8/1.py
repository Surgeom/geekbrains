class Date:

    def __init__(self, s):
        self.date = s

    @classmethod
    def date_to_int(cls, string):
        try:
            return cls(list(map(int, string.split('-'))))
        except ValueError:
            return "Введите строку правильного формата"

    @staticmethod
    def validation(string_date):
        new_obj = Date.date_to_int(string_date)
        arr = new_obj.date
        if arr[2] < 0 or arr[0] > 31:
            return 'Ошибка в числе месяца'
        elif arr[2] < 0 or arr[1] > 12:
            return 'Ошибка в месяце'
        elif arr[2] < 0 or arr[2] > 9999:
            return 'Ошибка в годе'
        else:
            return True


s = "01-02-2012"
a = Date.date_to_int(s)
print(a.date_to_int(s).date)
print(a.validation(s))

