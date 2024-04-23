from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import numpy as np
import lab4.Approximation as Approximation
import lab5.Interpolation as Int

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})



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
        
        answer = {"values": values, "defy": calculator.defy, "data_points": [[x[i], y[i]] for i in range(len(x))],}
        return jsonify(answer)
    except KeyboardInterrupt:
        return jsonify(error=str("Поступили неправильные данные x и y")), 400
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
        
        answer = {"values": values, "defy": calculator.defy}
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
