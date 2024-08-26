#Integrantes: Daniela Mancilla, Gabriela Martinez, Francisca Quijada
"""Siguiendo la receta de diseño, escriba la función obtenerDominios(correos), tal que dada una 
lista de correos electrónicos, retorne la lista de todos los dominios, sin repetir y en orden alfabético.
"""

# list(str)-->list(str)
# La funcion retorna la lista de todos los dominios sin repetir y en orden alfabeticos
# Ej: obtenerDominios(["hola@gmail.com", "ol@gmail.com","h@hola.cl"]) entrega ['gmail.com', 'hola.cl']

def obtenerDominios(correos):
    lista=[]
    listadominio=[]
    for elemento in correos:
        dominio = elemento.split("@")
        lista.append(dominio[1])
    for elemento in lista:
        if elemento not in listadominio:
            listadominio.append(elemento)
    listadominio.sort()
    return listadominio
        
assert obtenerDominios(["usuario@dcc.uchile.cl"])==["dcc.uchile.cl"]
assert obtenerDominios(["hola@gmail.com", "ol@gmail.com","h@hola.cl", "hola3@gmail.com","hola3@dcc.com"])==['dcc.com', 'gmail.com', 'hola.cl']

"""
Siguiendo la receta de diseño, escriba la función contarTLD(correos), tal que dada una lista de 
correos electrónicos, retorne un diccionario que asocie a cada TLD la cantidad de veces que aparece."""

#list(str)-->dict(str:int)
#La función recibe una lista y retorna un diccionario con TLD y la cantidad de veces que aparecen.
#Ej: contarTLD(["hola@gmail.com", "ol@gmail.com","h@hola.cl"]) entrega {"com":2, "cl":1}

def contarTLD(correos):
    diccionario={}
    for elemento in correos:
        indice=elemento.rfind(".")
        tld=elemento[indice+1:]
        if tld in diccionario:
            diccionario[tld] +=1
        else:
            diccionario[tld] =1
    return diccionario

assert contarTLD(["hola@gmail.com", "ol@gmail.com","h@hola.cl"])=={"com":2, "cl":1}
assert contarTLD(["hola@gmail.com", "ol@gmail.com","ol@gmail.com"])=={"com":3}
assert contarTLD(["h.ola@gmail.com", "ol@gmail.com","ol@gmail..com"])=={"com":3}
