import sys
import Integral_Calculator


def main():  # -f - прочитать данные из файла
    argv = sys.argv[1:]

    if len(argv) == 0:
        argv.append(0)

    match argv[0]:
        case "-f":
            with open(argv[1], "r") as f:
                try:
                    m, n, a, b, e = map(float, f.readline().split(" "))
                    n = int(n)
                    m = int(m)
                    if n < 1 or n > 4 or m < 1 or m > 5:
                        raise KeyboardInterrupt
                except ValueError:
                    print("Неправильный ввод данных")
                    sys.exit()
                except KeyboardInterrupt:
                    print("ПНеправильный номер функции или метода")
                    sys.exit()
        case _:
            try:
                print(
                    "Доступные уравнения:\n1: 3 * x**2 + 2 * x - 5\n2: exp(x)\n3: cosh(x)\n4: 2 * x**3 + 3 * x**2 - 5 * x + 7"
                )
                n = int(input("Введите номер уравнения: "))
                if n < 1 or n > 4:
                    raise KeyboardInterrupt
                print(
                    "Доступные методы:\n1: Метод прямоугольника(левых)\n2: Метод прямоугольника(правых)\n3: Метод прямоугольника(средних)\n4: Метод Трапеций\n5: Метод Симпсона"
                )
                m = int(input("введите номер метода: "))
                if m < 1 or m > 5:
                    raise KeyboardInterrupt
                a = float(input("Введите левую границу интегрирования: "))
                b = float(input("Введите правую границу интегрирования: "))
                if b <= a:
                    raise KeyError
                e = float(input("Введите точность интегрирования: "))
                if e <= 0:
                    raise FileNotFoundError

            except ValueError:
                print(
                    "Для номеров должно быть целое число\nДля остального - с фиксированной точкой"
                )
                sys.exit()
            except KeyboardInterrupt:
                print("Ввод не из пула номеров")
                sys.exit()
            except KeyError:
                print("Границы неправильно введены")
                sys.exit()
            except FileNotFoundError:
                print("Погрешность неправильно введена")
                sys.exit()
    print(
        f"Принятые данные из файла\nНомер метода: {m}\nНомер функции:{n}\nГраницы интегрирования [{a}, {b}]\nТочность: {e}"
    )

    calculator = Integral_Calculator.IntegralCalculator(a, b, e, n, m)
    integral, n, error = calculator.calculate_integral(4)
    print(f"Calculated integral: {integral}\nNumber of intervals: {n}\nError: {error}")


if __name__ == "__main__":
    main()
