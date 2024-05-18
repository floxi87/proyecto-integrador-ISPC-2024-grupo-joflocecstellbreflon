Algoritmo sin_titulo
	Definir part_ganados,part_perdidos,part_empatados,victoria,derrota,empate, puntos Como Entero
	victoria= 3
	empate=1
	derrota=0

	escribir "partidos ganados"
	leer part_ganados
	Escribir "partidos perdidos"
	leer part_perdidos
	escribir "partidos empatados"
	leer part_empatados
	
	puntos=(part_ganados*victoria+part_perdidos*derrota+part_empatados*empate)
	escribir"los puntos totales acumulados:", puntos
	
FinAlgoritmo
