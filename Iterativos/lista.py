"""1. Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, 
guardarlos en una lista y mostrarlos. """

lista = [ ]
nombre = str(input("Ingrese un nombre: "))
lista.append(nombre)

for i in range(9):
    nombre = str(input("Ingrese un nombre: "))
    while nombre in lista:
        nombre = str(input("Nombre repetido. Ingrese otro: "))
    lista.append(nombre)
    i +=1
print(lista)
#while len(lista)<9:                   <---------------- otra forma
#    nombre = str(input("Ingrese un nombre: "))
#    while nombre not in lista:
#        lista.append(nombre)
#print(lista)

"""2. Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo."""

lista.pop(3)
lista.pop()
lista.sort()
print(lista)