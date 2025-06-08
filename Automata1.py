
especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
              '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"',
              ',', '<', '.', '>', '/', '?', '`', '~']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digitos=["1","2","3","4","5","6","7","8","9"]
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guion="-"

matriz=[
        
    ["q1","q1","q1","q1","q2"],
    ["q3","q1","q1","q1","q2"],
    ["q4","q1","q1","q1","q2"],
    ["q1","q1","q1","q5","q2"],
    ["q1","q6","q1","q1","q2"],
    ["q1","q7","q1","q1","q2"],
    ["q1","q8","q1","q1","q2"],
    ["q1","q9","q1","q1","q2"],
    ["q1","q","q1","q10","q2"],
    ["q11","q1","q1","q1","q2"],
    ["q1","q1","q1","q1","q2"],
        ]
final="q11"
def otorgarColumna(caracter):
    if caracter in mayusculas:
        return 0
    if caracter in digitos:
        return 1
    if caracter in especiales:
        return 2
    if caracter == guion:
        return 3
entrada="AAA-1234-Q"
fila=0
def obtenerFila(estado):
    return int(estado[1:])
for n in entrada:
    columna=otorgarColumna(n)
    estado=matriz[fila][columna]
    fila=obtenerFila(estado)
    print(fila," ",columna," ",estado," ",n)
if estado==final:
    print("La placa es valida")
else:
    print("La placa no es valida")
    