# menores :: [int] int -> [int]
# la función recibe una lista y un valor, y devuelve una lista con los elementos menores al valor
# Ej: menores([1,2,3,5,7],4) -> T =[1,2,3]

def menores(L,valor):
        T = []
        for elemento in L:
                if elemento < valor:
                        T.append(elemento)
        return T

assert menores([1,2,3,5,7],4) == [1,2,3]
assert menores([1,2,3,5,7],0) == []
assert menores([1,2,3,5,7],10) == [1,2,3,5,7]


# listaMenores ::[int] -> [int] 
# la función recibe una lista y devuelve una lista con la cantidad de elementos menores a cada elemento de la lista
# Ej: listaMenores([50,30,70,20] -> [2,1,3,0]

def listaMenores(L):
        T = []
        for elemento in L:
                largo = len(menores(L,elemento))
                T.append(largo)
        return T

assert listaMenores([50,30,70,20]) == [2,1,3,0]
assert listaMenores([20,20,20,20]) == [0,0,0,0]


# listaOrdenada  :: [int] -> [int]
# la función recibe una lista con elementos distintos y devuelve otra lista con los elementos ordenados
# Ej: listaOrdenada([50,30,70,20]) -> [20,30,50,70]

def listaOrdenada(L):
        T = []
        P = listaMenores(L)
        i = 0
        while i < len(P):
                indice = P.index(i)
                T.append(L[indice])
                i += 1 
        return T

assert listaOrdenada([50,30,70,20]) == [20,30,50,70]
assert listaOrdenada([20,-10,0,4]) == [-10,0,4,20]














