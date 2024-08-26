# funcion :: str,str,dict --> int
# función devuelve la cantidad de paises en comun que dos personas han visitado en común
# Ej: paisesEnComun("Pepito", "Yayita", paises) -> 1


paises = {
 'Pepito': ['Chile', 'Argentina'],
 'Yayita': ['Francia', 'Suiza', 'Chile'],
 'Juan': ['Chile', 'Italia', 'Francia', 'Peru']
}


def paisesEnComun (p1,p2,diccionario):
    paises1=diccionario[p1]
    paises2=diccionario[p2]

    contador = 0
    for pais1 in paises1:  
        for pais2 in paises2:
            if pais1 == pais2:
                contador=contador+1
    return contador
    
assert paisesEnComun("Pepito", "Yayita", paises)==1
assert paisesEnComun("Juan", "Yayita", paises)==2
