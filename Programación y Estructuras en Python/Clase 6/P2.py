# funcion :: lista -> lista
# recibe una lista de valores (de cualquier tipo) y devuelve el conjunto que le corresponde.
# Ej: conjunto([1,2,2,1]) devuelve la lista [1,2].

def conjunto(L):
    nueva_L=[]
    for elemento in L:
        if elemento in nueva_L:
            nueva_L=nueva_L
        else:
            nueva_L.append(elemento)
    return nueva_L

assert conjunto([1,2,2,1]) == [1,2]


# funcion :: lista -> string
#dada una lista, devuelve el conjunto que la forma en tipo string.
# Ej: toString([1,2,2,1]) devuelve “{1,2}”

def toString(L):
    nueva_L = conjunto(L)
    largo=len(nueva_L)
    i=0
    string=""
    while i<largo-1:
        string=string+str(nueva_L[i])+","
        i += 1
    string="{"+string+str(nueva_L[largo-1])+"}"
    return string

assert toString([1,2,2,1]) == "{1,2}"


# funcion :: lista,lista -> lista
# dadas dos listas, devuelve el conjunto formado por
# todos los elementos que están en las listas que recibe como parámetro.
# Ej: union([1,2],[2,3]) devuelve [1,2,3].

def union(L1,L2):
    nueva_L=L1
    for elemento in L2:
        if elemento in nueva_L:
            L1=L1
        else:
            L1.append(elemento)
    return nueva_L

assert union([1,2],[2,3]) == [1,2,3]



# funcion :: lista,lista -> lista
# dadas dos listas, devuelve el conjunto formado por todos los elementos 
# que están simultáneamente en las dos listas que recibe como parámetro.
# Ej: interseccion([1,2],[2,3]) devuelve [2].

def interseccion(L1,L2):
    nueva_L=[]
    for elemento in L1:
        if elemento in L2:
            nueva_L.append(elemento)
    return nueva_L

assert interseccion([1,2],[2,3]) == [2]


# funcion :: lista,lista -> lista
# dadas dos listas, devuelve el conjunto formado por los elementos 
# que están presentes en la primera lista, pero no en la segunda
# Ej: diferencia([1,2],[2,3]) devuelve [1].


def diferencia(L1,L2):
    nueva_L=L1
    for elemento in L2:
        if elemento in L1:
            nueva_L.remove(elemento)
    return nueva_L

assert diferencia([1,2],[2,3]) == [1]

