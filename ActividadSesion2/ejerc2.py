lista = (20, 9, 10, 17, 6, 12)

def evaluar_valores(x):
    filtrado = filter(lambda x: x > 10, lista)
    sumar_cinco = map(lambda x:x+5, filtrado)
    return sumar_cinco

print(list(evaluar_valores(lista)))