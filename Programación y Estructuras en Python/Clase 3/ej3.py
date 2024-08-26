def write(date):
    day=date//10**6
    date=date%10**6
    month=date//10**4
    year=date%10**4
    if month==1:
        month="enero"
    elif month ==2:
        month="febrero"
    elif month ==3:
        month="marzo"
    elif month ==4:
        month="abril"
    elif month ==5:
        month="mayo"
    elif month ==6:
        month="junio"
    elif month ==7:
        month="julio"
    elif month ==8:
        month="agosto"
    elif month ==9:
        month="septiembre"
    elif month ==10:
        month="octubre"
    elif month ==11:
        month="noviembre"
    else:
        month="diciembre"
    print(str(day)+ " de " + month + " de " + str(year))

date=int(input("Entregue una fecha en formato DDMMAAAA: "))
write(date)
