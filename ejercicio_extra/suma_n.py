"""Pograma que calcula la suma de los primeros n números naturles."""

suma=0
j=1
print("Dame el valor de n:\n")

# input 
n=int(input())

# processing
while j<=n:
    suma=suma+j
    j=j+1

# output
print("La suma es: ",suma)

# Fin