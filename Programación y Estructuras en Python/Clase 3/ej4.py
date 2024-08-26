def cachipun(entrada):
    if entrada == "papel":
        return "tijera"
    elif entrada == "tijera":
        return "piedra"
    else:
        return "papel"

jugar=input("Juguemos al cachipún, elige piedra, papel o tijera: ")
print("Yo gano con: " + cachipun(jugar))
