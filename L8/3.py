class Check(Exception):
    def __init__(self):
        self.flag = True

    def check_char(self, ar):
        for x in ar:
            if not str(x).isnumeric():
                self.flag = False

    def __str__(self):
        return "Ошибка ввода"


arr = []
while True:
    char_to_check = input(" Введите чило (стоп слово =stop) ")
    if char_to_check == 'stop':
        print(arr)
        break
    else:
        try:
            arr.append(char_to_check)
            a = Check()
            a.check_char(arr)
            if not a.flag:
                raise Check
        except Check:
            arr.remove(char_to_check)
            print(Check())
        finally:
            arr = list(map(int, arr))
