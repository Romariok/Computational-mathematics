class GaussSeidelSolver:
    def __init__(self, A, b, accuracy, max_iterations=100):
        self.A = A
        self.b = b
        self.accuracy = accuracy

        if not self.is_matrix_non_singular():
            raise ValueError("Матрица вырожденная. Решение невозможно.")

    # Получение минора матрицы без указанного столбца
    def get_minor(self, matrix, col):
        minor = [row[:col] + row[col + 1 :] for row in matrix[1:]]
        return minor

    # Проверка невырожденности матрицы
    def is_matrix_non_singular(self):
        return self.calculate_determinant(self.A) != 0

    def make_diagonally_dominant(self, matrix):
        n = len(matrix)

        for i in range(n):
            diagonal_element = abs(float(matrix[i][i]))
            row_sum = sum(map(abs, map(float, matrix[i]))) - diagonal_element

            if diagonal_element > row_sum:
                continue

            max_element = max(map(abs, map(float, matrix[i])))
            max_element_index = matrix[i].index(max_element)

            matrix[i], matrix[max_element_index] = matrix[max_element_index], matrix[i]
            self.b[i], self.b[max_element_index] = self.b[max_element_index], self.b[i]

        return matrix

    # Рекурсивный метод вычисления определителя
    def calculate_determinant(self, matrix):
        size = len(matrix)

        if size == 1:
            return float(matrix[0][0])

        if size == 2:
            return float(matrix[0][0]) * float(matrix[1][1]) - float(
                matrix[0][1]
            ) * float(matrix[1][0])

        det = 0.0
        for i in range(size):
            cofactor = (
                (-1) ** i
                * float(matrix[0][i])
                * self.calculate_determinant(self.get_minor(matrix, i))
            )
            det += cofactor

        return det

    # Проверка диагонального преоблодания
    def is_diagonally_dominant(self, matrix):
        n = len(matrix)

        for i in range(n):
            diagonal_element = float(matrix[i][i])
            row_sum = sum(map(float, matrix[i])) - diagonal_element

            if diagonal_element <= row_sum:
                return False

        return True

    # Приведем систему A𝑥 = 𝑏 к виду 𝑥 = 𝐶𝑥 + 𝑑
    def transform(self):
        self.b = [bi / self.A[i][i] for i, bi in enumerate(self.b)]
        self.A = [
            [0.0 if i == j else (-1) * d / self.A[i][i] for j, d in enumerate(row)]
            for i, row in enumerate(self.A)
        ]

    def get_accuracy(self, new_x, old_x):
      return max(abs(a - b) for a, b in zip(new_x, old_x))
    def is_accuracy_reached(self, new_x, old_x, precision):
        return max(abs(a - b) for a, b in zip(new_x, old_x)) < precision

    def iterate(self):
        count = 0
        new_x = list(self.b)
        while True:
            old_x = list(new_x)
            for i in range(len(new_x)):

                new_x[i] = sum(
                    self.A[i][j] * d for j, d in enumerate(new_x)
                ) + self.b[i]
            count += 1
            if self.is_accuracy_reached(new_x, old_x, self.accuracy):
                break
        return [[new_x], self.get_accuracy(new_x, old_x), count]

    def solve(self):
        n = len(self.b)
        x = [0.0] * n

        if not self.is_diagonally_dominant(self.A):
            print("Изначальная матрица не имеет диагонального преобладания")
            self.A = self.make_diagonally_dominant(self.A)
            if self.is_diagonally_dominant(self.A):
                print("Получилось привести матрицу к диагональному преоблоданию")
            else:
                print("Матрицу не получилось привести к диагональному преобладанию")
            self.transform()
            return self.iterate()

        return x
