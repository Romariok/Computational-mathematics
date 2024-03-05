from Equations import int_r, draw_point
import matplotlib.pyplot as plt
import numpy as np


class Iteration_Method:
    n = 0
    data = []
    output = ""

    def __init__(self, eq):
        self.equation = eq
        self.data = []

    def increment(self):
        self.n += 1

    def solve(self, left, right, estimate):
        if self.equation.get_value(left) * self.equation.get_value(right) > 0:
            return ["На данном участке нет корней\несколько корней "]

        self.data.append(
            ("№ итерации", "x_i", "x_i+1", "φ(x_i+1)", "f(x_i+1)", "|x_i+1 - x_i|")
        )
        if self.equation.first_derivative(left) > 0:
            parameter_lambda = -1 / max(
                self.equation.first_derivative(left),
                self.equation.first_derivative(right),
            )
        else:
            parameter_lambda = 1 / max(
                self.equation.first_derivative(left),
                self.equation.first_derivative(right),
            )
        if (
            abs(self.new_function_first_derivative(left, parameter_lambda)) >= 1
            or abs(self.new_function_first_derivative(right, parameter_lambda)) >= 1
        ):
            self.output += "φ(a) = %9.5f\n" % self.new_function_first_derivative(
                left, parameter_lambda
            )
            self.output += "φ(b) = %9.5f\n" % self.new_function_first_derivative(
                right, parameter_lambda
            )
            self.output += "Метод не сходится. Нарушено достаточное условие сходимости метода.\nУменьшите рассматриваемый промежуток\n"
            return [self.output]

        if self.equation.get_value(right) * self.equation.second_derivative(right) > 0:
            x0 = right
        else:
            x0 = left
        self.output += "φ'(x) = %9.5f\n" % self.new_function_first_derivative(
            x0, parameter_lambda
        )

        self.draw_new_function(left, right, parameter_lambda)
        while self.n<=100:
            x = self.new_function(x0, parameter_lambda)
            draw_point(x0, self.new_function(x0, parameter_lambda), self.n, "g", "φ")
            draw_point(x0, self.equation.get_value(x0), self.n, "b", "x")
            self.print_line(self.n, x0, x, parameter_lambda)
            if abs(x - x0) <= estimate:
                self.increment()
                draw_point(x, self.equation.get_value(x), self.n, "r", "x")
                break
            x0 = x
            self.increment()
        self.output += "\nРезультат выполнения: \n"
        self.output += "x = %6.5f f(x) = %4.5f Количество итераций: %2d\n" % (
            int_r(x),
            int_r(self.equation.get_value(x)),
            self.n,
        )
        return [self.data, self.output]

    def new_function(self, x, parameter_lambda):
        return x + parameter_lambda * self.equation.get_value(x)

    def new_function_first_derivative(self, x, parameter_lambda):
        return 1 + parameter_lambda * self.equation.first_derivative(x)

    def draw_new_function(self, left, right, parameter_lambda):
        k_left, k_right = 1.2, 1.2
        if left > 0:
            k_left = 0.8
        if right < 0:
            k_right = 0.8
        x = np.arange(left * k_left, right * k_right, 0.01)
        y = self.new_function(x, parameter_lambda)
        plt.plot(x, y, c="g")

    def print_line(self, n, x0, x, parameter_lambda):
        self.data.append(
            (
                "%-5d" % n,
                "%9.5f" % int_r(x0),
                "%11.5f" % int_r(x),
                "%9.5f" % int_r(self.new_function(x0, parameter_lambda)),
                "%9.5f" % int_r(self.equation.get_value(x0)),
                "%9.5f" % int_r(abs(x0 - x)),
            )
        )
