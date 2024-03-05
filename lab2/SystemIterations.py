from Equations import int_r, draw_point
import matplotlib.pyplot as plt
import numpy as np


class Iteration_Method:
    n = 0
    data = []
    output = ""

    def __init__(self, eq1, eq2):
        self.equation1 = eq1
        self.equation2 = eq2
        self.data = []

    def increment(self):
        self.n += 1

    def solve(self, a, b, estimate):
        self.data.append(
            (
                "№ итерации",
                "x_1",
                "x_2",
                "|x1_i+1 - x1_i|",
                "|x2_i+1 - x2_i|",
            )
        )
        self.output += "Проверка сходимости метода\n"
        q = max(
            max(
                abs(self.equation1.first_derivative(a, b, 1)),
                abs(self.equation1.first_derivative(a, 0, 1)),
                abs(self.equation1.first_derivative(0, b, 1)),
                abs(self.equation1.first_derivative(0, 0, 1)),
            )
            + max(
                abs(self.equation1.first_derivative(a, b, 2)),
                abs(self.equation1.first_derivative(a, 0, 2)),
                abs(self.equation1.first_derivative(0, b, 2)),
                abs(self.equation1.first_derivative(0, 0, 2)),
            ),
            max(
                abs(self.equation2.first_derivative(a, b, 1)),
                abs(self.equation2.first_derivative(a, 0, 1)),
                abs(self.equation2.first_derivative(0, b, 1)),
                abs(self.equation2.first_derivative(0, 0, 1)),
            )
            + max(
                abs(self.equation2.first_derivative(a, b, 2)),
                abs(self.equation2.first_derivative(a, 0, 2)),
                abs(self.equation2.first_derivative(0, b, 2)),
                abs(self.equation2.first_derivative(0, 0, 2)),
            ),
        )
        self.output += "q = %9.5f\n" % q
        if q > 1:
            self.output += "Процесс не сходится\n"
            return [self.output]
        else:
            self.output += "Процесс сходится\n\n"
        self.output += "\nВыбор начального приближения\n"
        x = a
        y = b
        while self.n<=100:
            x1 = self.equation1.get_value(x, y, 1)
            y1 = self.equation2.get_value(x, y, 1)
            e1 = abs(x1 - x)
            e2 = abs(y1 - y)
            self.print_line(self.n, x1, y1, e1, e2)
            if e1 <= estimate and e2 <= estimate:
                self.increment()
                break
            x = x1
            y = y1
            self.increment()
        self.output += "\nРезультат выполнения: \n"
        self.output += (
            "x1 = %6.5f x2 = %6.5f f1(x1, x2) = %4.5f f2(x1, x2) = %4.5f Количество итераций: %2d"
            % (
                int_r(x1),
                int_r(y1),
                int_r(self.equation1.get_value(x, y)),
                int_r(self.equation2.get_value(x, y)),
                self.n,
            )
        )
        return [self.data, self.output]

    def print_line(self, n, x1, x2, abs1, abs2):
        self.data.append(
            (
                "%-5d" % (n),
                "%9.5f" % (x1),
                "%9.5f" % (x2),
                "%9.5f" % (abs1),
                "%9.5f" % (abs2),
            )
        )
