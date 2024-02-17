import os

class GaussSeidelSolver:
   def __init__(self, A, b, tolerance, max_iterations=100):
      self.A = A
      self.b = b
      self.tolerance = tolerance

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

    return matrix

   # Рекурсивный метод вычисления определителя
   def calculate_determinant(self, matrix):
      
      size = len(matrix)

      if size == 1:
         return float(matrix[0][0])

      if size == 2:
         return float(matrix[0][0]) * float(matrix[1][1]) - float(matrix[0][1]) * float(matrix[1][0])

      det = 0.0
      for i in range(size):
         cofactor = (-1) ** i * float(matrix[0][i]) * self.calculate_determinant(self.get_minor(matrix, i))
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


   def solve(self):
      n = len(self.b)
      x = [0.0] * n  # начальное приближение     


      if not self.is_diagonally_dominant(self.A):
         print("Изначальная матрица не имеет диагонального преобладания")
         matrix = self.make_diagonally_dominant(self.A)
         if self.is_diagonally_dominant(matrix):
            print("Получилось привести матрицу к диагональному преоблоданию")
         else:
            print("Матрицу не получилось привести к диагональному преобладанию")

      return x
      

