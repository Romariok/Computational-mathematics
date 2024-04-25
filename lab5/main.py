from Interpolation import Interpolation
import numpy as np

# x = [1.05, 1.15, 1.25, 1.35, 1.45, 1.55, 1.65]
# y = [0.1213, 1.1316, 2.1459, 3.1565, 4.1571, 5.1819, 6.1969]
x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = [1.25, 2.38, 3.79, 5.44, 7.14]

calculator = Interpolation(5, x, y)
calculator.difference_table()
# for i in calculator.defy:
#    s = ""
#    for j in i:
#       s+=f"{float(j):.4} &"
#    s = s[:len(s)-1]
#    s+="\\\\"
#    print(s)

print(calculator.lagrange(0.32))