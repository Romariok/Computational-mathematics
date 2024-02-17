import sys
import Solver

def main(): # file - прочитать данные из файла; rand - генерить картинку, n - размерность матрицы 
   argv = sys.argv[1:]
   A = []
   b = []
   if argv[0]=="file":
      with open(argv[1], "r") as f:
         n = int(f.readline())
         for i in range(n):
            s = f.readline().split(" ")
            s=[float(i) for i in s]
            A.append(s[:n])
            b.append(float(s[-1]))
         accuracy = float(f.readline())
   solver = Solver.GaussSeidelSolver(A, b, accuracy)
   solution = solver.solve()

   print(f"Получившийся вектор: {solution[0]}")
   print(f"Получившаяся погрешность{solution[1]}")
   print(f"Количество итераций: {solution[2]}")
   

if __name__ == "__main__":
   main()

