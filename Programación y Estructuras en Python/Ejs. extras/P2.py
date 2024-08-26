#Un dígrafo es un grupo de dos letras que representan un solo sonido,
#como lo es el conjunto “ch”, “ll” o “rr”. Usando la función Filter,
#escriba un programa que obtenga todas las palabras de una lista que contengan algún dígrafo.
#Hint: Suponga que posee una lista D con todos los dígrafos en formato String: D = [“ch”, “ll”, ...., “rr”]

Digrafos = ["ch" , "ll", "gu" , "qu" , "rr"]

#creemos una lista
cantidad = int(input("Cuántas palabras quiere agregar a su lista? "))
i = 1
palabras=[]

while i  < cantidad +1 :
        palabra= input("Palabra " + str(i) + "? ")
        palabras.append(palabra)
        i += 1


#filtro las palabras que contienen cada digrafo
nueva_lista = []
for elemento in Digrafos:
        nueva_lista.append(list(filter(lambda x:  elemento in x, palabras)))


#me quedo con las palabras sin repetición (algunas palabras pueden tener más de un dígrafo)
lista_final=[]
for lista in nueva_lista:
    for palabra in lista:
            if not palabra in lista_final:
                    lista_final.append(palabra)
  
print(lista_final)
