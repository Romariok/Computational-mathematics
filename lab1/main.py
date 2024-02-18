import sys
import Solver
import Generator

def main(): # -f - прочитать данные из файла; -g - генерить картинку, размерность матрицы 
   argv = sys.argv[1:]
   A = []
   b = []
   if argv[0]=="-f":
      with open(argv[1], "r") as f:
         n = int(f.readline())
         for i in range(n):
            s = f.readline().split(" ")
            s=[float(i)  for i in s]
            A.append(s[:n])
            b.append(float(s[-1]))
         accuracy = float(f.readline())
   elif argv[0]=="-r":
      n=int(argv[1])
      generator = Generator.Generator(n)
      data = generator.generate_matrix()
      for i in range(n):
         s = data[0][i]
         A.append(s[:n])
         b.append(s[-1])
      accuracy = data[-1]

      print(*A, *b, accuracy)

      
   
   solver = Solver.GaussSeidelSolver(A, b, accuracy)
   solution = solver.solve()

   print(f"Получившийся вектор: {solution[0]}")
   print(f"Получившаяся погрешность{solution[1]}")
   print(f"Количество итераций: {solution[2]}")

   

if __name__ == "__main__":
   main()

