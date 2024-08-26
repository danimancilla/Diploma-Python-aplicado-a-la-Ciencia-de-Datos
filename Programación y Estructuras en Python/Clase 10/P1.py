# archivo --> list[int]
# la función sumaLineas suma los enteros de cada línea y los guarda en una lista
# Ej. sumaLineas("datos.txt") -> [155,78,98,78,151]


def sumaLineas(nombre_archivo):
    archivo=open(nombre_archivo, "r")
    valores = []
    for linea in archivo:
        lista=linea.split(" ")
        suma=0
        for valor in lista:
            suma += int(valor)
        valores.append(suma)
    return valores



# archivo --> list[int]
# la función sumaColumnas suma los enteros de cada columna y los guarda en una lista
# Ej. sumaLineas("datos.txt") -> [172,64,324]

def sumaColumnas(nombre_archivo):
    archivo=open(nombre_archivo, "r")
    valores = [0,0,0]
    for linea in archivo:
        lista=linea.split(" ")
        valores[0] += int(lista[0])
        valores[1] += int(lista[1])
        valores[2] += int(lista[2])
    return valores
                 
