def dias(month,year):
    if month==1 or month ==3 or month==5 or month==7 or month==8 or  month==10 or  month==12:
        return 31
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    else:
        if (year%4==0 and year%100!=0) or year%400==0:
            return 29
        else:
            return 28

month=int(input("Ingrese un mes (como número): "))
year=int(input("Ingrese un año (como número): "))
cantidad=dias(month,year)
print("La cantidad de días que hay en el mes es: " + str(cantidad))
