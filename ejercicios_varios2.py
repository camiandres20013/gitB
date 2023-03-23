#Algoritmo de imc
estatura=float(input('Ingrese la estatura en metros: '))
peso=float(input('Ingrse el peso en kilogramos: '))
imc=peso/(estatura*estatura)
print('El IMC es de :', round(imc,1))

#Uso de Condicionales
x=int(input('Ingrese el numero a evaluar: '))
if x > 10:
  print('El numero es mayor')
else:
  print('El numero es menor')

#Uso de Condicionales (elif)
x=int(input('Ingrese el numero a evaluar: '))
if x < 10:
  print('El numero es menor a 10')
elif x==10:
  print("El numero es igual a 10")
else:
    print("El numero es menor a 10")

#Uso de Condicionales (Varias preguntas)
y=int(input('Ingrese el numero a evaluar: '))
z=int(input('Ingrese el numero a evaluar: '))
q=int(input('Ingrese el numero a evaluar: '))
if y>10 and z>10 and q>10:
  print('los numeros son mayores a 10')
elif y==10 and z==10 and q==10:
  print("todos los numeros son iguales a 10")
else:
  print("alguno o todos los numeros son menores a 10")

#Bucles
for i in range(0,11,2):
  print(i)

#Objetos iterables
#Range
#String
#Listas

var='Hola Mundo'
for i in var:
  print(i)

l=[1,1.2,'str',False]
for i in l:
  print(i)

#imprimir los numeros pares entre 0 y 20
for i in range(21):
  if i%2==0:
    print(i)

#imprimir los numeros impares entre 0 y 20
for i in range(21):
  if i%2 !=0:
    print(i)

#Acumulador 
cont=0
for i in range(6):
  cont=cont+1
  print(cont)
print("resultado:", cont)

#Numeros primos 
num=11
cont=0

for i in range (1,num+1):
  if num%i==0:
    cont+=1
if cont ==2:
  print("El numero es primo")
else:
  print("El numero no es primo")

#ciclos anidados
for i in range(1,10+1):
  for j in range (1,5+1):
    print(i,j)

#imprimir los primeros 100 numeros primos 
for i in range(1,101):  
  num=i
  cont=0
  for i in range (1,num+1):
   if num%i==0:
     cont+=1
  if cont ==2:
    print(i)
#ciclo while
numMax=int(input("ingrese el numero de impresiones:"))
x=0
while x<=numMax:
  print(x)
  x+=1

  