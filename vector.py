datos=[]
for i in range(0,7):
    nuevoDato=int(input("Ingrese valores enteros: "))
    datos.append(nuevoDato)

for i in range(0,7):
    print (datos[i])


valor_buscar=(int(input("cual es el valor a buscar: ")))
for i in range(0,7):
    if datos[i]==valor_buscar:
        print("El numero ",datos[i],"ubicado en la celda ",i)


valor_buscar_eliminar=(int(input("cual es el valor a eliminar y remplazar en cero: ")))
for i in range(0,7):
    if datos[i]==valor_buscar_eliminar:
        print(datos[i],i)
        datos[i]=0


print("Dtos en orden")
for i in range(0,7): 
    print (datos[i])



print("Dtos desde atras hacia adelante")   
for i in range(0,1):
    datos.sort()
    print(datos)
        





"""
valor_buscar_eliminar=(int(input("cual es el valor a eliminar y desplazar: ")))
for i in range(0,7):
    if datos[i]==valor_buscar_eliminar:
        print(datos[i],i)
        datos[i]=0
"""
