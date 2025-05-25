import random
import copy
def pinterMatriz(matriz):
    for fila in matriz:
        print(fila)

matriz = [
    [[random.randint(0, 10), random.randint(0, 10)] for _ in range(3)]
    for _ in range(3)
]
pinterMatriz(matriz)
print("\n \n")
destination = (0, 0)
destino = (4,4)
black_holes = [(1,1),(1,2)]
big_stars = [ (0,2), (20, 20)]
agujeros_gusano = [((11, 11), (13, 13)), ((18, 5), (21, 6))]

zones_charge = [ (0,0,5), (22, 22,22)]


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



def is_valid(pos):
    x=pos[0]
    y=pos[1]
    return True if x<len(matriz) and x>=0 and y<len(matriz[0])and y>=0 and matriz[x][y][0]!=-1 else False
def action_zones(pos):
    return matriz[pos[0]][pos[1]][0]

def check_is_zone_charge(x,y):
    for i,j,k in zones_charge:
        if i==x and j==y:
            print("que mas") 
            return True 
def return_charge(x,y):
    for i,j,k in zones_charge:
        if i==x and j==y:
            return k
movements=[( 0,  1), ( 1,  0),(-1, -1), (-1,  0), (-1,  1),
 ( 0, -1), ( 0,  0),
 ( 1, -1), ( 1,  0), ( 1,  1)]
contador=1
def bckt(x,y,wasBigSatar,actual_charge,S,ActualWay):
    if is_valid((x,y)) and is_viable(wasBigSatar,(x,y),actual_charge):
        life=action_zones((x,y))
        if check_is_zone_charge(x,y):
            enhancer=return_charge(x,y)
            actual_charge*=enhancer
            print(actual_charge)
            matriz[x][y][0]=-1
        else:
            actual_charge-=life
            # print(matriz[x][y][0])
            matriz[x][y][0]=-1
        ActualWay.append(matriz)
        # print(contador,matriz)
      
        if (x,y)==(2,2):
            if   matriz  not in S:
                S.append(copy.deepcopy(matriz))
                
                pinterMatriz(matriz)
                print("\n")
        else:
            for i,j in movements:
                
                isBigStar=False if (x,y) not in big_stars else True
                bckt(x+i,y+j,isBigStar,actual_charge,S,ActualWay)
        matriz[x][y][0]=life
        # pinterMatriz(matriz)

        
bckt(0,0,False,10,[],[])
