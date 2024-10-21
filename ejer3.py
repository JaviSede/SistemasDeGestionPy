a = [1,2,3]
i = 2
f = 2.4
b = True
s = "cadena"
c = {1, "set", "hola", 2}
h = {"uno": 1, "dos": 2, "tres": 3}
tu = (1, 2, 3, 4, "si")

# Se puede concatenar solo con otros array, no con cadenas
# print(a + s)

# No se puede sumar un booleano con una cadena de texto
# print(b + s)

# Como los booleanos tambien pueden ser representados con 0 y 1, es capaz de hacer la suma.
print(b + i)

# Se pueden hacer sumas de numeros enteros y flotantes
print(i + f)
print(f + i)

# Solo se pueden concatenar con otros arrays, no con enteros
# print(a + i)

# Se pueden concatenar arrays
print(a + a)

# Se escribe i veces la cadena s, por lo que concatena en funcion del numero por el que se multiplica
print(i * s)

# No se puede operar entre diccionarios y colecciones ya que no son listas compatibles
# print(h - c)
#t = None
#t = t + a
#print(t)

print(c.intersection(c))
print(a.intersection(c))