"""
#Funcional
texto="SSEEHDDOGBSW"
alfabeto="SEOG"
clave="ESHC"
for i in range(len(clave)):
    texto=texto.replace(alfabeto[i],clave[i])
print(texto)

"""

#diccionario funcional
cesta={}
centinela="si"
while centinela=="si":
    clave=input("dato a introducir: ")
    valor=int(input(clave+":"))
    cesta[clave]=valor
    print(cesta)
    centinela=input("Si desea continuar===>si: ")

print("su lista es ",cesta)

total=0
for null,precio in cesta.items():
    total +=precio

print(total)
