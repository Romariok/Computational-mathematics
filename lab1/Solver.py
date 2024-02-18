import sys

class GaussSeidelSolver:
    def __init__(self, A, b, accuracy):
        self.A = A
        self.b = b
        self.accuracy = accuracy
        self.max_iterations = -1
        if not self.is_matrix_non_singular():
            raise ValueError("Матрица вырожденная. Решение невозможно.")

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
            try:
                max_element_index = matrix[i].index(max_element)
            except ValueError:
                max_element_index = matrix[i].index(-max_element)

            matrix[i], matrix[max_element_index] = matrix[max_element_index], matrix[i]
            self.b[i], self.b[max_element_index] = self.b[max_element_index], self.b[i]

        return matrix

    # Рекурсивный метод вычисления определителя
    def calculate_determinant(self, matrix):
        det = 1.0
        n = len(matrix)

        for i in range(n):
            # Find pivot for column i and swap if necessary
            max_row = max(range(i, n), key=lambda j: abs(matrix[j][i]))
            if matrix[max_row][i] == 0.0:
                return 0.0  
            if max_row != i:
                matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                det *= -1.0

            pivot = matrix[i][i]
            det *= pivot

            # Forward elimination
            for j in range(i + 1, n):
                factor = matrix[j][i] / pivot
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]
        print(f"Значение детерминанта: {det}")
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
                new_x[i] = (
                    sum(self.A[i][j] * d for j, d in enumerate(new_x)) + self.b[i]
                )
            count += 1
            if (
                self.is_accuracy_reached(new_x, old_x, self.accuracy)
                or count == self.max_iterations
            ):
                break
        return [[new_x], self.get_accuracy(new_x, old_x), count]

    def solve(self):
        if not self.is_diagonally_dominant(self.A):
            print("Изначальная матрица не имеет диагонального преобладания")
            old_A= list(self.A)
            self.A = self.make_diagonally_dominant(self.A)
            if self.is_diagonally_dominant(self.A):
                print("Получилось привести матрицу к диагональному преоблоданию")
            else:
                print("Матрицу не получилось привести к диагональному преобладанию\n")
                self.A=list(old_A)
                while True:
                    try:
                        self.max_iterations = int(input("Введите желаемое количество итераций: "))
                        break  
                    except ValueError:
                        print("Ошибка: Введено некорректное число. Пожалуйста, введите целое число.")


        self.transform()
        return self.iterate()

