#tipos de datos
a = 2 #numero entero
b = 2.1 #numero flotante
c = 4+3j # numero complejo
d = False # Dato de tipo booleano
e = True # Dato de tipo booleano
f= "cadena"

print(type(a),a,", Este es el entero")
print(type(b),b,", Este es el flotante")
print(type(c),c,", Este es el complejo")
print(type(d),d,", Este es booleano")
print(type(e),e,", Este es booleano")
print(type(f),f,", Este es una cadena de caracteres")

#operadores aritmeticos
#   potencias
import math
print(2**8)
print(pow(2,8))
print(math.pow(2,8))
#   #Operador Modulo %
var = 10%2
print(var)
#   suma resta multiplicaion 
z = (2+3)*4
print(z)

#operadores logicos 
#    AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)
#    or
print(True or True)
print(True or False)
print(False or True)
print(False or False)
#    not
print(not(True))
print(not(False))

#operadores racionales
print(2>3)
print(2<3)
print(2>=3)
print(2<=3)
print(2==3)
print(2!=3) #diferentes

estatura=float(input("Ingrese la estatura en metros: "))
print(estatura)
peso=float(input("Ingrese el peso en kilogramos: "))
print(peso)
imc=peso/(estatura**2)
print("el indice de masa corporal es: ",round(imc,1))

# Problema salrio 
#   Se ingresan los datos
Salario,CanHorasEx,Bon=input().split()
Salario = float(Salario)
CanHorasEx = int(CanHorasEx)
Bon=int(Bon)

#   Operaciones
ValHora = Salario/(192) #Valor de la hora normal
ValHoraEx = ValHora*(1.25) #Valor de la hora extra 
Bonificaciones = (Salario)*(1.05) #Bonificacion
SalarioTotal = Salario + (ValHoraEx*CanHorasEx) + (Bonificaciones*Bon)
Total = SalarioTotal-((SalarioTotal*0.035)+(SalarioTotal*0.04)+(SalarioTotal*0.01))
print(round(Total,1))