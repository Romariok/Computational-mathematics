from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import lab4.Approximation as Approximation
import lab5.Interpolation as Int
import lab6.DifferentialEquations as diff

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})

@app.route("/lab6/app", methods=["POST"])
def solve_differential():
    try:
        data = request.get_json()
        eq_num = data.get("eq_num", 0)
        x0 = data.get("x0", 0)
        xn = data.get("xn", 0)
        y0 = data.get("y0", 0)
        e = data.get("eps", 0)
        h = data.get("h", 0)
        print(eq_num, x0, xn, y0, e, h)
        if x0>=xn or e <=0 or h <=0 or eq_num < 1 or eq_num > 3:
            raise KeyboardInterrupt
        
        calculator = diff.Differential(eq_num, x0, xn, y0, e, h)
        calculator.init()
        
        answer = {"euler": calculator.Euler(), "ext_euler": calculator.ExtendedEuler(), "milne": calculator.Milne(), "direct": calculator.Direct() }
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные")), 400
    except ValueError as ee:
        return jsonify(error=str(ee)), 400

@app.route("/lab5/function", methods=["POST"])
def solve_interpolation_function():  
    def fun1(x):
        return 2*np.sin(x) - 4
    def fun2(x):
        return 13 - 5*np.cos(x)
    try:
        data = request.get_json()
        n = data.get("n", 0)
        a = data.get("a", 0)
        b = data.get("b", 0)
        if a>=b or n <=0:
            raise KeyboardInterrupt
        x = []
        y = []
        num = data.get("num", 0)
        if num<1 or num >2:
            raise ValueError("Error: unknown number of file")
        
        h = (b-a)/n
        x = [a+h*i for i in range(n)]
        if num ==1: 
            y = [fun1(x[i]) for i in range(n)]
        else:
            y = [fun2(x[i]) for i in range(n)]
        
        values = []
        value = data.get("value", "")
        value = float(value)
        if len(x) != len(y):
            raise KeyboardInterrupt
        print(x)
        print(y)
        print(value)
        calculator = Int.Interpolation(len(x), x, y)
        values.append(calculator.lagrange(value))
        values.append(calculator.newton(value))
        
        calculator.difference_table()
        values.append(calculator.gauss(value, h))
        values.append(calculator.sterling(value, h))
        values.append(calculator.bessel(value, h))
        
        answer = {"values": values, "defy": calculator.defy, "data_points": [[x[i], y[i]] for i in range(len(x))],}
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные")), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400    

@app.route("/lab5/file", methods=["POST"])
def solve_interpolation_file():  
    try:
        data = request.get_json()
        x = []
        y = []
        num = data.get("num", 0)
        if num<1 or num >3:
            raise ValueError("Error: unknown number of file")
        
        f = open(f"lab5/input{num}.txt", "r", encoding="utf-8")
        x_values = f.readline().replace(",", ".").strip().split()
        x.extend(map(float, x_values))
        y_values = f.readline().replace(",", ".").strip().split()
        y.extend(map(float, y_values))
        
        values = []
        value = data.get("value", "")
        value = float(value)
        if len(x) != len(y):
            raise KeyboardInterrupt
        print(x)
        print(y)
        print(value)
        calculator = Int.Interpolation(len(x), x, y)
        values.append(calculator.lagrange(value))
        
        values.append(calculator.newton(value))
        
        h = x[1] - x[0]
        calculator.difference_table()
        values.append(calculator.gauss(value, h))
        values.append(calculator.sterling(value, h))
        values.append(calculator.bessel(value, h))
        
        answer = {"values": values, "defy": calculator.defy, "data_points": [[x[i], y[i]] for i in range(len(x))],}
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные x и y")), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400    
    except:
        return jsonify(
            error="Не получилось загрузить данные из файла!\nПроверьте валидность данных"
        ), 400    
        
@app.route("/lab5/app", methods=["POST"])
def solve_interpolation():
    try:
        data = request.get_json()
        x = data.get("x", [])
        y = data.get("y", [])
        values = []
        value = data.get("value", "")
        value = float(value)
        if len(x) != len(y):
            raise KeyboardInterrupt
        
        print(x)
        print(y)
        print(value)
        calculator = Int.Interpolation(len(x), x, y)
        
        
        values.append(calculator.lagrange(value))
        
        values.append(calculator.newton(value))
        
        h = x[1] - x[0]
        calculator.difference_table()
        values.append(calculator.gauss(value, h))
        values.append(calculator.sterling(value, h))
        values.append(calculator.bessel(value, h))
        
        answer = {"values": values, "defy": calculator.defy, "data_points": [[x[i], y[i]] for i in range(len(x))] }
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные x и y")), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400

@app.route("/lab4/app", methods=["POST"])
def solve_approximation():
    try:
        data = request.get_json()
        x = data.get("x", [])
        y = data.get("y", [])

        if len(x) != len(y):
            raise KeyboardInterrupt
        print(x)
        print(y)
        function, m = Approximation.find_best_function(len(x), x, y)
        calculator = Approximation.ApproximationCalculator(function, x, y, [], m)
        coefficients = calculator.calculate_coefficients()
        phi_values = calculator.get_phi_values()
        epsilon_values = calculator.get_epsilon_values()
        err, pearson_coefficient = calculator.calculate_pearson_correlation()
        if not err:
            return jsonify(error=str(pearson_coefficient)), 400
        answer = {
            "coefficients": list(coefficients),
            "function": str(int(function) + m - 2),
            "standard_deviation": calculator.calculate_standard_deviation(),
            "pearson_correlation": pearson_coefficient,
            "differences": list(calculator.calculate_differences()),
            "phi_values": list(phi_values),
            "epsilon_values": list(epsilon_values),
            "data_points": [[x[i], y[i]] for i in range(len(x))],
            "func": calculator.print_function(),
        }
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные x и y")), 400
    except ValueError as e:
        return jsonify(error=str(e)), 400


@app.route("/lab4/download", methods=["POST"])
def download_file():
    try:
        data = request.get_json()
        new_file = open("output.txt", "w+", encoding="utf-8")
        json.dump(data, new_file, indent=4)
        new_file.close()
        answer = {"success": "Данные успешно загружены в файл"}
        return jsonify(answer)
    except:
        return jsonify(error=str("Ошибка загрузки данных в файл")), 400


@app.route("/lab4/file", methods=["GET"])
def solve_approximation_file():
    try:
        x = []
        y = []
        f = open("input.txt", "r", encoding="utf-8")
        x_values = f.readline().replace(",", ".").strip().split()
        x.extend(map(float, x_values))
        y_values = f.readline().replace(",", ".").strip().split()
        y.extend(map(float, y_values))
        if len(x) != len(y):
            raise KeyboardInterrupt
        print(x)
        print(y)
        function, m = Approximation.find_best_function(len(x), x, y)
        calculator = Approximation.ApproximationCalculator(function, x, y, [], m)
        coefficients = calculator.calculate_coefficients()
        phi_values = calculator.get_phi_values()
        epsilon_values = calculator.get_epsilon_values()
        err, pearson_coefficient = calculator.calculate_pearson_correlation()
        if not err:
            return jsonify(error=str(pearson_coefficient)), 400
        answer = {
            "coefficients": list(coefficients),
            "function": str(int(function) + m - 2),
            "standard_deviation": calculator.calculate_standard_deviation(),
            "pearson_correlation": pearson_coefficient,
            "differences": list(calculator.calculate_differences()),
            "phi_values": list(phi_values),
            "epsilon_values": list(epsilon_values),
            "data_points": [[x[i], y[i]] for i in range(len(x))],
            "func": calculator.print_function(),
        }
        return jsonify(answer)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные x и y")), 400
    except:
        return jsonify(
            error="Не получилось загрузить данные из файла!\nПроверьте валидность данных"
        ), 400


if __name__ == "__main__":
    app.run()
