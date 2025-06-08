
especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
              '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"',
              ',', '<', '.', '>', '/', '?', '`', '~']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digitos=["1","2","3","4","5","6","7","8","9"]
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guion="-"
matriz=[
    [["q1"], ["q2","Se ingreso un digito y se esperaba una mayuscula"], ["q2","Se ingreso un caracter especial y se esperaba una mayuscula"], ["q2","Se ingreso un - y se esperaba una mayuscula"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q3"], ["q2","Se ingreso un digito y se esperaba una mayuscula"], ["q2","Se ingreso un caracter especial y se esperaba una mayuscula"], ["q2","Se ingreso un - y se esperaba una mayuscula"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q2","Ingreso un digito y no es valida"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y se esperaba un -"], ["q2","Ingreso un digito y se esperaba un -"], ["q2","Ingreso un caracter especial y se esperaba un -"], ["q4"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y se esperaba un digito"], ["q5"], ["q2","Ingreso un caracter especial y se esperaba un digito"], ["q2","Ingreso un - y se esperaba un digito"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q6"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q7"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q8"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q2","Ingreso un digito y no es valida"], ["q2","Ingreso un caracter especial y no es valida"], ["q9"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q10"], ["q2","Ingreso un digito y no es valida"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q11"], ["q2","Ingreso un digito y no es valida"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q12"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
    [["q2","Ingreso una mayuscula y no es valida"], ["q2","Ingreso un digito y no es valida"], ["q2","Ingreso un caracter especial y no es valida"], ["q2","Ingreso un - y no es valida"], ["q2","Ingreso una minuscula y no es valida"]],
]
def obtenerFila(estado):
    return int(estado[1:])
final="q12"
def otorgarColumna(caracter):
    if caracter in mayusculas:
        return 0
    if caracter in digitos:
        return 1
    if caracter in especiales:
        return 2
    if caracter == guion:
        return 3
    if caracter in minusculas:
        return 4
entrada="BB-3472-XY2"
fila=0
for n in entrada:
    columna=otorgarColumna(n)
    print(columna,fila)
    estado=matriz[fila][columna][0]
    print(fila," ",columna," ",estado," ",n)
    if estado =="q2":
        print(matriz[fila][columna][1])
        break
    fila=obtenerFila(estado)
if estado==final:
    print("La clave es valida")
else:
    print("La clave no es valida")
    