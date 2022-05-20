# Ejemplo menú

num=int(input("Menú: 1(Ver números) 0(Salir): "))
while num!=0:

    x = 0
    while x<10:
        print("EL valor de x es: ",x)
        x += 1
    
    print("Saliendo...")
    num=int(input("Menú: 1(Ver números) 0(Salir): "))

print("Gracias")