import math

#	Convertir argumento a radianes
x_deg = float(input('Valor del argumento en grados: '))
x = math.radians(x_deg)

n = int(input('Número de terminos a sumar: '))

#	Error verdadadero/total porcentual
err_verd = 100.0

#	Valor verdadero de sen(x)
sen_verd = math.sin(x)

#	Inicializar el acumulador en 0
sen_x = 0.0

#	Encabezados
print ("\n\n{:^2} {:^10} {:^16} {:^20}".format("Termino", "k", "sen(x)", "err_verd"))

#	Acumular/Sumar terminos
for k in range(n):
	#	Acumula la suma
	sen_x = sen_x + (-1)**k * x**(2*k+1) / math.factorial((2*k+1))
	#	Calcula el error verdadero
	err_verd = abs((sen_verd -sen_x) / sen_verd)*100
	print("{:^2d} {:^19d} {:^15.10f} {:^15.4g}".format(k+1, k, sen_x, err_verd))




#Serie de Taylor para el seno en Python. (2020, 3 abril). 
#[Vídeo]. YouTube. https://www.youtube.com/watch?v=JrlwvWVhlJ4