# str, str ---> str
# funcion que dada un mensaje y una clave, entrega un mensaje cifrado
# Ej: cifrar("hola!","sur") --> "elis!"

def cifrar(mensaje,clave):
        abc = "abcdefghijklmnopqrstuvwxyz"
        abcMod = abc
        for letra in clave:
                abcMod = abcMod.replace(letra,"")
        abcMod = clave + abcMod
                
        mensajeNuevo = ""

        for letra in mensaje:
                if letra in abc:
                        indice = abc.find(letra)
                        letraNueva = abcMod[indice]
                        mensajeNuevo = mensajeNuevo + letraNueva
                else:
                        mensajeNuevo = mensajeNuevo + letra
        return mensajeNuevo
        

assert cifrar("hola!","sur") == "elis!"
assert cifrar("camilo","z") == "bzlhkn"


