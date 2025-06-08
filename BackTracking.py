import random
import copy

def resolve(datos):
    print(datos)
    if datos:
        rows = datos["matriz"]["filas"]
        columns =  datos["matriz"]["columnas"]
        start = tuple(datos["origen"])
        destination = tuple(datos["destino"])
        black_holes = [tuple(pos) for pos in datos["agujerosNegros"]]
        big_stars = [tuple(pos) for pos in datos["estrellasGigantes"]]
        wormholes = [[entrada,salida] for entrada,salida in datos["agujerosGusano"]]
        zones_charge = [ (x, y,carga) for x, y, carga in datos["zonasRecarga"] ]
    print(black_holes,big_stars,"que mas")
    def pinterMatriz(matriz):
        for fila in matriz:
            print(fila)

    matriz = [
        [[random.randint(0, 10), random.randint(0, 10)] for _ in range(columns)]
        for _ in range(rows)
    ]
    # matriz=[[[5, 3], [1, 5], [6, 4]],
    # [[4, 2], [0, 7], [6, 2]],
    # [[1, 7], [8, 6], [8, 9]]]


 
    ## Validaciones

    def is_viable(wasBigSatar,pos,actual_charge):
        return for_black_holes(wasBigSatar,pos) and for_zones_minimun_load(pos,actual_charge) and for_zones_energy(pos,actual_charge)
    def for_black_holes(wasBigSatar,pos):
        
        return False if not wasBigSatar and pos in black_holes else True #Hay que eliminar la poscicion de los agujeros negros para no tner errores
    def for_zones_minimun_load(pos,actual_charge):
        x=pos[0]
        y=pos[1]
        return False if actual_charge < matriz[x][y][1] else True
    def for_zones_energy(pos,actual_charge):
        x=pos[0]
        y=pos[1]
        return False if actual_charge-matriz[x][y][0]<0 and pos not in zones_charge  else True

    def is_wormhole_entrance(pos):
        for n in wormholes:
            if pos == n[0]:
                return True
        return False

    def return_wormhole_final(pos):
        for n in wormholes:
            if pos in n:
                return n[1]
        return -1

    def is_valid(pos):
        x=pos[0]
        y=pos[1]
        return True if x<len(matriz) and x>=0 and y<len(matriz[0])and y>=0 and matriz[x][y][0]!=-1 else False
    def action_zones(pos):
        return matriz[pos[0]][pos[1]][0]

    def check_is_zone_charge(x,y):
        for i,j,k in zones_charge:
            if i==x and j==y:
                return True 
    def return_charge(x,y):
        for i,j,k in zones_charge:
            if i==x and j==y:
                return k
            
    movements=[( 0,  1), ( 1,  0),(-1, -1), (-1,  0), (-1,  1),
    ( 0, -1), ( 0,  0),
    ( 1, -1), ( 1,  0), ( 1,  1)]
    contador=1

    def bckt(x,y,wasBigSatar,actual_charge,S,ActualWay,solutions,So):
        if is_valid((x,y)) and is_viable(wasBigSatar,(x,y),actual_charge):
            life=action_zones((x,y))
            if check_is_zone_charge(x,y):
                enhancer=return_charge(x,y)
                actual_charge*=enhancer
                matriz[x][y][0]=-1
            else:
                actual_charge-=life
                # print(matriz[x][y][0])
                matriz[x][y][0]=-1
            ActualWay.append((x,y))
            solutions.append(copy.deepcopy(matriz))
            # print(contador,matriz)
        
            if (x,y)==destination:
                
                if  ActualWay  not in S:
                    S.append(copy.deepcopy(ActualWay))
                    So.append(copy.deepcopy(solutions))
                    # print(ActualWay,"hola")
                    # for j in solutions:
                        
                    #     pinterMatriz(j)
                    #     print("\n")
                    print(S)
                    if len(S)==5:
                        print(S)
                        return True
            elif  is_wormhole_entrance([x,y]) :
                z,k=return_wormhole_final([x,y])
                if bckt(z,k,False,actual_charge,S,ActualWay,solutions,So):
                    return True
            else:
                for i,j in movements:
                    isBigStar=False if (x,y) not in big_stars else True
                    if bckt(x+i,y+j,isBigStar,actual_charge,S,ActualWay,solutions,So):
                        # print("hola")
                        return True   
            matriz[x][y][0]=life
            solutions.pop()
            ActualWay.pop()
            # pinterMatriz(matriz)
    S=[]
    bckt(start[0],start[1],False,10,S,[],[],[])
    return matriz,S
