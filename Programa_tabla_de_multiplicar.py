
#Programa tabla de multiplicar (for)
print("Tabla de multiplicar")
tabla = int(input("Ingrese un valor para la tabla que quiere visualizar-->:"))
for x in range(1,11):
  resultado = x * tabla
  print(tabla, "*", x, "=", resultado)

#Programa tabla de multiplicar del 1 al 10 (for)
print("Tabla de multiplicar")
for tabla in range(1,11):
  print("Tabla del ", tabla)
  for i in range(11):
    multi = tabla * i
    print(tabla, "x ", i, "= ", multi)
  print("")

#Funcion para llamr a una tabla de multiplicar
def tablaMult(tabla):
  print("Tabla de multiplicar")
  for x in range(11):
    resultado = x * tabla
    print(tabla, "*", x, "=", resultado)
tabla = int(input("Ingrese un valor para la tabla que quiere visualizar-->:"))
tablaMult(tabla)

#Funcion factorial
def factorial(numero):
  print("Factorial de un numero")
  fact = 1
  for i in range(1,(numero+1)):
      fact = fact * i
  return fact
numero = int(input("Ingrese un valor factorial que quiere visualizar-->:"))
print("El factorial de ", numero, "es---> ", factorial(numero))