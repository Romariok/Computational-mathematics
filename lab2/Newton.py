from Equations import int_r, draw_point, draw_tangent
import matplotlib.pyplot as plt
import numpy as np


class Newton:
    n = 0
    data = []

    def __init__(self, equation):
        self.equation = equation
        self.data = []

    def increment(self):
        self.n += 1

    def solve(self, a, b, e):
        self.data.append(
            ("№ итерации", "x_i", "f(x_i)", "f'(x_i)", "x_i+1", "|x_i+1 - x_i|")
        )
        if self.equation.get_value(a) * self.equation.get_value(b) > 0:
            return ["На данном участке нет корней\несколько корней"]
        if self.equation.get_value(b) * self.equation.second_derivative(b) > 0:
            x0 = b
        else:
            x0 = a
        try:
            x = x0 - (self.equation.get_value(x0) / self.equation.first_derivative(x0))
        except ZeroDivisionError:
            return [
                "Уточните входной интервал. Первая производная на промежутке равна нулю"
            ]
        self.print_line(self.n, x0, x)
        draw_point(x, 0, self.n, "b", "x")
        draw_tangent(x0, self.equation.get_value(x0), x)
        while self.n<=100:
            self.increment()
            x0 = x
            x = x0 - (self.equation.get_value(x0) / self.equation.first_derivative(x0))
            draw_point(x, 0, self.n, "b", "x")
            draw_tangent(x0, self.equation.get_value(x0), x)
            self.print_line(self.n, x0, x)
            if abs(x - x0) <= e and abs(self.equation.get_value(x)) < e:
                draw_point(x, 0, self.n, "r", "x")
                break

        return [
            self.data,
            "x = %6.5f f(x) = %4.5f Количество итераций: %2d"
            % (int_r(x), int_r(self.equation.get_value(x)), self.n + 1),
        ]

    def print_line(self, n, x0, x):
        self.data.append(
            (
                "%-5d" % (n),
                "%9.5f" % (int_r(x0)),
                "%9.5f" % (int_r(self.equation.get_value(x0))),
                "%11.5f" % (int_r(self.equation.first_derivative(x0))),
                "%9.5f" % (int_r(x)),
                "%9.5f" % (int_r(abs(x0 - x))),
            )
        )
