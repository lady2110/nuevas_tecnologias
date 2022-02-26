nivelAgua= int(input("Digita la cantidad de agua de la represa: "))
print(f"El nivel del agua es {nivelAgua}")

if(nivelAgua < 200):
	print("nivel de agua por debajo de los 200")
elif(nivelAgua >= 200 and nivelAgua < 400):
	print("nivel de agua adecuado")
else:
	print("Nivel del agua elevado mayor a 400")

