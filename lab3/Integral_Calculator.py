import math


def quadratic(x):
    return 3 * x**2 + 2 * x - 5


def exponent(x):
    return math.exp(x)


def hyperbolic_cosine(x):
    return math.cosh(x)


def polynom(x):
    return 2 * x**3 + 3 * x**2 - 5 * x + 7


def root(x):
    return 1 / math.sqrt(1 - x**2)


def hyperbola(x):
    return 1 / x


class IntegralCalculator:
    def __init__(self, a, b, e, func_choice, method_choice):
        self.a = a
        self.b = b
        self.perm = True
        self.e = e
        self.func = self.choose_function(func_choice)
        self.method = self.choose_method(method_choice)

    def check_invalid(self):
        if self.func == root:
            if self.a > 1 or self.b > 1 or self.a < -1 or self.b < -1:
                print("Интеграл расходится")
                self.perm = False
            elif self.b == 1:
                print("Интервал интегрирования заходит на точки разрыва - 1")
                self.b = self.b - 0.00000000001
            if self.a == -1:
                print("Интервал интегрирования заходит на точки разрыва - -1")
                self.a = self.a + 0.00000000001
        if self.func == hyperbola:
            if self.a < 0 and self.b > 0:
                self.perm = False
                print("Интеграл расходится")
            elif self.a == 0 and self.b > 0:
                self.a = self.a + 0.00000000001
            if self.a < 0 and self.b == 0:
                self.b = self.b - 0.00000000001

    def choose_function(self, choice):
        match choice:
            case 1:
                return quadratic
            case 2:
                return exponent
            case 3:
                return hyperbolic_cosine
            case 4:
                return polynom
            case 5:
                return root
            case 6:
                return hyperbola

    def choose_method(self, choice):
        match choice:
            case 1:
                return self.left_rectangles
            case 2:
                return self.right_rectangles
            case 3:
                return self.middle_rectangles
            case 4:
                return self.trapezoid
            case 5:
                return self.simpson

    def calculate_integral(self, n):
        if self.perm:
            num = n
            while num <= 1000000:
                h = (self.b - self.a) / num
                if self.method == self.simpson:
                    coefficient = 15
                else:
                    coefficient = 3

                integral_value = self.method(num, h)
                error = abs(integral_value - self.method(2 * num, h / 2)) / coefficient
                if error <= self.e:
                    break
                num *= 2

            return integral_value, num, error
        else:
            print("Значение данного интеграла подсчитать нельзя!")
            return 0, 0, 0

    def left_rectangles(self, n, h):
        total = 0
        for i in range(n):
            total += self.func(self.a + i * h)
        return h * total

    def right_rectangles(self, n, h):
        total = 0
        for i in range(1, n + 1):
            total += self.func(self.a + i * h)
        return h * total

    def middle_rectangles(self, n, h):
        total = 0
        for i in range(n):
            total += self.func(self.a + (i + 0.5) * h)
        return h * total

    def trapezoid(self, n, h):
        total = 0.5 * (self.func(self.a) + self.func(self.b))
        for i in range(1, n):
            total += self.func(self.a + i * h)
        return h * total

    def simpson(self, n, h):
        total = self.func(self.a) + self.func(self.b)
        for i in range(1, n):
            coef = 4 if i % 2 != 0 else 2
            total += coef * self.func(self.a + i * h)
        return h / 3 * total
