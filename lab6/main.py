import numpy as np

# Differential equation
def f1(x, y):
    return -2 * y + x ** 2

# Implementation of Milne's Method (including the RK4 initialization)
def milne_method(x0, y0, b, h):
    # Initialization with RK4 for the first four points
    def runge_kutta_4(x0, y0, h, steps):
        y = y0
        for _ in range(steps):
            k1 = h * f1(x0, y)
            k2 = h * f1(x0 + 0.5 * h, y + 0.5 * k1)
            k3 = h * f1(x0 + 0.5 * h, y + 0.5 * k2)
            k4 = h * f1(x0 + h, y + k3)
            y += (k1 + 2*k2 + 2*k3 + k4) / 6
            x0 += h
        return y

    n = int((b - x0) / h)
    x_values = np.linspace(x0, b, n + 1)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0

    for i in range(1, 4):
        y_values[i] = runge_kutta_4(x_values[i-1], y_values[i-1], h, 1)

    # Milne's method
    for i in range(3, len(x_values) - 1):
        # Predictor
        y_pred = y_values[i-3] + (4*h/3) * (2*f1(x_values[i-2], y_values[i-2]) - f1(x_values[i-1], y_values[i-1]) + 2*f1(x_values[i], y_values[i]))
        # Corrector
        y_values[i+1] = y_values[i-1] + (h/3) * (f1(x_values[i-2], y_values[i-2]) + 4*f1(x_values[i], y_values[i]) + f1(x_values[i+1], y_pred))

    return x_values, y_values

# Generate dataset
def generate_dataset():
    b_values = [1, 2, 5]
    y0_values = [0, 1, -1]
    h_values = [0.1, 0.05, 0.2]

    for b in b_values:
        for y0 in y0_values:
            for h in h_values:
                x_vals, y_vals = milne_method(0, y0, b, h)
                print(f"Results for b={b}, y0={y0}, h={h}:")
                for x, y in zip(x_vals, y_vals):
                    print(f"x = {x:.2f}, y = {y:.4f}")

generate_dataset()
