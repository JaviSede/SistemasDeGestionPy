# Crear un array en el que todos los elementos son multiplicaciones de ese elemento
array = [x for x in range(11)]

# Tablas de multiplicar

tablas = [[x*y for y in range(11)] for x in range(1, 11)]

array = [x for x in range(1, 10)]

new_array = [x+10 for x in array]
print(new_array)