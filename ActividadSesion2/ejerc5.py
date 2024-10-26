lista = (range(1, 11))

impares = [x for x in lista if x % 2 != 0]
print(list(impares))

cuadrados = {num: num ** 2 for num in range(1, 11)}
print(cuadrados)

unicos = {x for x in "Pythonista"}
print(list(unicos))

