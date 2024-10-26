string = "numero 1"

def transformar_texto(x):
    def agregar_exclamacion(x):
        x = x + "!"
        return x
    return agregar_exclamacion(x)

print(transformar_texto(string))