# validar :: str --> bool
# función que recibe una patente y retorna True o False dependiendo de si cumple con la norma
# validar("HJKL25") == True


def validar(patente):
        caracteres = "BCDFGHJKLMNPRSTVWXYZ"
        numeros = "0123456789"
        patente = patente.upper()
        for letra in patente[0:4]:
                if letra not in caracteres:
                        return False
        for numero in patente[4:6]:
                if numero not in numeros:
                        return False
        return True

assert validar("HJKL25") == True
assert validar("HJOL25") == False
assert validar("HJÑL25") == False
assert validar("KJQL25") == False
assert validar("GHBWRT") == False
assert validar("HJKLG25") == False
assert validar("3HJKLF") == False
