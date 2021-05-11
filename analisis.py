
lasLetras=["a","b"]


palabra=input("ingrese un nombre o una palabra= ")
for i in range(len(palabra)):
    print(palabra[i])

lista=[]
for i in range(0,3):
    llenar=input("Letra: ")
    for j in range(len(lasLetras)):
        if(llenar==lasLetras[j]):
            llenar=len(palabra[i])
            print(llenar)
    lista.append(llenar)

    

        
print(lista)

        

#convertir vector a palabra
#strLista="".join(lista)
#print(strLista)



