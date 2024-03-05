import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np


def int_r(num):
    num = int(num * 100000 + (0.5 if num * 100000 > 0 else -0.5)) / 100000
    return num


class Equations:
    def __init__(self, number):
        if number == 1:
            self.equation = lambda x, y: np.sin(y) - 2 * x - 2
            self.equivalent = lambda x, y: (np.sin(y) - 2) / 2
        if number == 2:
            self.equation = lambda x, y: np.cos(x + 0.5) + y - 1
            self.equivalent = lambda x, y: 1 - np.cos(x + 0.5)
        if number == 3:
            self.equation = lambda x, y: np.sin(x+1)-y-1.2
            self.equivalent = lambda x, y: np.sin(x+1)-1.2
        if number == 4:
            self.equation = lambda x, y: 2*x+np.cos(y)-2
            self.equivalent = lambda x, y: (2-np.cos(y))/2
    def get_value(self, x, y, num=0):
        if num == 0:
            return self.equation(x, y)
        if num == 1:
            return self.equivalent(x, y)

    def first_derivative(self, x, y, num):
        h = 0.000001
        if num == 1:
            return (self.equivalent(x + h, y) - self.equivalent(x, y)) / h
        if num == 2:
            return (self.equivalent(x, y + h) - self.equivalent(x, y)) / h

    def draw_graph(self, left, right):
        x = np.linspace(left, right, 100)
        y = np.linspace(left, right, 100)
        x, y = np.meshgrid(x, y)
        z = self.get_value(x, y)
        plt.contour(x, y, z, levels=[0], colors="r")
        plt.grid(True)
