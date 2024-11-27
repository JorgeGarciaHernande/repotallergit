
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):  # Itera del 1 al 10
    print(f"{numero} * {i} = {numero * i}")
