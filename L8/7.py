class Complex:

    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __str__(self):
        return f'{self.a} + i{self.b}'

    def __add__(self, other):
        return Complex(self.a + other.b, self.a + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b - self.a * other.b)


c1 = Complex(1, 4)
c2 = Complex(2, 5)
print(c1)
