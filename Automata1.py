def automata(data):
    print(data)
    entrada = data['automata']
    print(entrada,"HOLA")
    especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
                '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"',
                ',', '<', '.', '>', '/', '?', '`', '~']
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digitos=["1","2","3","4","5","6","7","8","9"]
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def buscarValorEsperado(fila):
        for i, j in enumerate(matriz[fila]):
            if j != "q2":
                if i == 0:
                    return "una mayúscula"
                if i == 1:
                    return "un dígito"
                if i == 3:
                    return "un guion"

    matriz=[
            
        ["q2","q1","q1","q1","q1"],
        ["q1","q1","q1","q1","q1"],
        ["q3","q1","q1","q1","q1"],
        ["q4","q1","q1","q1","q1"],
        ["q1","q1","q1","q1","q5"],
        ["q1","q6","q1","q1","q1"],
        ["q1","q7","q1","q1","q1"],
        ["q1","q8","q1","q1","q1"],
        ["q1","q9","q1","q1","q1"],
        ["q1","q1","q1","q1","q10"],
        ["q11","q1","q1","q1","q1"],
        ["q1","q1","q1","q1","q1"],
            ]
    final="q11"
    def otorgarColumna(caracter):
        if caracter in mayusculas:
            return 0
        if caracter in digitos:
            return 1
        if caracter in especiales:
            return 2
        if caracter in minusculas:
            return 3
        if caracter =='-':
            return 4
    fila=0
    def obtenerFila(estado):
        return int(estado[1:])
    for i,n in enumerate(entrada):
        columna=otorgarColumna(n)
        estado=matriz[fila][columna]
        if estado == "q1":
            valor = buscarValorEsperado(fila)
            error = f"Ingresó '{n}' en vez de {valor} en la posición {i+1}"
            print(error)
            return {"valida": False, "mensaje": "La placa no es válida", "error": error}
        fila=obtenerFila(estado)
        # print(fila," ",columna," ",estado," ",n)
    if estado == final:
        return {"valida": True, "mensaje": "La placa es válida"}
    else:
        return {"valida": False, "mensaje": "La placa no es válida", "error": "Formato incompleto"}
