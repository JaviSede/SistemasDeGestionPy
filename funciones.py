def funcion(x, y):
    print(x, y)

funcion(1,2)

# Lambda
array = (1,2,3)

data_map = map(lambda x:x+2, array)
filter_data = filter((lambda x: x<=4), list(data_map))

print(list(data_map))
print(list(filter_data))
