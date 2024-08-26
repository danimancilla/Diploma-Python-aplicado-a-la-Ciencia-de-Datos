# funcion :: string -> lista
# recibe un string y crea una lista con los carácteres
# ejemplo crearLista("abracadabra") -> L = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'].

def crearLista(palabra):
    L=[]                                # creamos una lista vacía
    for elemento in palabra:
        L.append(elemento)
    return L
    
assert crearLista("abracadabra") == ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']


# funcion :: lista, caracter --> int
# cuenta la cantidad de veces que se repite un carácter dentro de la lista.
# Ej: contarLetras(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'],'a') devuelve 5

def contarLetras(L,x):
    contador=0
    for elemento in L:
        if elemento == x:
            contador +=1
    return contador

assert contarLetras(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'],'a') == 5
assert contarLetras(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'],'h') == 0

# funcion :: lista  --> lista
# dada una lista de carácteres entrega una nueva lista con los elementos invertidos
# Ej: invertir["p","e","r","r","o"] entrega ["o", "r", "r", "e", "p"]

def invertir(L):
    largo=len(L)
    nueva_L=[]
    i=largo-1
    while i>-1:
        nueva_L.append(L[i])
        i = i-1
    return nueva_L

assert invertir(["p","e","r","r","o"]) == ["o", "r", "r", "e", "p"]


# funcion :: lista  --> lista
# recibe una lista de carácteres y retorna la misma lista sin repetidos
# Ej: sinRepeticiones(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'])
# entrega ['a','b','r','c','d']

def sinRepeticiones(L):
    nueva_L=[]
    for elemento in L:
        if elemento in nueva_L:
            nueva_L=nueva_L # no hago nada
        else:
            nueva_L.append(elemento) # le agregamos el elemento a la lista            
    return nueva_L
            
assert sinRepeticiones(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']) == ['a','b','r','c','d']


# funcion :: lista, lista  --> lista
# recibe dos listas de carácteres retorna una nueva lista con los valores concatenados uno por uno
# Ej: mezclarListas(L1,L2) entrega ["ac", "ba", "r_", "a_"]
# donde L1 = ['a','b','r','a'] y L2 = ['c','a']

def mezclarListas(L1,L2):
    largo1=len(L1)
    largo2=len(L2)
    minimo=min(largo1,largo2)
    nueva_L=[]
    i=0
    while i<=minimo-1:
        nueva_L.append(L1[i]+L2[i])
        i += 1

        
    if largo1>largo2:
        while i<=largo1-1:
            nueva_L.append(L1[i]+"_")
            i += 1
    elif largo2>largo1:
        while i<=largo2-1:
            nueva_L.append("_"+L2[i])
            i += 1
    return nueva_L

assert mezclarListas(['a','b','r','a'], ['c','a']) == ["ac", "ba", "r_", "a_"]





















