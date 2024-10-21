tareas = []

for i in range(1, 6):
    tarea = f"Tarea {i}"
    tareas.append(tarea)

tareas.pop(0)
tareas.pop(1)

print(tareas[-1] if tareas else "No hay tareas")
print(tareas[1:])
print(tareas[:-2])
print(tareas[::2])
print(tareas[2:4])
print(tareas[::-1])
print(len(tareas))