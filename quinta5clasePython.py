#Ejercicios diccionario
#   ejercicio 1
divisa=input('Ingrese la divisa: ')
d={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
for i in d:
  if i==divisa:
    print(d[divisa])
    break
else:
    print('La divisa no esta')

#   ejercicio 2
nombre=input('Ingrese su nombre: ')
edad=input('Ingrese la edad: ')
direccion=input('Ingrese su direccion: ')
telefono=input('Ingrese su telefono: ')

Datos = {
  "Nombre": nombre,
  "Edad": edad,
  "Direccion": direccion,
  "Telefono": telefono
}
x = Datos["Nombre"]
y = Datos["Edad"]
z = Datos["Direccion"]
q = Datos["Telefono"]

print(x," tiene",y, " años, vive en, ", z, " y su número de teléfono es",q)
#   como lo hizo el profe
print('Ingrese los datos ')
nom=input('Ingrese el Nombre:')
edad=int(input('Ingrese el Edad: '))
dir=input('Ingrese el Direccion: ')
tel=int(input('Ingrese el numero de Tel: '))
d={'Nombre':'','Edad':'','Dir':'','Tel':''}
d['Nombre']=nom
d['Edad']=edad
d['Dir']=dir
d['Tel']=tel

x=d['Nombre']
y=d['Edad']
z=d['Dir']
q=d['Tel']

print(x,'tiene', y, 'años','vive en',z, 'su numero de telefono es', q)

#ejercicio 3
fruta=input('Ingrese la fruta: ')
kilo=float(input('Ingrese la los kilos: '))
tabla = {
  "Platano": 1.35,
  "Manzana": 0.8,
  "Pera": 0.85,
  "Naranja": 0.7
}
for i in tabla:
  if i==fruta:
    x=float(tabla[fruta])
    print("el precio de la fruta es: ",x*kilo)
    break
else:
    print('La fruta no esta')

#   metodo de el profe 
frutas={'Platano':1.35,'Manzana':0.80,'Pera': 0.85,'Naranja':0.70}
fruta=input('Ingrese la fruta: ')
kilo=float(input('Ingrese la cantidad de kilos: '))
for i in frutas:
  if i==fruta:
    valor_fruta=frutas[fruta]*kilo
    print('El valor de la fruta es: ', valor_fruta)
    break
else:
  print('La fruta NO esta')

# otra mas jejej
frutas={'Platano':1.35,'Manzana':0.80,'Pera': 0.85,'Naranja':0.70}
fruta, kilo=input('Ingrese la fruta y la cantidad de kilos: ').split()
kilo=float(kilo)
if fruta in frutas:
  valor_fruta=frutas[fruta]*kilo
  print('El valor de la fruta es: ', valor_fruta)
else:
  print('La fruta NO esta')

#ejercicio 4
d={}
print(d)
d['Nombre_1'] = 'Juan'
d['Edad_2'] = 20
d['Sexo'] = 'M'
d['Telefono'] =12345
d['Email'] = 'Juan@hotmail.com'
print(d)

