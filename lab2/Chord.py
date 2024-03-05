from Equations import int_r, draw_point, draw_chord
import matplotlib.pyplot as plt
import numpy as np


class Chord:
    n = 0
    data = []

    def __init__(self, equation):
        self.equation = equation
        self.data = []

    def increment(self):
        self.n += 1

    def solve(self, a, b, e):
        self.data.append(
            ("№ итерации", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|x_i+1-x_i|")
        )
        if self.equation.get_value(a) * self.equation.get_value(b) > 0:
            return ["На данном участке нет корней\несколько корней"]
        while self.n<=100:
            x = a - (
                (b - a) / (self.equation.get_value(b) - self.equation.get_value(a))
            ) * self.equation.get_value(a)
            draw_point(x, 0, self.n, "b", "x")
            draw_chord(a, self.equation.get_value(a), b, self.equation.get_value(b))
            if self.equation.get_value(x) * self.equation.get_value(a) > 0:
                self.print_line(
                    self.n,
                    a,
                    b,
                    x,
                    self.equation.get_value(a),
                    self.equation.get_value(b),
                    self.equation.get_value(x),
                    b - x,
                )
                a = x
                abss = b - x
            else:
                self.print_line(
                    self.n,
                    a,
                    b,
                    x,
                    self.equation.get_value(a),
                    self.equation.get_value(b),
                    self.equation.get_value(x),
                    a - x,
                )
                b = x
                abss = a - x
            if abs(abss) <= e or abs(self.equation.get_value(x)) < e:
                break
            self.increment()

        return [
            self.data,
            "\nx = %6.5f f(x) = %4.5f Количество итераций: %2d"
            % (int_r(x), int_r(self.equation.get_value(x)), self.n + 1),
        ]

    def print_line(self, n, a, b, x, f_a, f_b, f_x, abss):
        self.data.append(
            (
                "%-5d" % (n),
                "%9.5f" % (int_r(a)),
                "%9.5f" % (int_r(b)),
                "%9.5f" % (int_r(x)),
                "%9.5f" % (int_r(f_a)),
                "%9.5f" % (int_r(f_b)),
                "%9.5f" % (int_r(f_x)),
                "%9.5f" % (int_r(abs(abss))),
            )
        )

