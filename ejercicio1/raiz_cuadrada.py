# Bucle While

import math
numero=int(input("Digite un número: "))

while numero<0:
    print("Error-> Debería ser un número poitivo")
    numero=int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")