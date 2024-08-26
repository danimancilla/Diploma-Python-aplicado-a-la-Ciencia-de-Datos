# esPangrama :: str -> bool
# la función indica si el texto es o no un pangrama (contiene todas las letras del abecedario)
# Ej: esPangrama('Cada vez que trabajo, Felix me paga un whisky.') --> True

def esPangrama(texto):
    letras="abcdefghijklmnopqrstuvwxyz"
    texto = texto.lower()
    for letra in letras:
        if texto.find(letra) == -1:
            return False
    return True
    
assert esPangrama("Cada vez que trabajo, Felix me paga un whisky") == True
assert esPangrama("Cada vez que trabajo, Luis me invita a una cerveza") == False










