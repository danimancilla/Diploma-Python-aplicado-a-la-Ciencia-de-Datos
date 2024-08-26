# costo :: str--> int
# entrega valor de mensaje enviado (letra 10, digito 20, caracter especial 30)
# Ej: costo ("hola tengo 2 perros!") == 200

def costo (mensaje):
    mensaje=mensaje.replace(" ","")
    costo=0
    for c in mensaje:
        if c.isalpha():
            costo += 10
        elif c.isdigit():
            costo += 20
        else:
            costo += 30
    return costo

assert costo("hola tengo 2 perros!")==200
assert costo("!!.?")==120
assert costo("911")==60

