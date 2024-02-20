import sys
import Solver
import Generator

def main(): # -f - прочитать данные из файла; -g - генерить матрицу, размерность матрицы 
   argv = sys.argv[1:]
   A = []
   b = []
   if len(argv)==0:
      argv.append(0)

   match argv[0]:
      case "-f":
         with open(argv[1], "r") as f:
            try:
               n = int(f.readline().replace(",", "."))
               for i in range(n):
                  s = f.readline().replace(",", ".").split(" ")
                  s=[float(i)  for i in s]
                  A.append(s[:n])
                  b.append(float(s[-1]))
               accuracy = float(f.readline().replace(",", "."))
            except ValueError:
               print("Неправильный ввод данных")
               sys.exit()
      case "-g":
         n=int(argv[1])
         generator = Generator.Generator(n)
         data = generator.generate_matrix()
         for i in range(n):
            s = data[0][i]
            A.append(s[:n])
            b.append(s[-1])
         accuracy=data[1]
      case _:
         try:
            n = int(input("Введите размерность матрицы: ").replace(",", "."))
            data = [input().replace(",", ".").split(" ") for _ in range(n)]
            if len(data)!=n:
               print("Неверное количество строк",len(data))
               raise ValueError

            for i in data:
               if len(i)!=n+1:
                  print("Неверное количество столбцов", len(i))
                  raise ValueError
            data.append(float(input("Введите точность, до которой будем производить вычисления: ")[-2:]))

            for i in range(n):
               s = data[i]
               s=[float(i)  for i in s]
               A.append(s[:n])
               b.append(float(s[-1]))
            accuracy=data[-1]
         except ValueError:
            print("Неправильный ввод данных")
            sys.exit()  


   print("\nПолученная матрица: ")
   for i in A:
      print(*i)
   print("Полученный вектор ответов:")
   print(*b)
   print(f"Заданная погрешность: {accuracy}\n")
   solver = Solver.GaussSeidelSolver(A, b, accuracy)
   solution = solver.solve()

   print("Получившийся вектор:")
   print(*solution[0])
   print(f"Получившаяся погрешность: {solution[1]}")
   print(f"Количество итераций: {solution[2]}")

   

if __name__ == "__main__":
   main()

