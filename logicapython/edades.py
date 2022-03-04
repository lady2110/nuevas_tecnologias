edad = (input("Ingrese la edad: "))

while(edad.isdigit() != True):
	print("No es un numero")
	edad = (input("Ingrese la edad: "))
else:
	edad2 = int(edad)
	if(edad2 <= 14):
		print ("Niño")
	elif (edad2 <= 28):
		print ("Joven")
	elif (edad2 <= 60):
		print("Adulto")
	else:
		print("anciano decrepito")

