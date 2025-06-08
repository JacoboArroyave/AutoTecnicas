from flask import Flask, render_template, request, jsonify
from BackTracking import resolve
from Automata1 import automata
from Automata2 import automata2

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
@app.route("/resolverAutomata", methods=["POST"])
def resolverAutomta():
    datos = request.get_json()
    print(datos)
    matriz  = automata(datos) 
    # print(matriz )# función que devuelve pasos del backtracking
    return jsonify(matriz)
@app.route("/clave-producto", methods=["POST"])
def resolverClaveProducto():
    datos = request.get_json()
    print(datos,"hola")
    matriz  = automata2(datos) 
    print(matriz )
    # print(matriz )# función que devuelve pasos del backtracking
    return jsonify(matriz)

if __name__ == "__main__":
    app.run(debug=True)
