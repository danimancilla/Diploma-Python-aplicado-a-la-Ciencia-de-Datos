# edad_perro :: int -> float
# la función calcula la edad de un perro en años humanos siguiendo la fórmula
# Edad humana equivalente = 16 x ln(edad cronológica del perro) + 31
# Ej: edad_perro(1) -> 31

import math

def edad_perro(N):
        edad_humana = 16 * math.log(N)+ 31
        return edad_humana

assert edad_perro(1) == 31
assert edad_perro(3) == 16 * math.log(3)+31


cantidad = int(input("Cuántos perros tiene? "))
i = 1
edades = []
while i < cantidad+1:
        edad = int(input("Qué edad tiene el perro " + str(i) + "? "))
        edades.append(edad)
        i += 1

if cantidad > 1:
        print("Las edades de sus perros en años humanos son: ")
else:
        print("La edad de su perro en años humanos es: ")

print(list(map(lambda x: edad_perro(x) , edades)))





