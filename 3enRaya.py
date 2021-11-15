
'''
NOTA: Usar en Shell help(<nombre-función) para ver los comentarios

## 3 en Raya

Se representa con un Matriz 3x3.

'''
estado_actual = [[0,1,0],[0,0,1],[2,2,0]]
TURNO = 1

def nuevoJuego():
    """ Inicializa una matriz 3x3 a 0 """
    global estado_actual
    global contador
    
    estado_actual =  [[0,0,0],[0,0,0],[0,0,0]]
    contador = 0
    
def imprime(matriz):
    """ Imprime por pantalla el tablero dada una matriz 3x3 """
    print("---a----b----c-----")
    print("1| ", imprimeFicha(matriz[0][0]) , "|", imprimeFicha( matriz[0][1]), "|" , imprimeFicha(matriz[0][2]) , " | ")
    print("----------------")
    print("2| ", imprimeFicha(matriz[1][0]) , "|", imprimeFicha(matriz[1][1]), "|" , imprimeFicha(matriz[1][2]) , " | ")
    print("----------------")
    print("3| ", imprimeFicha(matriz[2][0]) , "|", imprimeFicha(matriz[2][1]), "|" , imprimeFicha(matriz[2][2]) , " | ")
    print("---a----b----c-----")

def imprimeFicha(num_ficha):
    """ Imprime la ficha dado un número """
    if(num_ficha == 1):
        return 'O'
    elif(num_ficha == 2):
        return 'X'
    else:
        return ' ' 

def cambiarTurno():
    """Cambia el turno """
    global TURNO
    if(TURNO == 1):
        TURNO = 2
    else:
        TURNO = 1
        
def verTurno():
    """Devuelve el turno actual"""
    return TURNO

def hayFicha(estado_actual, pos_fila, pos_columna):
    """Comprueba si hay una ficha dada una posición"""
    return estado_actual[pos_fila][pos_columna] == 1 or estado_actual[pos_fila][pos_columna] == 2


def ponerFicha(estado_actual,  pos_fila, pos_columna, ficha):
    """Pone una ficha dada una posición"""
    estado_actual[pos_fila][pos_columna] = ficha



def esCorrectaCoordenada(coordenada):
    """Comprueba si la coordenada se encuentra en el tablero"""
    if(not coordenada in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")):
        print("No existe esa posición")
        return False
    else:
        return True
    

def obtenerPos_fila(coordenada):
    if(coordenada[1] == "1"):
        return 0
    elif(coordenada[1] == "2"):
        return 1
    elif(coordenada[1] == "3"):
        return 2
    
def obtenerPos_columna(coordenada):
    if(coordenada[0] == "a"):
        return 0
    elif(coordenada[0] == "b"):
        return 1
    elif(coordenada[0] == "c"):
        return 2
    

def pedirColocarFicha():
    """Función que pide información al usuario"""
    
    print("Es el turno de ", imprimeFicha(verTurno()))
    print("Por favor ", imprimeFicha(verTurno()) , "¿Donde coloco la ficha?")
    coordenada = input()
    casillavalida = False
    while(not casillavalida):
        if(not (esCorrectaCoordenada(coordenada))):
            print("Por favor ", imprimeFicha(verTurno()) , "¿Donde coloco la ficha?")
            coordenada = input()
            break
        
        pos_fila = obtenerPos_fila(coordenada)
        pos_columna = obtenerPos_columna(coordenada)
        
        if(not hayFicha(estado_actual, pos_fila, pos_columna)):
            ponerFicha(estado_actual,  pos_fila, pos_columna, TURNO)
            casillavalida = True
        else:
            print("Lo sentimos, ya hay una ficha")
            pedirColocarFicha()
            break

def totalFichasColocadas(estado_actual):
    """Devuelve el total de fichas colocadas"""
    contador = 0
    for fila in estado_actual:
        for elemento in fila:
            if(elemento != 0):
                contador = contador + 1
    return contador

#estado_gana_o = [[1,1,1],[0,0,1],[2,2,0]]
#estado_gana_x = [[1,1,0],[0,0,1],[2,2,2]]
#estado_empate = [[1,1,2],[2,2,1],[1,2,1]]

def ganador(estado_actual):
    if(totalFichasColocadas(estado_actual) >= 8):
        print("Ha terminado en Empate ")
        return True
    #FILAS 'O'
    elif(estado_actual[0][0] * estado_actual[0][1] * estado_actual[0][2] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    elif(estado_actual[1][0] * estado_actual[1][1] * estado_actual[1][2] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    elif(estado_actual[2][0] * estado_actual[2][1] * estado_actual[2][2] == 1):
        print("Ha ganado el jugador 'O'")
        return True
   #Columnas 'O'
    elif(estado_actual[0][0] * estado_actual[1][0] * estado_actual[2][0] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    elif(estado_actual[0][1] * estado_actual[1][1] * estado_actual[2][1] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    elif(estado_actual[0][2] * estado_actual[1][2] * estado_actual[2][2] == 1):
        print("Ha ganado el jugador 'O'")
        return True
   #Diagonales
    elif(estado_actual[0][0] * estado_actual[1][1] * estado_actual[2][2] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    elif(estado_actual[0][2] * estado_actual[1][1] * estado_actual[2][0] == 1):
        print("Ha ganado el jugador 'O'")
        return True
    
    #FILAS 'X'
    if(estado_actual[0][0] * estado_actual[0][1] * estado_actual[0][2] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    elif(estado_actual[1][0] * estado_actual[1][1] * estado_actual[1][2] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    elif(estado_actual[2][0] * estado_actual[2][1] * estado_actual[2][2] == 8):
        print("Ha ganado el jugador 'X'")
        return True
   #Columnas 'O'
    elif(estado_actual[0][0] * estado_actual[1][0] * estado_actual[2][0] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    elif(estado_actual[0][1] * estado_actual[1][1] * estado_actual[2][1] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    elif(estado_actual[0][2] * estado_actual[1][2] * estado_actual[2][2] == 8):
        print("Ha ganado el jugador 'X'")
        return True
   #Diagonales
    elif(estado_actual[0][0] * estado_actual[1][1] * estado_actual[2][2] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    elif(estado_actual[0][2] * estado_actual[1][1] * estado_actual[2][0] == 8):
        print("Ha ganado el jugador 'X'")
        return True
    
def main():
    """Programa principal"""
    nuevoJuego()
    
    while(not ganador(estado_actual)):
        imprime(estado_actual)
        pedirColocarFicha()
        cambiarTurno()
    
    imprime(estado_actual)
    
if __name__ == '__main__':
    main()

