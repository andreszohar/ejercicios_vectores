#3. Se tiene un vector que almacenara los nombres científicos de hongos, se deberá realizar un algoritmo que permita insertar los nombres en el vector, realizar la búsqueda, realizar la consulta por nombre. Para un total de 10 muestras.

hongo=[]
especie=[]

for i in range(0,10):
    llenar1=input("Ingrese nombre del hongo==> ")
    llenar2=input("Describalo==> ")
    hongo.append(llenar1)
    especie.append(llenar2)


print("Que hongo buscas")
print("Ingrese el hongo a buscar de la siguiente lista para su respectiva descripción")

for i in range(len(hongo)):
    print(hongo[i])

buscar=input("===> ")

for i in range(0,10):
    if hongo[i]==buscar:
        print(hongo[i],"= ",especie[i])
    