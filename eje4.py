#4.Se desea realizar un algoritmo que almacene las letras del alfabeto, y debe mostrar las posiciones de las letras donde se encuentran cuando una persona, digita un nombre o una palabra.

vectorLetras=[]
vectorNombre=[]
vectorPosicion=[]
contador=0
n=0

n=int(input("Ingrese el numero de letras a ingresar= "))
print("Ingrese las letras")

for i in range(0,n):
    llenar1=input("Ingrese letra= ")
    vectorLetras.append(llenar1)
    contador=contador+1
    vectorPosicion.append(contador)


print(vectorLetras)
print(vectorPosicion)

palabra=input("ingrese un nombre o una palabra= ")





    




