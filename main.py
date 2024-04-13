from flask import Flask, request, jsonify
from flask_cors import CORS
import lab4.Approximation as Approximation

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})


@app.route('/lab4/app',methods=['POST'])
def solve_integral():
    try:
        data = request.get_json()
        x = data.get("x", [])
        y = data.get("y", [])
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
        answer = {"coefficients": list(coefficients), "function": function, "standard_deviation": calculator.calculate_standard_deviation(),
                  "pearson_correlation": pearson_coefficient, "differences": list(calculator.calculate_differences()),
                  "phi_values": list(phi_values), "epsilon_values": list(epsilon_values), 
                  "data_points": [[x[i], y[i], phi_values[i], epsilon_values[i]] for i in range(len(x))]}
        return jsonify(answer)
    except ValueError as e:
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run()