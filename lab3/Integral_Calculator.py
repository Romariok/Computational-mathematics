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
    return 1 / (1 - x**2)


def hyperbola(x):
    return 1 / x


def quadratic_primitive(x):
    return x**3 + x**2 - 5 * x


def exponent_primitive(x):
    return math.exp(x)


def hyperbolic_cosine_primitive(x):
    return math.sinh(x)


def polynom_primitive(x):
    return x**4 / 4 + x**3 - (5*x**2)/2+7*x


def root_primitive(x):
    return 1/2*math.log(x+1) - 1/2*math.log(1-x)


def hyperbola_primitive(x):
    return abs(math.log(x))


class IntegralCalculator:
    def __init__(self, a, b, e, func_choice, method_choice):
        self.a = a
        self.b = b
        self.perm = True
        self.e = e
        self.func = self.choose_function(func_choice)
        self.method = self.choose_method(method_choice)

    def choose_function(self, choice):
        match choice:
            case 1:
                self.interval = [[[math.pow(10, -10), math.pow(10, 10)]], []]
                self.primitive = quadratic_primitive
                return quadratic
            case 2:
                self.interval = [[[-math.pow(10, 10), math.pow(10, 10)]], []]
                self.primitive = exponent_primitive
                return exponent
            case 3:
                self.interval = [[[-math.pow(10, 10), math.pow(10, 10)]], []]
                self.primitive = hyperbolic_cosine_primitive
                return hyperbolic_cosine
            case 4:
                self.interval = [[[-math.pow(10, 10), math.pow(10, 10)]], []]
                self.primitive = polynom_primitive
                return polynom
            case 5:
                self.interval = [[[-math.pow(10, 10),-1],[-1, 1], [1, math.pow(10, 10)]], [-1, 1]]
                self.primitive = root_primitive
                return root
            case 6:
                self.interval = [[[-math.pow(10, 10), 0], [0, math.pow(10, -10)]], [0]]
                self.primitive = hyperbola_primitive
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

    def check_range(self, ranges):
        for r in ranges:
            if self.a >= r[0] and self.b <= r[1]:
                return True
        return False

    def check_convergence(self, points):
        intervals_count = 0
        intervals: list[tuple(float, float)] = []

        for point in points:
            if point < self.a or point > self.b:
                continue
            try:
                antiderivative_value = self.primitive(point)
            except:
                return []

            if math.isnan(antiderivative_value) or math.isinf(antiderivative_value):
                return []  # Function does not converge in this interval

            deviation = 0.000000001
            if abs(point - self.a) < deviation:
                intervals.append(tuple([point + deviation, self.b]))
                intervals_count += 1
            elif abs(self.b - point) < deviation:
                if not intervals:
                    intervals.append(tuple([self.a, self.b - deviation]))
                else:
                    intervals[intervals_count - 1] = (
                        intervals[intervals_count - 1][0],
                        self.b - deviation,
                    )
            else:
                if intervals_count > 0:
                    intervals[intervals_count - 1] = (
                        intervals[intervals_count - 1][0],
                        point - deviation,
                    )
                intervals.append(tuple([point + deviation, self.b]))
                intervals_count += 1
        if len(intervals) == 0:
            return [tuple([self.a, self.b])]
        else:
            return intervals

    def check_n_calculate(self):
        ranges, points = self.interval
        if not self.check_range(ranges):
            print("Интеграл расходится")
            self.perm = False
        else:
            intervals = self.check_convergence(points)
            if len(intervals) == 0:
                print("Интеграл расходится")
                self.perm = False
            else:
                summ = 0
                for interval in intervals:
                    value, num, error = self.calculate_integral(4, interval)
                    summ += value
                return summ, num, error
        return tuple([0, 0, 0])  
            
        
        return tuple([value, num, error])

    def calculate_integral(self, n, interval):
        if self.perm:
            start, end = interval
            num = n
            while num <= 1000000:
                h = (end - start) / num
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
            return tuple([0, 0, 0])

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
