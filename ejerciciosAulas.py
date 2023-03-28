#conversion de temperaturas.
c=float(input('Ingrese la temperatura en Grados Celcius: '))
f=((9/5)*c)+32
r=((c*1.8))+491
k=c+273.15
print(c, 'es equivalente a', f,'Grados Fahrenheit')
print(c, 'es equivalente a', r,'Grados Rankine')
print(c, 'es equivalente a', k,'Grados Kelvin')

#ejercicio 2
repetir='s'
while repetir =="s" or repetir=="S":
  c=float(input('Ingrese la temperatura en Grados Celcius: '))
  f=((9/5)*c)+32
  r=((c*1.8))+491
  k=c+273.15
  print('Presione 1: si quiere convertir de Celcius a Fahrenheit')
  print('Presione 2: si quiere convertir de Celcius a Rankine')
  print('Presione 3: si quiere convertir de Celcius a Kelvin')
  opción = input('ingrese la opcion: ')       
  while opción !="1" and opción !="2" and opción !="3":
      print("Valide la tecla ingresada")
      opción = input("Pulse la tecla 1, 2 o 3 y pulse el retorno de carro: ")
  else:
      if opción == "1":
          print(c, 'es equivalente a', f,'Grados Fahrenheit')
      elif opción == "2":
          print(c, 'es equivalente a', r,'Grados Rankine')
      else:
          print(c, 'es equivalente a', k,'Grados Kelvin')
  repetir=input('Desea continuasr S/N')

#opcion del profesor 
#Conversión de temparaturas.
repetir='S'
while repetir=='S' or repetir=='s':
	print('Ingrese la temperatura en Grados Celcius')
	c=float(input('Temperatura: '))
	print('Presione 1 si desea Grados Fahrenheit')
	print('Presione 2 si desea Grados Rankine')
	print('Presione 3 si desea Grados Kelvin')
	num=int(input('Ingrese la opción : '))

	if num ==1:
		f=round(((9/5)*c) + 32,1)
		print(c,'Grados Celcius', ' es equivalente a', f,'Grados Fahrenheit')

	elif num==2:
		r=round(((c*1.8)+491.67),1)
		print(c,'Grados Celcius', 'es equivalente a', r,'Grados Rankine')

	elif num==3:
		k=round(c+273.15,1)
		print(c,'Grados Celcius', 'es equivalente a', k,'Grados Kelvin')
	else:
		print('Numero invalido. Ingrese un numero valido')

	repetir=input('¿Desea continuar S/N?')
        
#ejecicio 3
c=float(input('Ingrese la temperatura en Grados Celcius: '))
def f(c):
     f=((9/5)*c)+32
     return f
def r(c):
     r=((c*1.8))+491
     return r
def k(c):
     k=c+273.15
     return k

repetir='s'
while repetir =="s" or repetir=="S":
  print('Presione 1: si quiere convertir de Celcius a Fahrenheit')
  print('Presione 2: si quiere convertir de Celcius a Rankine')
  print('Presione 3: si quiere convertir de Celcius a Kelvin')
  opción = input('ingrese la opcion: ')       
  while opción !="1" and opción !="2" and opción !="3":
      print("Valide la tecla ingresada")
      opción = input("Pulse la tecla 1, 2 o 3 y pulse el retorno de carro: ")
  else:
      if opción == "1":
          print(c,'Grados Celcius', ' es equivalente a', f(c),'Grados Fahrenheit')
      elif opción == "2":
          print(c,'Grados Celcius', 'es equivalente a', r(c),'Grados Rankine')
      else:
          print(c,'Grados Celcius', 'es equivalente a', k(c),'Grados Kelvin')
  repetir=input('Desea continuasr S/N')

#opcion del profesor 
#Conversión de temparaturas.
def gf(n):
	return round(((9/5)*c) + 32,1)

def gr(n):
	return round(((c*1.8)+491.67),1)

def gk(n):
	return round(c+273.15,1) 

repetir='S'
while repetir=='S' or repetir=='s':
	print('Ingrese la temperatura en Grados Celcius')
	c=float(input('Temperatura: '))
	print('Presione 1 si desea Grados Fahrenheit')
	print('Presione 2 si desea Grados Rankine')
	print('Presione 3 si desea Grados Kelvin')
	num=int(input('Ingrese la opción : '))

	if num ==1:
		print(c,'Grados Celcius', ' es equivalente a', gf(c),'Grados Fahrenheit')

	elif num==2:
		
		print(c,'Grados Celcius', 'es equivalente a', gr(c),'Grados Rankine')

	elif num==3:
		
		print(c,'Grados Celcius', 'es equivalente a', gk(c),'Grados Kelvin')
	else:
		print('Numero invalido. Ingrese un numero valido')

	repetir=input('¿Desea continuar S/N?')


#ejercicio 4
l=[]
print('Ingrese cuatro numeros reales')
n1=float(input('Ingrese el primer numero:'))
l.append(n1)
n2=float(input('Ingrese el segundo numero:'))
l.append(n2)
n3=float(input('Ingrese el tercer numero:'))
l.append(n3)
n4=float(input('Ingrese el cuarto numero:'))
l.append(n4)
n5=float(input('Ingrese el quinto numero:'))
l.append(n5)

max_value = max(l)
min_value = min(l)
average = sum(l) / len(l)

print(f"El valor maximo es: {max_value}")
print(f"El valor minimo es: {min_value}")
print(f"El promedio es: {average}")

#otra forma
#Orden Numeros en una lista
def ordenar(lista, lon):
  if lon>1:
    for i in range(lon-1):
      if lista[i]>lista[i+1]:
        var=lista[i]
        lista[i]=lista[i+1]
        lista[i+1]=var
      ordenar(lista, lon -1)

l=[]
print('Ingrese cuatro numeros reales')
n1=float(input('Ingrese el primer numero:'))
l.append(n1)
n2=float(input('Ingrese el segundo numero:'))
l.append(n2)
n3=float(input('Ingrese el tercer numero:'))
l.append(n3)
n4=float(input('Ingrese el cuarto numero:'))
l.append(n4)
n5=float(input('Ingrese el quinto numero:'))
l.append(n5)

ordenar(l,len(l))
print('El numero menor es :', l[0])
print('El numero mayor es: ', l[len(l)-1])
count=0
acum=0
for i in l:
  count+=i
  acum+=1


promedio=count/acum
print('El promedio es: ', promedio)
#[50, 42, 23, 32, 1]