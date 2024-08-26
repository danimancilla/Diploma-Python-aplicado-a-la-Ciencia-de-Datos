from P1 import verificar
from P1 import ok

# sudoku :: [[int]] -> bool
# entrega True si la solución de un sudoku está correcta, o False en caso contrario

def sudoku(T):
    #recorremos las filas
    i=0
    while i<9:
        if ok(T,i,0,i,8) == False:
            return False
        else:
            i += 1
    #recorremos las columnas
    i=0
    while i<9:
        if ok(T,0,i,8,i) == False:
            return False
        else:
            i += 1
    #recorremos las subtablas
    fila=[0,3,6]
    columna=[0,3,6]
    for i in fila:
        for j in columna:
            if ok(T,i,j,i+2,j+2) == False:
                return False
    return True
    
"""
T=[[5,3,4,6,7,8,9,1,2],
   [6,7,2,1,9,5,3,4,8],
   [1,9,8,3,4,2,5,6,7],
   [8,5,9,7,6,1,4,2,3],
   [4,2,6,8,5,3,7,9,1],
   [7,1,3,9,2,4,8,5,6],
   [9,6,1,5,3,7,2,8,4],
   [2,8,7,4,1,9,6,3,5],
   [3,4,5,2,8,6,1,7,9]]
"""
"""
T=[[5,4,3,6,7,8,9,1,2],
   [6,7,2,1,9,5,3,4,8],
   [1,9,8,3,4,2,5,6,7],
   [8,5,9,7,6,1,4,2,3],
   [4,2,6,8,5,3,7,9,1],
   [7,1,3,9,2,4,8,5,6],
   [9,6,1,5,3,7,2,8,4],
   [2,8,7,4,1,9,6,3,5],
   [3,4,5,2,8,6,1,7,9]]
   """
    
