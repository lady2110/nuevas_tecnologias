numero = int(input("Ingrese un numero: "))
acumulado = 0
while(numero >= 0):
	acumulado = acumulado + numero
	print(acumulado)
	numero = int(input("Ingrese un numero: "))
else :
	print("Adios, ingresaste un valor negativo")
	