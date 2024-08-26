#Integrantes: Daniela Mancilla, Gabriela Martinez, Francisca Quijada

#sonAnagramas :: str, str -> bool
#la función indica True si p1 y p2 son anagramas, y False en caso contrario.
#Ej: sonAnagramas("torpes", "postre") --> True

def sonAnagramas(p1,p2):
    lista1 = []
    lista2 = []

    p1_sinA=p1.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    p2_sinA=p2.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

    for letra in p1_sinA:
        lista1.append(letra)
    lista1.sort()
    for letra in p2_sinA:
        lista2.append(letra)
    lista2.sort()
    
    if lista1 == lista2:
        return True
    return False
    
assert sonAnagramas("raptar", "aparta") == False
assert sonAnagramas("torpes", "postre") == True
assert sonAnagramas("oso", "osa") == False


#esPanvocalica :: str -> bool
#la función indique si una palabra dada es o no panvocálica.
#Ej:esPanvocalica(centrifugado) --> True

def esPanvocalica(palabra):
    palabra_sinA=palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    vocales=["a", "e", "i", "o", "u"]
    for vocal in vocales:
        if vocal not in palabra_sinA:
            return False
    return True

assert esPanvocalica("centrifugado") == True
assert esPanvocalica("bisabuelo") == True
assert esPanvocalica("hipotenusa") == True
assert esPanvocalica("mano") == False
assert esPanvocalica("12345") == False


#tieneLetrasEnOrden :: str --> bool
#indica si las letras de la palabra dada están o no en orden alfabético
#Ej: tieneLetrasEnOrden(abenuz) --> True

def  tieneLetrasEnOrden(palabra):
    palabra_sinA=palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    i=0
    while i < len(palabra)-1:
        if palabra_sinA[i]>palabra_sinA[i+1]:
            return False
        i +=1
    return True
        
assert tieneLetrasEnOrden("abenuz") ==True
assert tieneLetrasEnOrden("himnos") ==True
assert tieneLetrasEnOrden("zapato") ==False
assert tieneLetrasEnOrden("g") == True


############

RAE=open("palabras.txt" ,"r")

palabra1=input("Palabra? ")
lista=[]
for linea in RAE:
    palabra2=linea[:-1]
    if sonAnagramas(palabra1, palabra2):
        lista.append(palabra2)

if len(lista)>0:
    print(lista)
else:
    print("No tiene anagramas")

RAE.close()

############

RAE=open("palabras.txt" ,"r")
archivo=open("panvocalicas.txt", "w")

for linea in RAE:
    palabra=linea[:-1]
    if esPanvocalica(palabra):
        archivo.write(palabra+"\n")
        
RAE.close()
archivo.close()

############

RAE=open("palabras.txt" ,"r")
archivo=open("letrasEnOrden.txt", "w")

for linea in RAE:
    palabra=linea[:-1]
    if tieneLetrasEnOrden(palabra):
        archivo.write(palabra+"\n")
        
RAE.close()
archivo.close()


