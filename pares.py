#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
#Nota: para saber si un número es par hacer i % 2 == 0)

num = int(input("Ingrese el num: "))
count = 0

while count <=num:
    if count % 2 ==0:
        print(count)
    count +=1