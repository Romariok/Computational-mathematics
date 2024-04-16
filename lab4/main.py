import Approximation

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
y = [0.0, 0.0888, 0.1722, 0.2628, 0.34, 0.4, 0.4334, 0.436, 0.4114, 0.3692, 0.32]

def f(x):
   return 0.17631*x + 0.11766
def g(x):
   return -0.2386*x**2 + 0.6535*x - 0.0255

sum_x = sum([(y[i]-f(x[i]))**2 for i in range(len(y))])
sum_xx = sum([(y[i]-g(x[i]))**2 for i in range(len(y))])
print((sum_x/11)**0.5)
print((sum_xx/11)**0.5)

# function, m = Approximation.find_best_function(len(x), x, y)
# calculator = Approximation.ApproximationCalculator(function, x, y,[], m)
# coefficients = calculator.calculate_coefficients()
# phi_values = calculator.get_phi_values()
# epsilon_values = calculator.get_epsilon_values()
# pearson_coefficient = calculator.calculate_pearson_correlation()
# print(calculator.print_function())
# print(coefficients)
# print(phi_values)
# print(epsilon_values)
# print(pearson_coefficient)
