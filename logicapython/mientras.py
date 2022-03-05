#variable controladora
import math

print("Empanadas el machetico")
print("*******")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz cuadrada de un número")
print("2. Digita 2 para calcular la potencia de un número")
print("*******")

opcion = 1

while(opcion != 0):
	opcion = int(input("Digite una opcion: "))
	if(opcion == 0):
		print("Adios")
		break
	elif(opcion == 1):
		numero= int(input("Ingrese un número: "))
		raiz = math.sqrt(numero)
		print(f"la Raiz del numero {numero} es {raiz}")
	elif(opcion == 2):
		numero= int(input("Ingrese un número: "))
		potencia = math.pow(numero,2)
		print(f"la potencia del numero {numero} es {potencia}")
	else:
		print("Digita una opcion valida")

	

