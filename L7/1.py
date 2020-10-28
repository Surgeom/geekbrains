class Matrix:
    def __init__(self, matrix_in_arr):
        self.income_matrix = matrix_in_arr

    def __str__(self):
        return '\n'.join(['   '.join([str(num) for num in arr]) for arr in [arr for arr in self.income_matrix]])

    def __add__(self, other):
        if len(self.income_matrix) == len(other.income_matrix):
            rezult = []
            for i in range(len(self.income_matrix)):
                arr_to_append = []
                for j in range(len(self.income_matrix[i])):
                    arr_to_append.append(int(self.income_matrix[i][j]) + int(other.income_matrix[i][j]))
                rezult.append(arr_to_append)
            return Matrix(rezult)
        else:
            return "матрицы должны быть с одинкаовым числом элементов"


ar = [[1, 2], [3, 4], [5, 6]]
ar_2 = [[7, 8], [9, 1], [2, 3]]

a = Matrix(ar)
b = Matrix(ar_2)
print(a)
print()
print(b)
print()
print(a + b)
