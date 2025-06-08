from flask import Flask, render_template, request, jsonify
from BackTracking import resolve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resolver", methods=["POST"])
def resolver():
    datos = request.get_json()
    print(datos)
    matriz  = resolve(datos) 
    # print(matriz )# función que devuelve pasos del backtracking
    return jsonify(matriz)

if __name__ == "__main__":
    app.run(debug=True)
