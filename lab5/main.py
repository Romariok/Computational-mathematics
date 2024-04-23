from Interpolation import Interpolation
import numpy as np
# x = [0.1, 0.2, 0.3, 0.4, 0.5]
# y = [1.25, 2.38, 3.79, 5.44, 7.14]

x = [0.15, 0.2, 0.33, 0.47, 0.62]
y = [1.25, 2.38, 3.79, 5.44, 7.14]

calculator = Interpolation(5, x, y)




print(calculator.newton(0.22))


def fun1(x):
   return np.sin(x)
a = 4.3
b = 9.61
n = 8

h = (b-a)/n
x = [a+h*i for i in range(n)]
y = [fun1(x[i]) for i in range(n)]
calculator = Interpolation(n, x, y)

print(calculator.newton(5.62))