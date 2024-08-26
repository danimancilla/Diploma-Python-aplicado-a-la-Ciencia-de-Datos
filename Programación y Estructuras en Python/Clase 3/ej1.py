#programa que simula el comportamiento de un cajero automático

def billetes(monto, valor):
    cantidad = monto//valor
    print("Le corresponden " + str(cantidad) + " billetes de " +str(valor))
    return monto%valor

monto=int(input("Ingrese el monto que necesita: "))

if monto//20000>0:
    monto=billetes(monto,20000)
if monto//10000>0:
    monto=billetes(monto,10000)
if monto//5000>0:
    monto=billetes(monto,5000)
if monto//2000>0:
    monto=billetes(monto,2000)
if monto//1000>0:
    monto=billetes(monto,1000)

