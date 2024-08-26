# int->str
# cambia el orden de la fecha, de DDMMAAAA a AAAAMMDD
# Ej change(03071998) -> 19980703


def change(date):
    day=date//10**6
    if day<10:
        day="0"+str(day)
    else:
        day=str(day)
    date=date%10**6
    month=date//10**4
    if month<10:
        month="0"+str(month)
    else:
        month=str(month)
    year=str(date%10**4)
    return(year + month + day)

#Tests
assert change(3071998)==str(19980703)


date=int(input("Entregue una fecha en formato DDMMAAAA: "))
new= change(date)
print("La fecha en formato AAAAMMDD es: " + new)

# int int->int
# compara dos fechas en formato DDMMAAAA y devuelve la mayor
# Ej comparar(24121988,10101654) -> 10101654

def comparar(date1,date2):
    d1=int(change(date1))
    d2=int(change(date2))
    if d1>d2:
        return str(date1)
    else:
        return str(date2)

#Tests
assert comparar(24121988,10101654) == 10101654


date1=int(input("Entregue una fecha en formato DDMMAAAA: "))
date2=int(input("Entregue otra fecha en formato DDMMAAAA: "))
mayor= comparar(date1,date2)
print("La fecha mayor es: " + mayor)
