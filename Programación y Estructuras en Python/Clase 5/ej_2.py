# digitos :: int -> int
# entrega la cantidad de digitos de un numero entero positivo
# Ej: digitos(2023) entrega 4 y digitos(1) entrega 1


def digitos(N):
    digitos=1
    while N//10 != 0:
        N=N//10
        digitos+=1
    return int(digitos)
        
assert digitos(2022) ==4
assert digitos(2) == 1


#programa que pide a el usuario digitos y al final entrega el numero que tiene
#la mayor cantidad de digitos

usuario=int(input("numero? "))
cantidad=0
numero=0
while usuario!=0:
    dig=digitos(usuario)
    if dig>cantidad:
        cantidad=dig
        numero=usuario
    usuario=int(input("numero? "))
print("El " + str(numero)+ " tiene " + str(cantidad)+ " dígitos")
