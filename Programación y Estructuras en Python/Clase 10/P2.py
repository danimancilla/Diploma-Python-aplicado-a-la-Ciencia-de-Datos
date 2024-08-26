# archivo -> lista, lista
# funcion entrega la lista de aceptados y de rechazados


def AcepRech(archivo):
    archivo= open(archivo, "r")
    puntajes = []
    for linea in archivo:
        puntajes.append(int(linea))
    puntajes.sort()
    rechazados = puntajes[:150]
    aceptados = puntajes[150:]
    return [rechazados,aceptados]


# archivo -> int
# funcion entrega la cantidad mensual que se debe entregar en beca
        


def beca(archivo):
    archivo= open(archivo, "r")
    becados=0
    for linea in archivo:
        if int(linea) >=764:
            becados += 1
    return becados*60000


# archivo -> float
# funcion entrega puntaje promedio de los/as estudiantes aceptados/as.
        


def promedio(archivo):
    aceptados = AcepRech(archivo)[1]
    return sum(aceptados)/len(aceptados)

# archivo -> float
# funcion entrega la desviación estándar de los puntajes de los/as estudiantes
# rechazados/as.
        


def desviacion(archivo):
    rechazados = AcepRech(archivo)[0]
    N = len(rechazados)
    promedio = sum(rechazados)/N
    suma=0
    for elemento in rechazados:
        suma += (elemento-promedio)**2
    return (suma/N)**0.5







