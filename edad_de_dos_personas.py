#ESTE ES UN EJEMPLO DE MODIFICACION
def tablaMult(tabla):
  print("Tabla de multiplicar")
  for x in range(11):
    resultado = x * tabla
    print(tabla, "*", x, "=", resultado)
tabla = int(input("Ingrese un valor para la tabla que quiere visualizar-->:"))
tablaMult(tabla)

#Programa qué compara Las edades de dos personas
edad_1=eval(input("Ingrese la edad de la primera persona-->:"))
numEntero = (isinstance(edad_1, int))
while numEntero == False:
    print("Valide la edad ingresada")
    edad_1 = eval(input("Ingrese la edad de la primera persona-->:"))
    numEntero = (isinstance(edad_1, int))
else:
    edad_2 = eval(input("Ingrese la edad de la segunda persona-->:"))
    numEntero = (isinstance(edad_2, int))
    while numEntero == False:
        print("Valide la edad ingresada")
        edad_2 = eval(input("Ingrese la edad de la segunda persona-->:"))
        numEntero = (isinstance(edad_2, int))
    else:
        if edad_1 > edad_2:
            print("La segunda persona es más joven que la primera persona")

        elif edad_1 < edad_2:
            print("La primera persona es más joven qué la segunda persona")
        else:
            print("Ambas personas tienen la misma")
