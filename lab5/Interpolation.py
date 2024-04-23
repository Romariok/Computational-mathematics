from dataclasses import dataclass
import numpy as np

@dataclass
class Interpolation:
   n: int
   x: []
   y: []
   
   

   def lagrange(self, v):
      sum = 0.0
      for i in range(self.n):
            product = 1.0
            for j in range(self.n):
               if j == i:
                  continue
               else:
                  product *= (v - self.x[j]) / (self.x[i] - self.x[j])
            sum += self.y[i] * product
      return sum


   def diff(self, k, i):
      n = len(self.x)
      if k == 0:
         return self.y[i]
      elif i + k >= n:
         raise ValueError("Index out of bounds")
      else:
         return (self.diff(k - 1, i + 1) - self.diff(k - 1, i)) / (self.x[i + k] - self.x[i])

   def newton(self, v):
      sum = self.y[0]
      for i in range(1, self.n):
            product = 1.0
            for j in range(i):
               product *= v - self.x[j]
            sum += self.diff(i, 0) * product
      return sum


   def gauss(self, v):
      h = self.x[1] - self.x[0]
      x0 = self.x[self.n // 2]

      t = (v - x0) / h
      sum = self.y[self.n // 2]
      for i in range(1, self.n):
            product = t
            delta = 0.0
            for j in range(1, i):
               product *= (t - delta * (-1) ** (j % 2)) / j
               delta += (j % 2)
            sum += self.diff(i, (self.n - i) // 2) * product
      return sum
