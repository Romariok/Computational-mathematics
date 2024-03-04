from PyQt5 import QtWidgets, uic
import matplotlib.pyplot as plt
import Newton
import Iterations
import Chord
import Equations
import SystemEquations
import SystemIterations
import sys



# app = QtWidgets.QApplication([])
# win = uic.loadUi("lab2\lab2.ui") 
 
# win.show()
# sys.exit(app.exec())
eq1 = SystemEquations.Equations(1)
eq2 = SystemEquations.Equations(2)
# solver= SystemIterations.Iteration_Method(eq1, eq2)
# solver.solve(0.01)  

left = -2
right = -1
eqq1 = Equations.Equation(1)
solver = Iterations.Iteration_Method(eqq1)

solver.solve(left, right, 0.01)
k_left, k_right = 1.2, 1.2
if left> 0:
    k_left = 0.8
if right < 0:
    k_right = 0.8
eqq1.draw_graph(k_left * left, k_right * right)
plt.show()