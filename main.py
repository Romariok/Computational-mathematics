from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})


@app.route('/lab4/app',methods=['POST'])
def solve_integral():
    try:
        data = request.get_json()
        a = data.get("a",0)
        b =data.get("b",0)
        equathion = data.get("eq", "")
        method = data.get("m", "")
        eps = data.get("e", "")
        integral = Int.Integrals(a,b,equathion,method,eps)
        answer = integral.solve()
        return jsonify(answer.__dict__)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except:
        return jsonify(error="An error occurred"), 400

if __name__ == '__main__':
    app.run()