class NullDevis(Exception):
    def __init__(self):
        self.txt = "Ввели отрицательное"

    def __str__(self):
        return f"{self.txt}"


num = input("Введите положительное число ")

try:
    num = int(num)
    if num < 0:
        raise NullDevis
except NullDevis:
    print(NullDevis())
except ValueError:
    print("а надо было число ввести")
else:
    print("+")
