#Los nombres de candidatos para una elección están guardados en una lista:
#Ej: candidatos = [“Gabriela”, “Jose”, “Rosa”, “Matías”]
#Escriba un programa que lea por teclado los votos que obtuvo cada candidato/a, y muestre en
#pantalla los resultados de la elección en orden descendiente de porcentaje de votos.

candidatos = ["Gabriela", "José", "Rosa", "Matías"]

print("Ingresar votos obtenidos por cada candidato/a:")

d = {}
total = 0
for elemento in candidatos:
        d[elemento] = int(input(elemento + "? "))
        total += d[elemento]

T = []
for elemento in d:
        porcentaje = d[elemento]*100/total
        T.append([porcentaje,elemento])
        T.sort(reverse=True)
        
print(" ")
print("Resultados ordenados (en porcentaje):")
for elemento in T:
        print (elemento[1]+ " " + str(elemento[0]) + "%")
