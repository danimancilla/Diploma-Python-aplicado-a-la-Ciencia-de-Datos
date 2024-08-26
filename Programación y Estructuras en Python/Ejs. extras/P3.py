"""Hoy le ha llegado el estado de cuenta de su tarjeta de crédito.
Como tiene dudas sobre el cálculo, usted traspasa todos los cobros y
abonos a una lista de Python, en donde los cargos son representados
por un número positivo y los abonos con un número negativo. Usando la
función reduce,
escriba un programa que permita obtener el balance total de su tarjeta.
"""

import functools
transacciones = []

abonos= int(input("Cuántos abonos recibió? "))
i=1
while i < abonos + 1:
        abono=int(input("Ingrese abono " +  str(i) + ": "))
        transacciones.append(abono)
        i += 1


cargos= int(input("Cuántos cargos recibió? "))
i=1
while i < cargos + 1:
        cargo=int(input("Ingrese cargo " +  str(i) + ": "))
        transacciones.append(-cargo)
        i += 1
        

balance_total=functools.reduce(lambda x,y: x+y, transacciones, 0)
print(balance_total)
