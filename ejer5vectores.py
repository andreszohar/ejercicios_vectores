#Se desea realizar un algoritmo que permita almacenar dos valores que son ingresados en código binario, y se debe de realizar la suma y la resta de estos dos valores

num1=str(input("ingrese el numero binario1: "))
num2=str(input("ingrese el numero binario2: "))

convertido_num1=int(num1,2)
convertido_num2=int(num2,2)
print("numero binario 1==> ",convertido_num1)
print("numero binario 2==> ",convertido_num2)

print("Sumar==>1   Restar==>2")
pregunta=input(" ")

if(pregunta=="1"):
    suma=convertido_num1+convertido_num2
    print("La suma en decimal: ",suma)
    print("La suma en binario: ",format(suma,"0b"))


elif(pregunta=="2"):
    resta=convertido_num1-convertido_num2
    print("La resta en decimal: ",resta)
    print("La resta en binario: ",format(resta,"0b"))


else:
    print("ERROR(NO EXISTE EL NUMERO QUE SELECCIONASTE)")







"""


"""









