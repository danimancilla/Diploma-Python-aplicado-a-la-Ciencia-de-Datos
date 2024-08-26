#archivo-->int
#Entrega cuantos cartones fueron jugados (cuenta las líneas de un archivo)


def jugados (archivo):
    archivo=open(archivo,"r")
    contador=0
    for elemento in archivo:
        contador=contador+1   
    return contador

#archivo-->int
#Entrega De todos los cartones jugados, cuántos escogieron el número 7

def contar7(archivo):
    archivo=open(archivo,"r")
    lista = []
    cartones=0
    for elemento in archivo:
        lista=elemento[:-1].split(" ")
        cuenta=lista.count("7")
        if cuenta !=0:
            cartones += 1
    return cartones

#archivo, lista[int]--> bool
#Dada una lista con los números elegidos del sorteo, determinar si hubo o no ganadores
        
def ganadores (archivo, lista1):
    archivo=open(archivo,"r")
    lista1.sort()
    for linea in archivo:
        numeros=linea[:-1].split(" ")
        lista2=list(map(lambda x: int(x), numeros))
        lista2.sort()
        if lista1 == lista2:
            return True
    return False

# archivo, lista, int --> int
#Dada una lista con los números elegidos del sorteo y una cota N, determinar cuántos cartones
#tuvieron N aciertos en el sorteo

def Naciertos(archivo, lista1, N):
    archivo=open(archivo,"r")
    lista1.sort()
    cartones =0
    for linea in archivo:
        numeros=linea[:-1].split(" ")
        lista2=list(map(lambda x: int(x), numeros))
        lista2.sort()
        contador = 0
        for elemento1 in lista1:
            for elemento2 in lista2:
                if elemento1 == elemento2:
                    contador += +1

        if contador >= N:
            cartones += 1
            
    return cartones



