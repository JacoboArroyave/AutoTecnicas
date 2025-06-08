from flask import jsonify

def automata2(data):
    entrada = data['automata']
    print(entrada, "HOLA")
    especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"',
                ',', '<', '.', '>', '/', '?', '`', '~']
    mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digitos = list("123456789")
    minusculas = list("abcdefghijklmnopqrstuvwxyz")
    guion = "-"
    matriz = [
        ["q1", "q2", "q2", "q2", "q2"],
        ["q3", "q2", "q2", "q2", "q2"],
        ["q2", "q2", "q2", "q2", "q2"],
        ["q2", "q2", "q2", "q4", "q2"],
        ["q2", "q5", "q2", "q2", "q2"],
        ["q2", "q6", "q2", "q2", "q2"],
        ["q2", "q7", "q2", "q2", "q2"],
        ["q2", "q8", "q2", "q2", "q2"],
        ["q2", "q2", "q2", "q9", "q2"],
        ["q10", "q2", "q2", "q2", "q2"],
        ["q11", "q2", "q2", "q2", "q2"],
        ["q2", "q12", "q2", "q2", "q2"],
        ["q2", "q2", "q2", "q2", "q2"],
    ]

    def buscarValorEsperado(fila):
        for i, j in enumerate(matriz[fila]):
            if j != "q2":
                if i == 0:
                    return "una mayúscula"
                if i == 1:
                    return "un dígito"
                if i == 3:
                    return "un guion"

    def obtenerFila(estado):
        return int(estado[1:])

    def otorgarColumna(caracter):
        if caracter in mayusculas:
            return 0
        if caracter in digitos:
            return 1
        if caracter == guion:
            return 3
        if caracter in minusculas:
            return 4
        return 2

    fila = 0
    final = "q12"
    error = ""
    estado = "q0"

    for i, n in enumerate(entrada):
        columna = otorgarColumna(n)
        estado = matriz[fila][columna]
        if estado == "q2":
            valor = buscarValorEsperado(fila)
            error = f"Ingresó '{n}' en vez de {valor} en la posición {i+1}"
            print(error)
            return {"valida": False, "mensaje": "La clave no es válida", "error": error}
        fila = obtenerFila(estado)

    if estado == final:
        return {"valida": True, "mensaje": "La clave es válida"}
    else:
        return {"valida": False, "mensaje": "La clave no es válida", "error": "Formato incompleto"}
