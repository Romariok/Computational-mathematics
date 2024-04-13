import Approximation
import numpy as np

x = [1.1, 2.3, 3.7, 4.5, 5.4, 6.8, 7.5]
y = [2.73, 5.12, 7.74, 8.91, 10.59, 12.75, 13.43]


function, m = Approximation.find_best_function(len(x), x, y)
calculator = Approximation.ApproximationCalculator(function, x, y, np.zeros(len(x)), m)
coefficients = calculator.calculate_coefficients()
phi_values = calculator.get_phi_values()
epsilon_values = calculator.get_epsilon_values()
pearson_coefficient = calculator.calculate_pearson_correlation()
print(calculator.print_function())
print(coefficients)
print(phi_values)
print(epsilon_values)
print(pearson_coefficient)
