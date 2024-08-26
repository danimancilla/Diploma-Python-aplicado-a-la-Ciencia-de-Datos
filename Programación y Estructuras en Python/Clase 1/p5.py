#programa que tome un número de 2 dígitos del usuario
#genera un nuevo número que resulta de invertir los dígitos del número anterior

#ingresa el usuario el número a dar vuelta
numero=int(input("¿Qué número de 2 dígitos quiere dar vuelta? "))
#calculamos el dígito de las decenas y unidades
decena=str(numero//10)
unidad=str(numero%10)
#imprimimos el resultado
print("El número dado vuelta es: " + unidad + decena)


#ahora con 3 dígitos
numero=int(input("¿Qué número de 3 dígitos quiere dar vuelta? "))
c=numero//100
d=(numero-100*c)//10
u=numero-100*c-10*d
print("El número dado vuelta es: " + str(u) + str(d) + str(c))
