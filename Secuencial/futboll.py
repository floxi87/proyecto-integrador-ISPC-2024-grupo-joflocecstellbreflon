"""Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, para ello recibe cada semana la información de la cantidad total 
de partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado recibe un punto, por cada partido ganado 
tres puntos y por los perdidos cero puntos."""

puntos_empatado=1
puntos_ganado=3
semanas_num = int(input("Escriba la cantidad de semanas: "))
count = 0
puntos_total = 0

while count < semanas_num:
    empatado = int(input("Ingrese cuántos partidos empató: "))
    perdido = int(input("Ingrese cuántos partidos perdió: "))
    ganado = int(input("Ingrese cuántos partidos ganó: "))
    puntos_semana = (empatado*puntos_empatado) + (ganado*puntos_ganado)
    puntos_total= puntos_total + puntos_semana  
    count += 1
    if count < semanas_num:
        print("Siguiente semana...")

print("Los puntos en total son: ", puntos_total)