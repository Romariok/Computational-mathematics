from dataclasses import dataclass
import numpy as np


def f1(x ,y):
   return 4*x + y/3
def fy1(x, c):
   return c*np.exp(x/3) - 12*x - 36
def c1(x, y):
   return  (y + 12*x + 36)/np.exp(x/3)


def f2(x, y): 
   return x**2 + y
def fy2(x, c):
   return c * np.exp(x) - x**2 - 2 * x - 2
def c2(x, y):
   return (-y - x**2 - 2 * x - 2) / (-np.exp(x))

def f3(x ,y):
   return y * np.cos(x)
def fy3(x, c):
   return c * np.exp(np.sin(x))
def c3(x, y):
   return y /np.exp(np.sin(x))

@dataclass
class Differential:
   eq_num: int
   x0: int
   xn: int
   y0: int
   e: int
   h: int
   eq = None
   fy = None
   c = None
   def init(self):
      match self.eq_num:
         case 1:
            self.eq = f1
            self.fy = fy1
            self.c = c1(self.x0, self.y0)
         case 2:
            self.eq = f2
            self.fy = fy2
            self.c = c2(self.x0, self.y0)
         case _:
            self.eq = f3
            self.fy = fy3
            self.c = c3(self.x0, self.y0)


   def Direct(self):
      n = int((self.xn-self.x0)/self.h)
      x = [self.x0]
      y = [self.y0]
      for i in range(1, n+1):
         x.append(x[-1]+self.h)
         
         
      for i in range(1, n+1):
         y.append(self.fy(x[i], self.c))
         
      return [["{:.3f}".format(x[i]), "{:.3f}".format(y[i])] for i in range(len(x))]  
         
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

            
      return [["{:.3f}".format(x[i]), "{:.3f}".format(y[i])] for i in range(len(x))]
   
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

            
      return [["{:.3f}".format(x[i]), "{:.3f}".format(y[i])] for i in range(len(x))]
   
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
      
      return [["{:.3f}".format(x[i]), "{:.3f}".format(y[i])] for i in range(len(x))]
      
      
      
   
   