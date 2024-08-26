#programa que permita a un conductor conocer el rendimiento de su auto
#solicita una lista de valores de kms y litros
#El fin de la lista se indica por el valor 0 kms.


kms_total=0
litros_total=0
rendimiento_1=0
rendimiento_2=0

while True:
    kms=float(input("kms? "))
    if kms==0:
        break
    litros=float(input("litros? "))
    rendimiento=kms/litros
    kms_total+=kms
    litros_total+=litros
    
    if rendimiento>=rendimiento_1 and rendimiento>=rendimiento_2:
        rendimiento_2=max(rendimiento_1,rendimiento_2)
        rendimiento_1=rendimiento
    elif rendimiento>=rendimiento_2 and rendimiento<=rendimiento_1:
        rendimiento_1=rendimiento_1
        rendimiento_2=rendimiento

    
print("resultados finales:")
print("rendimiento promedio=" + str(kms_total/litros_total))
print("mejor rendimiento: " + str(rendimiento_1))
print("2do mejor rendimiento: " + str(rendimiento_2))

