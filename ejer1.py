tupla = (1, 2, 3, "h", 5, 6)
array = [1, 2, 3, 4, 5, 6, 7]

for n in tupla:
    print(n)

for n in array:
    print(n)

n = 0
while n < len(tupla):
    print(tupla[n])
    n += 1

n = 0
while n < len(array):
    print(array[n])
    n += 1
