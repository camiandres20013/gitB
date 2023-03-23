#tuplas
tubla=(1,2.2,False,'hola')
print(len(tubla)) # tamaño de la Tupla
print(tubla) #IPRIME LA TUPLA
print(tubla[3]) #imprime la dupla en la posicion 4
#   recorrer la tupla
for i in tubla:
    print(i)

for i in range(len(tubla)):
    print(tubla[i])

#   cuantas veses aparece repetido un dato en una tupla
tu1=(1,1,2,4,4,5,6,7,8,8,9)
x=tu1.count(1)
print(x)

x=tu1.index(5)
print(x)

#listas
lista=[1,2.2,False,'hola']
print(type(lista))
print(len(lista))
print(lista[0])
print(lista)
lista[0]=9
print(lista)
lista.append('mundo')
print(lista)

for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

#   lista posicion negativa
l=[1,2,3,4,5,6,7,8,9,10]
print(l[-1])
print(l[-10])

for i in range(len(l)-1,-1,-1):
    print(l[i])

#   cortar la lista
print(l[2:5])
print(l[:5])
print(l[5:])

#Llenar listas
m=[]
print(m)
for i in range(21):
    m.append(i)
print(m) 

#llenarla con numeros aleatorios 
import random
print(random.random())
print(random.random()*10)
print(round(random.random()*10,1))
print(random.randint(0,10))

#    Lista
mi=[]
print(mi)
for i in range(21):
    mi.append(random.randint(0,10))
print(mi)
#   remover 
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)

#   concatenacion de listas
a=[1,2,3,4]
b=[5,6,7,8,9]
c=a+b
d=b+a
print(c)
print(d)

#   enumerate
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

#otro
l1 = ["eat", "sleep", "repeat"]
for pos, ele in enumerate(l1):
  print(ele)
  print(pos)

#otro
l1 = ["eat", "sleep", "repeat"]
for pos, ele in enumerate(l1):
  print(pos,ele)

# otros
fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.insert(3, "orange")
print(fruits)

import random
l=[]
for i in range(11):
  l.append(random.randint(1,100))
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.sort(reverse=False)
print(l)

#listas anidadas
#Matriz
l=[[1,2,3,4,5]]
l[0][4]
print(l[0][4])

l=[[1,2,3,4,5],['A','B','C','D']]
l[0][4]
print(l[1][2])

#recorer las matrises
m=[[1,2,3],
  [4,5,6],
  [7,8,9]]

for i in range(len(m)):
  for j in range(len(m)):
    print(i,j)

print(m[2][2])

for i in range(len(m)):
  for j in range(len(m)):
    print(m[i][j])

#ejemplo: lista de numeros, sacar el promedio
from statistics import mean
import random
l=[]
for i in range(10):
  l.append(random.randint(1,100))
print(l)
print(mean(l))

#   echos a mano (utilizando sum y len)
promedio=sum(l)/len(l)
print(promedio)

#   echos a mano (utilizando acum y len)
acum=0
for i in l:
  acum+=i
avg=acum/len(l)
print(avg)

#   otra
acum=0
cont=0
for i in l:
  acum+=i
  cont+=1
avg=acum/cont
print(avg, 'Utilizando acum y cont')