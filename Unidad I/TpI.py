
print ("Hola mundo")
#Nombre y saludo 
nombre=input("Ingrese su nombre:")
print(f"Hola {nombre}!")
#Nombre, apellido, edad y lugar de residencia
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
lugar=input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido},tengo {edad}años y soy de {lugar}")
#Ejercicio 4 - Radio de circulo 
radio=float(input("Inserte el radio de un circulo:"))
area=3.14*(radio**2)
perimetro= 2*3.14*radio
print(f"El area del circulo es {area:.2f}")
print(f"El perimetro del circulo es {perimetro:.2f}")
#Ejercicio 5 - Cantidad de segundos
segundos=int(input("Ingrese una cantidad de segundos:"))
hora=segundos/3600
print(f"Equivale a {hora} horas")
#Ejercicio 6 Numero y tabla de multiplicar
numero=int(input("Ingrese un numero:"))
print(f"La tabla de multiplicar del numero {numero} es:")
for i in range(1, 11):
    print(numero*i)
#Ejercicio 7 Dos numeros enteros distintos  del 0 y mostrar por pantalla el resultado de sumarlos, dividirlos,multiplicarlos y restarlos
num1=int(input("Ingrese un numero entero(distinto de cero):"))
num2=int(input("Ingrese otro numero entero (distinto de cero):"))
suma=num1+num2
print(f"La suma de {num1} y {num2} es: {suma}")
division=num1/num2
print(f"La division de {num1} y {num2} es: {division}")
multiplicacion=num1*num2
print(f"El producto de {num1} y {num2} es: {multiplicacion}")
resta=num1-num2
print(f"La resta de {num1} y {num2} es: {resta}")
#Ejercicio 8 - Altura y peso
altura=float(input("Ingrese su altura en metros:"))
peso=float(input("Ingrese su peso en kilogramos:"))
imc=peso/altura**2
print(f"Su índice de masa corporal es: {imc}")
#Ejercicio 9 - Grados Celsius a Fahrenheit
grados=float(input("Ingrese una temperatura en grados Celsius:"))
fahrenheit=9/5*grados+32
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")
#Ejercicio 10 
num1=float(input("Ingrese el primer numero:"))
num2=float(input("Ingrese el segundo numero:"))
num3=float(input("Ingrese el tercer numero:"))
promedio=num1+num2+num3/3
print(f"El promedio de los tres numeros es: {promedio}")


