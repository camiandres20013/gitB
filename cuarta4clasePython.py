#   Diccionario 
#Diccionarios
estudiantes={1:['Nombre: Juan', 'Apellido: Perez',['CC','Prob','Etica'], 18],
             2:['Nombre: Pedro', 'Apellido: Rojas',['Español','Prob','Calculo'], 19],
             3:['Nombre: Maria', 'Apellido: Suarez',['CC','Etica','Calculo'], 19]}
print(estudiantes[3])

#cambios 
estudiantes[3]= ['Nombre: Maria', 'Apellido: Suarez',['CC','Etica','Calculo'], 21]
print(estudiantes)

#Ejemplos
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y = thisdict.get("year")
z = thisdict.keys()
print(x)
print(y)
print(z)

#22222 agregar al diccionario
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #Antes del cambio
car["color"] = "white"
print(x) #Después del cambio

#333333 actualizar
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)
thisdict.update({"year": 2023})
print(thisdict)

# borrar
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.pop("model")
print(thisdict)

#pop item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.popitem()
print(thisdict)

#borrar por clave
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
del thisdict["model"]
print(thisdict)

#recorrer el diccionario con valores y llaves
dic= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in dic:
  print(i)
print('-----------')
for i in dic:
  print(dic[i])
print('-----------')
for x in dic.values():
  print(x)
print('-----------')
for x in dic.keys():
  print(x)
print('-----------')
for x, y in dic.items():
  print(x, y)

#copiar diccionaro
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
mydict = thisdict.copy()
print(mydict)