MAXIMO = 20

def desconto_valido(percentual):
    if percentual <= 0:
        return False
    return percentual <= MAXIMO
