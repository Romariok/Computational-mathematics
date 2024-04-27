from dataclasses import dataclass
import numpy as np




def f1(x ,y):
   return -2*y+x**2

def f2(x, y):
   return (2*x+4*y-3)/(x + 2*y+1)

def f3(x ,y):
   return y * np.cos(x)

@dataclass
class Differential:
   eq_num: int
   x0: int
   xn: int
   y0: int
   e: int
   h: int
   eq = None
   def init(self):
      match self.eq_num:
         case 1:
            self.eq = f1
         case 2:
            self.eq = f2
         case _:
            self.eq = f3


      

   def Euler(self):
      h = self.h
      quitloop = True
      while quitloop == True:
         x = [self.x0]
         y = [self.y0]
         n = int((self.xn-self.x0)/h)
         for i in range(1, n+1):
            y.append(y[-1] + h*self.eq(x[-1], y[-1]))
            x.append(x[-1]+h)
            
         h /=2
         x1 = [self.x0]
         y1 = [self.y0]
         n = int((self.xn-self.x0)/h)
         for i in range(1, n+1):
            y1.append(y1[-1] + h*self.eq(x1[-1], y1[-1]))
            x1.append(x1[-1]+h)
         if abs(y[1] - y1[1]) <= self.e:
            quitloop = False

            
      return [[x[i], y[i]] for i in range(len(x))]
   
   def ExtendedEuler(self):
      h = self.h
      quitloop = True
      while quitloop == True:
         x = [self.x0]
         y = [self.y0]
         n = int((self.xn-self.x0)/h)
         for i in range(1, n+1):
            x.append(x[-1]+h)
            y.append(y[-1]+h/2*(self.eq(x[-2], y[-1]) + self.eq(x[-1], y[-1] + h*self.eq(x[-2], y[-1]))))
            
         h /=2
         x1 = [self.x0]
         y1 = [self.y0]
         n = int((self.xn-self.x0)/h)
         for i in range(1, n+1):
            x1.append(x1[-1]+h)
            y1.append(y1[-1]+h/2*(self.eq(x1[-2], y1[-1]) + self.eq(x1[-1], y1[-1] + h*self.eq(x1[-2], y1[-1]))))
            
         if abs(y[1] - y1[1])/3 <= self.e:
            quitloop = False

            
      return [[x[i], y[i]] for i in range(len(x))]
   
   def Milne(self):
      x = [self.x0]
      y = [self.y0]
      n = int((self.xn-self.x0)/self.h)
      for i in range(1, n+1):
         x.append(x[-1]+self.h)
              
      for i in range(1, min(n, 4)):
         y.append(y[-1]+self.h/2*(self.eq(x[i-1], y[-1]) + self.eq(x[i], y[-1] + self.h*self.eq(x[i-1], y[-1]))))
      
      for i in range(4, n+1):
         y_pred = y[i-4] + 4 * self.h / 3 * (2*self.eq(x[i-3], y[i-3]) - self.eq(x[i-2], y[i-2]) + 2*self.eq(x[i-1], y[i-1]))
         y_corr = y[i-2] + self.h / 3 * (self.eq(x[i-2], y[i-2]) + 4 * self.eq(x[i-1], y[i-1]) + self.eq(x[i], y_pred))
         while abs(y_pred - y_corr) > self.e:
            y_pred = y_corr
            y_corr = y[i-2] + self.h / 3 * (self.eq(x[i-2], y[i-2]) + 4 * self.eq(x[i-1], y[i-1]) + self.eq(x[i], y_pred))
         y.append(y_corr)
      
      return [[x[i], y[i]] for i in range(len(x))]
      
      
      
   
   