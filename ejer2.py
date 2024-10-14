diccio = {"1H": "Juan", "2F": "Pepe", "3I": "Manolo", "4H": "Maria", "5D": "Ana", "6A": "Damian", "7S": "Javier", "8Z": "Joana", "9C": "Pilar", "10X": "Carmen"}

# print(diccio.get("4"))
# diccio["7"] = "Antonio"
# print(diccio)

for key in diccio:
    if diccio.get(key) == "Ana":
        diccio.pop(key)
        diccio[11] = "Ana"

print(diccio)