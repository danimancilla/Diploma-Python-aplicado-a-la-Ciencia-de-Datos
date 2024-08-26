#Integrantes: Daniela Mancilla, Gabriela Martinez, Francisca Quijada

#cambiamos mayúsculas a minúsculas,quitamos carácteres especiales y sacamos tildes
archivo=open("donQuijote.txt","r")
archivonuevo=open("donQuijote2.txt","w")

for linea in archivo:
    if linea != "\n":
        linea=linea.lower()
        linea=linea.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
        for letra in linea:
            if letra.isalpha() or letra==" ":
                archivonuevo.write(letra)
        archivonuevo.write(" ")
        
archivo.close()
archivonuevo.close()


#abrimos el archivo nuevo
archivonuevo=open("donQuijote2.txt","r")
diccionario={}
for linea in archivonuevo:
    #quedan dobles espacios de "capitulo 1: " los debemos sacar
    linea2=linea.replace("  ", " ")
    lista=linea2[:-1].split(" ")
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

######
#más frecuentes

lista=[]
for elemento in diccionario:
    lista.append([diccionario[elemento], elemento])
lista.sort(reverse=True)

#ordenamos alfabéticamente
i=0
listaletra=[]
while i<10:
    listaletra.append([lista[i][1],lista[i][0]])
    i += 1
listaletra.sort()

print("Las 10 palabras más frecuentes, junto a su frecuencia, ordenadas alfabéticamente")
i=0
while i<10:
    print(listaletra[i][0]+": "+str(listaletra[i][1]))
    i += 1
print("\n") 

######
#ordenamos por frecuencia
print("Las 10 palabras más frecuentes, junto a su frecuencia, ordenadas por frecuencia: ")
i=0
while i<10:
    print(lista[i][1]+": "+ str(lista[i][0]))
    i += 1

print("\n")
####
#menos frecuentes
lista=[]
for elemento in diccionario:
    lista.append([diccionario[elemento], elemento])
lista.sort()


#ordenamos alfabéticamente
i=0
listaletra=[]
while i<10:
    listaletra.append([lista[i][1],lista[i][0]])
    i += 1
listaletra.sort()

print("Las 10 palabras menos frecuentes, junto a su frecuencia, ordenadas alfabéticamente: ")
i=0
while i<10:
    print(listaletra[i][0]+": "+str(listaletra[i][1]))
    i += 1
print("\n") 

#buscaremos las palabras que tengan un caracter y los imprimiremos por orden de aparición
print("Las 10 palabras menos frecuentes, junto a su frecuencia, ordenadas por frecuencia: ")
i=0
for elemento in diccionario:
    if diccionario[elemento]==1 and i<10:
        print(elemento+": 1")
        i += 1

######
print("\n")
    
lista=[]
for elemento in diccionario:
    lista.append([diccionario[elemento], elemento])
print("La cantidad total de palabras distintas: ")
print(len(lista))
print("\n")

######
lista=[]
for elemento in diccionario:
    if len(elemento)>=4:
        lista.append([diccionario[elemento], elemento])
print("La cantidad total de palabras distintas, con al menos 4 caracteres: ")
print(len(lista))

archivonuevo.close()
    
    

