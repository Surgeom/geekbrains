class Cells:
    def __init__(self, cells_num):
        self.cells_num = int(cells_num)

    def __add__(self, other):
        return Cells(self.cells_num + other.cells_num)

    def __sub__(self, other):
        return Cells(self.cells_num - other.cells_num) if self.cells_num - other.cells_num >= 0 \
            else Cells(other.cells_num - self.cells_num)

    def __mul__(self, other):
        return Cells(self.cells_num * other.cells_num)

    def __truediv__(self, other):
        try:
            return Cells(self.cells_num // other.cells_num)
        except   ZeroDivisionError:
            return Cells(self.cells_num)

    def __str__(self):
        return f"число ячеек = {self.cells_num}"

    def make_order(self, rows):
        rows_of_cells = ''
        for i in range(self.cells_num // int(rows)):
            rows_of_cells += ''.join('*' * int(rows) + "\n")
        rows_of_cells += ''.join('*' * (self.cells_num % int(rows)) + "\n")
        return rows_of_cells


a = Cells(12)
b = Cells(13)
print(a + b)
print(b - a)
print(a * b)
print(a / b)
print(a.make_order(5))
