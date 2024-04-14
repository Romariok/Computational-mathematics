import numpy as np
from enum import Enum
from dataclasses import dataclass

ACCURACY = 0.001


class Function(str, Enum):
    Polynomial = '0'
    Exponential = '3'
    Logarithmic = '4'
    Power = '5'


@dataclass
class ApproximationCalculator:
    function: Function
    x: []
    y: []
    coefficients: []
    m: int = -1

    def calculate_coefficients(self):
        self.coefficients = approximation_calculation(
            self.function, len(self.x), self.x, self.y, m = self.m
        )
        return self.coefficients

    def calculate_differences(self):
        return differences_calculation(
            self.function, len(self.x), self.coefficients, self.x, self.y
        )

    def calculate_standard_deviation(self):
        diffs = self.calculate_differences()
        return standard_deviation_calculation(diffs, len(self.x))

    def calculate_pearson_correlation(self):
        n = len(self.x)
        sum_x = np.sum(self.x)
        sum_y = np.sum(self.y)
        sum_xy = np.sum(
            self.x[i] * self.y[j] if i == j else 0
            for i in range(len(self.x))
            for j in range(len(self.y))
        )
        sum_x_squared = np.sum(x**2 for x in self.x)
        sum_y_squared = np.sum(y**2 for y in self.y)

        numerator = n * sum_xy - sum_x * sum_y
        denominator = (
            (n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2)
        ) ** 0.5

        if denominator == 0.0:
            return [False,"Division by zero (деление на ноль)"]

        r = numerator / denominator

        if abs(r) < 0.8:
            return [False, "No strong linear dependency (линейная зависимость) detected."]

        return [True,r]

    def get_phi_values(self):
        return np.array(
            [get_function_value(self.function, self.coefficients, x) for x in self.x]
        )

    def get_epsilon_values(self):
        return self.y - self.get_phi_values()

    def print_function(self):
        if self.function == Function.Polynomial:
            terms = []
            for i, coeff in enumerate(self.coefficients):
                if coeff == 0 and i != 0:
                    continue
                term = (
                    f"{coeff:.10f}"
                    if i == 0 or not terms
                    else f"{'+' if coeff >= 0 else ''}{coeff:.10f}"
                )
                if i == 1:
                    term += "x"
                elif i > 1:
                    term += f"x^{i}"
                terms.append(term)
            if not terms:
                terms.append("0")
            return "".join(terms)
        elif self.function == Function.Exponential:
            return f"{self.coefficients[0]:.10f}e^{self.coefficients[1]:+.10f}x"
        elif self.function == Function.Logarithmic:
            return f"{self.coefficients[0]:.10f} + {self.coefficients[1]:+.10f}ln(x)"
        elif self.function == Function.Power:
            return f"{self.coefficients[0]:.10f}x^{self.coefficients[1]:+.10f}"


def approximation_calculation(f, n, x, y, m=1):
    if f == Function.Polynomial:
        b = np.zeros(m)
        matrix = np.zeros((m, m))

        for i in range(m):
            b[i] = np.sum(x[k] ** i * y[k] for k in range(n))
            for j in range(m):
                matrix[i, j] = np.sum(x[k] ** (i + j) for k in range(n))

        return linear_calculation(m, matrix, b, ACCURACY)

    elif f == Function.Exponential:
        a = approximation_calculation(Function.Polynomial, n, np.log(x), np.log(y), m=2)
        a[0] = np.exp(a[0])
        return a

    elif f == Function.Logarithmic:
        return approximation_calculation(Function.Polynomial, n, np.log(x), y, m=2)

    elif f == Function.Power:
        return approximation_calculation(
            Function.Polynomial, n, np.log(x), np.log(y), m=2
        )


def linear_calculation(n, a, b, e):
    v_x = np.zeros(n)
    while True:
        delta = 0.0
        for i in range(n):
            s = np.sum(a[i, j] * v_x[j] for j in range(0, i)) + np.sum(
                a[i, j] * v_x[j] for j in range(i + 1, n)
            )
            x = (b[i] - s) / a[i, i]
            d = abs(x - v_x[i])
            if d > delta:
                delta = d
            v_x[i] = x
        if delta < e:
            break
    return v_x


def differences_calculation(f, n, coefficients, x, y):
    differences = np.zeros(n)
    for i in range(n):
        differences[i] = y[i] - get_function_value(f, coefficients, x[i])
    return differences


def get_function_value(f, coefficients, x):
    if f == Function.Polynomial:
        return np.dot(coefficients, [x**i for i in range(len(coefficients))])
    elif f == Function.Exponential:
        # a[0] * exp(a[1] * x)
        return coefficients[0] * np.exp(coefficients[1] * x)
    elif f == Function.Logarithmic:
        # a[0] + a[1] * ln(x)
        return coefficients[0] + coefficients[1] * np.log(x)
    elif f == Function.Power:
        # a[0] * x^a[1]
        return coefficients[0] * x ** coefficients[1]


def standard_deviation_calculation(differences, n):
    var = np.sum(differences**2) / n
    return var**0.5


@staticmethod
def find_best_function(n, x, y):
    deviations = []

    # Polynomial of degree 1 to 3
    for i in range(1, 4):
        func = Function.Polynomial
        approximations = approximation_calculation(func, n, x, y, m=i)
        differences = differences_calculation(func, n, approximations, x, y)
        deviations.append((standard_deviation_calculation(differences, n), func, i))

    # Exponential
    exponential_approximations = approximation_calculation(
        Function.Exponential, n, x, y
    )
    exponential_differences = differences_calculation(
        Function.Exponential, n, exponential_approximations, x, y
    )
    deviations.append(
        (
            standard_deviation_calculation(exponential_differences, n),
            Function.Exponential,
            2,
        )
    )

    # Logarithmic
    logarithmic_approximations = approximation_calculation(
        Function.Logarithmic, n, x, y
    )
    logarithmic_differences = differences_calculation(
        Function.Logarithmic, n, logarithmic_approximations, x, y
    )
    deviations.append(
        (
            standard_deviation_calculation(logarithmic_differences, n),
            Function.Logarithmic,
            2,
        )
    )

    # Power
    power_approximations = approximation_calculation(Function.Power, n, x, y)
    power_differences = differences_calculation(
        Function.Power, n, power_approximations, x, y
    )
    deviations.append(
        (standard_deviation_calculation(power_differences, n), Function.Power, 2)
    )

    deviations.sort(key=lambda x: x[0])
    return [deviations[0][1], deviations[0][2]]
