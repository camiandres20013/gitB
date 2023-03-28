#funciones matematicas 
import matplotlib.pyplot as plt

def linea(x):
  return x

def cuadrado(x):
  return x**2
l=[]
m=[]
for i in range(-3,4):
  l.append(linea(i))
  m.append(cuadrado(i))

print(m)

plt.plot(l,l)
plt.plot(l,m)
plt.grid()
plt.show()

print(m)

#   Area circulo
import math
def areaCirculo(radio):
  return math.pi*radio**2

print(round(areaCirculo(2),1))
print(areaCirculo(3))

#   Factorial recursivo
def factoR(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factoR(n-1)

for i in range(11):
  print('El Factorial de', i, 'es', factoR(i))