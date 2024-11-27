numero1 = float(input("Ingresa el primer número: "))

signo = input("Ingresa el signo algebraico (+, -, *, /): ")

numero2 = float(input("Ingresa el segundo número: "))

if signo == "+":
    resultado = numero1 + numero2
elif signo == "-":
    resultado = numero1 - numero2
elif signo == "*":
    resultado = numero1 * numero2
elif signo == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Error: División entre cero no permitida"
else:
    resultado = "Error: Signo no válido"

print(f"El resultado de {numero1} {signo} {numero2} es: {resultado}")
