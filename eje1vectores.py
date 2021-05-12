#1. Inserte valores numéricos en el siguiente vector y ordénelos de forma ascendente, descendente. Muestre el menor valor y el mayor valor.

datos=[]
mayor=None
menor=None

for i in range(0,15):
    nuevoDato=int(input("Ingrese valores enteros: "))
    datos.append(nuevoDato)
    if mayor is None or nuevoDato > mayor:
        mayor=nuevoDato
    if menor is None or nuevoDato < menor:
        menor=nuevoDato


datos.sort()
print("Los datos en forma ascendente ===> ",datos)

datos.reverse()
print("Los datos en forma descendente ===> ",datos)

print("El numero mayor es ===> ",mayor)

print("El numero menor es ===> ",menor)


    

