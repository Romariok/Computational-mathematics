from dataclasses import dataclass
from math import factorial

@dataclass
class Interpolation:
   n: int
   x: []
   y: []
   
   
   def difference_table(self):
      n = len(self.y)
      defy = [[0] * n for _ in range(n)]

      for i in range(n):
         defy[i][0] = self.y[i]

      for i in range(1, n):
         for j in range(n - i):
               defy[j][i] = defy[j + 1][i - 1] - defy[j][i - 1]
      self.defy = defy
      return 

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
   
   def gauss(self, v, h):
      a = len(self.y) // 2
      if v>self.x[a]:
         t = (v- self.x[a]) / h
         n = len(self.defy)
         pn = self.defy[a][0] + t * self.defy[a][1] + ((t * (t - 1)) / 2) * self.defy[a - 1][2]
         tn = t * (t - 1)
         for i in range(3, n):
            if i % 2 == 1:
                  n = int((i + 1) / 2)
                  tn *= (t + n - 1)
                  pn += ((tn / factorial(i)) * self.defy[a - n + 1][i])
            else:
                  n = int(i / 2)
                  tn *= (t - n)
                  pn +=((tn / factorial(i)) * self.defy[a - n][i])
            
      elif v < self.x[a]:
         t = (v- self.x[a]) / h
         n = len(self.defy)
         
         pn = self.defy[a][0] + t * self.defy[a - 1][1] + ((t * (t + 1)) / 2) * self.defy[a - 1][2]
         tn = t * (t + 1)
         for i in range(3, n):
            if i % 2 == 1:
                  n = int((i + 1) / 2)
                  tn *= (t + n -1)
            else:
                  n = int(i / 2)
                  tn *= (t - n)

            fact = factorial(i)
            pn += (tn / fact) * self.defy[a - n][i]
      else:
         raise ValueError("Error in Gauss")
      
      return pn

   def bessel(self, v, h):
      n = len(self.x) - 1  
      center = n // 2
      a = self.x[center]
      t = (v - a) / h  
      result = (self.defy[center][0]+self.defy[center+1][0])/2 + (t- 1/2)*self.defy[center][1] + t*(t-1)/2*(self.defy[center - 1][2] + self.defy[center][2])/2
      term = t*(t-1)/2
      for k in range(3, n + 1):
         if k % 2 == 0:
            term /= (t-1/2)
            term*= (t + (k // 2 - 1)) * (t - (k // 2 ))/k
            result += term * (self.defy[center - 1 - (k // 2 - 1)][k] + self.defy[center- (k // 2 - 1 )][k]) / 2
         else:
            term *= (t - 1/2)/ k
            result += term * self.defy[center - k // 2][k]

      return result
   
   def sterling(self, v, h):
      n = len(self.x) - 1  
      center = n // 2
      a = self.x[center]
      t = (v - a) / h 

      result = self.defy[center][0]   + t * (self.defy[center - 1][1] + self.defy[center][1]) / 2 + t**2/2 * self.defy[center - 1][2]
      term = t**2/2 
      for k in range(3, n):
         if k % 2 == 0:
            term *= t / k 
            result += term * self.defy[center - k//2][k]
         else:
            term *= (t**2 - int(k / 2)**2) / (k * t)
            result += term * (self.defy[center - k//2 - 1][k] + self.defy[center - k//2][k]) / 2

      return result