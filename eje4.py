#4.Se desea realizar un algoritmo que almacene las letras del alfabeto, y debe mostrar las posiciones de las letras donde se encuentran cuando una persona, digita un nombre o una palabra.


lasLetras=[]
vectorPosicion=[]
contador=-1
n=0

print("Cambiando letras a numeros(Codificador)")

n=int(input("número de letras que vas a ingresar= "))
print("Ingrese las letras que se remplazaran por numeros")

for i in range(0,n):
    llenar1=input("Ingrese letra= ")
    lasLetras.append(llenar1)
    contador=contador+1
    vectorPosicion.append(contador)


print("Las letras son= ",lasLetras)
print("La posición en el listado es= ",vectorPosicion)


letras="".join([str(_) for _ in lasLetras])
print(letras)

palabra=input("ingrese un nombre o una palabra= ")

vectorPalabraFinal=[]

for i in range(len(palabra)): 
    llenar2=palabra[i]
    print(llenar2)
    for j in range(len(letras)):
        if(letras[j]==llenar2):
            print("Si")
        

            
    
        



"""

import string

letra=[]

def listAlphabeth():
    return list(string.ascii_lowercase)

print(listAlphabeth())

letra=listAlphabeth()
posicion=[]
for i in range(len(listAlphabeth())):
    posicion.append(i)

print(posicion)






"""







    




