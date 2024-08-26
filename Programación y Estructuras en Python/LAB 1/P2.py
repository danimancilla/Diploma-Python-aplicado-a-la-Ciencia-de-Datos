# Integrantes: Dusan Cotoras, Daniela Mancilla, Jenifer Villarroel
# dineroFinal :: int , float , int -> float
# calcula el dinero obtenido luego de depositar un monto con un interés anual
# considerando una cantidad de años
# Ej. dineroFinal(1000000.0, 5.0, 2) entrega 1102500.0

def dineroFinal(montoInicial, tasa, annos):
    porcentaje=1+tasa/100
    return montoInicial* porcentaje**annos

#Tests
assert abs(dineroFinal(1000000.0, 5.0, 2) - 1102500.0) <0.001
assert abs(dineroFinal(1000000.0, 5.0, 1) - 1050000.0) <0.001
assert abs(dineroFinal(0.0, 5.0, 1) -0.0) <0.001
assert abs(dineroFinal(100, 5.0, 0) -100) <0.001


#programa que determine el número mínimo de años
#que debe depositarse un monto dado para alcanzar el total deseado

monto=float(input("Dinero inicial? "))
monto_deseado=float(input("Monto deseado? "))
tasa=float(input("Tasa de interés anual? "))

monto_final=dineroFinal(monto,tasa,1)
x=1

while monto_final<monto_deseado:
    x+=1
    monto_final=dineroFinal(monto,tasa,x)

print("Resultado = " + str(monto_final)+ " en " + str(x) + " años" )
