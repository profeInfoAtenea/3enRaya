sol1 = [[' ','O', ' '],[' ',' ','O'],['X','X',' ']]

sol2 = [[0,1,0],[0,0,1],[2,2,0]]

def imprime(matriz):
    print("----------------")
    print("| ", matriz[0][0] , "|", matriz[0][1], "|" , matriz[0][2] , " | ")
    print("----------------")
    print("| ", matriz[1][0] , "|", matriz[1][1], "|" , matriz[1][2] , " | ")
    print("----------------")
    print("| ", matriz[2][0] , "|", matriz[2][1], "|" , matriz[2][2] , " | ")
    print("----------------")

imprime(sol2)

def hayFicha(estado_actual, pos_fila, pos_columna):
    return estado_actual[pos_fila][pos_columna] == 1 or estado_actual[pos_fila][pos_columna] == 2

print(hayFicha(sol2, 0,1)) # 1 --> True
print(hayFicha(sol2, 2,1)) # 2 --> True
print(hayFicha(sol2, 2,2)) # 0 --> False

def ponerFicha(estado_actual,  pos_fila, pos_columna, ficha):
    estado_actual[pos_fila][pos_columna] = ficha

def introducirFicha(estado_actual,  pos_fila, pos_columna, ficha):
    if(not hayFicha(estado_actual, pos_fila, pos_columna)):
        ponerFicha(estado_actual,  pos_fila, pos_columna, ficha)
        print("OK")
    else:
        print("Lo sentimos, hay una ficha prueba con otra posición")


imprime(sol2)
introducirFicha(sol2, 0,1,1)
introducirFicha(sol2, 0,2,1)
imprime(sol2)

#Nuevo branch
