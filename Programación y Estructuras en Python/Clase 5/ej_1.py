# primerdigito :: int -> int
# entrega el primer dígito de un número entero entregado
# Ej: primerdigito(2022) entrega 2 y primerdigito(-23) entrega 2


def primerdigito(N):
    if N<0:
        N=N*(-1)
    while N//10 != 0:
        N=N//10
    return int(N)
        
assert primerdigito(2022) ==2
assert primerdigito(-23) == 2
assert primerdigito(1) == 1
