# Codigo base lo hacen la coordinadora (alejandra)
print ("Bienvenido a la calculadora de Youssef, Houda, María y Alejandra")

Variable1 = int(input("Ingrese el primer número: "))
Variable2 =  int(input("Ingrese el segundo número: "))
Cuenta = input("Ingrese la operación a realizar (+, -, *, /): ")

# Operaciones las hacen los desarrolladores (maria  y alejandra)
if Cuenta == "+":
    print(Variable1 + Variable2)
elif Cuenta == "-":
    print(Variable1 - Variable2)
elif Cuenta == "*":
    resultado= Variable1 * Variable2
    elif Cuenta == "/":
        if Variable2 == 0:
            resultado= "Error"
            print("No se puede dividir por cero")
    
else:
    resultado=Variable1 / Variable2

else:
    resultado= "Error"

    print("No válido")

if resultado != "Error":
    print(f"{Variable1} {Cuenta} {Variable2} = {resultado}")
else:
    print("Error en la operación")








# Revisión la hace la coordinadora (alejandra)