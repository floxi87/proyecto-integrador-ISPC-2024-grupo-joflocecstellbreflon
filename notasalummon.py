#Un estudiante está cursando 5 materias, tiene la nota de cada 
#materia y quiere saber cuál es su promedio."

lista = []
nota1 = int(input("Escriba la 1 nota: "))
lista.append(nota1)
for i in range(4):
    nota = int(input(f"Escriba la {i + 2} nota: "))
    lista.append(nota)

def promedio(x):
    promedio_lista = sum(x) / len(x)
    return promedio_lista 


print(promedio(lista))