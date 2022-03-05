print("Menú")
print("0. Salida")
print("1. Encuentre si el numero es multiplo de 2")
print("2. Sume 100 al numero ingresado")
print("3. Eleve a la 2 el numero ingresado")

opcion = 1

while(opcion != 0):
	opcion = int(input("Selecciones una opción: "))
	if(opcion == 1):
		numero = int(input("Ingrese un número: "))
		resultado = numero % 2
		if(resultado == 0):
			print("Es multiplo de 2")
		else:
			print("No es multiplo 2")
	elif(opcion == 2):
		numero = int(input("Ingrese un número: "))
		resultado = numero + 100
		print(resultado)
	elif(opcion == 3):
		numero = int(input("Ingrese un número: "))
		resultado = numero * numero
		print(resultado)
	elif(opcion == 0):
		print("Adiós")
	else:
		print("Opcion no valida")
	
	
		
		
			
				

	
	

