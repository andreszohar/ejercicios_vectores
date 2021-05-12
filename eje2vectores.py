#2. Se tiene un vector de 20 posiciones donde se desean almacenar marcas de vehículos , y se tiene un segundo vector donde se almacenan los precios del mismo.

import pandas as pd


df=pd.DataFrame({

"Marca":["Marca1","Marca2","Marca3","Marca4","Marca5","Marca6","Marca7","Marca8","Marca9","Marca10","Marca11","Marca12","Marca13","Marca14","Marca15","Marca16","Marca17","Marca18","Marca19","Marca20"],
"Precio":["200000","3000000","400000","500000","600000","7000000","8000000","9000000","3000003","3455500000","4500022200","2000191919","363635353","4664646464466","8899997779900","10","2727883000","7889003","8292992","36490092"]

})
df["Marca"]=df["Marca"].str.upper()

#print(df)

print("Listado de Marcas")
print(df["Marca"])
pregunta=input("Cual es la marca que deseas==> ").upper()
buscarMarca=df[df["Marca"]==pregunta]
print(buscarMarca["Precio"])
