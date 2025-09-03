#1. Programa edad de usuario
edad=int(input("Ingrese su edad:"))

if edad>18: 
    print("Es mayor de edad.")
    
#2. Programa nota usuario
nota=float(input("Ingrese su nota: "))

if nota>=6:
    print("Aprobado.")
else:
    print("Desaprobado")
    
#3. Programa de números pares

numero=int(input("Ingrese un número par: "))

if numero%2==0:
    print("Usted ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4. Programa que solicite edad y categorias
edad=int(input("Introduce tu edad: "))

if edad>=0 and edad <=11:
    print("Eres un niño.")
elif edad>=12 and edad<18:
    print("Eres un adolescente.")
elif edad >=18 and edad<30:
    print("Eres un adulto/a joven.")
else:
    print("Eres un adulto.")

#5 Programa para validad longitud de contraseña
contraseña=input("Ingrese una contraseña (entre 8 y 14 caracteres):")

if 8<=len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6 Moda, Mediana y Media

from statistics import mode, median, mean
import random

#Crear la lista de 50 numeros aleatorios
numeros_aleatorios=[random.randint(1,100) for i in range (50)]
print("Lista de numeros:", numeros_aleatorios)

#Calcular moda, mediana y media
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)

print("Moda",moda)
print("Mediana",mediana)
print("Media",media)

#Determinar el sesgo
if media>mediana>moda:
    print("La distribución tiene sesgo positivo o a la derecha.")
elif media<mediana<moda:
    print("La distribución tiene sesgo negativo o a la iziquierda.")
elif media==mediana==moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar un sesgo.")

#7 Palabra o frase con vocal

texto=input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
   print(texto + "!")
else:
    print(texto)

#8 Programa de nombre y número de opción (mayusculas y minusculas)
nombre=input("Ingrese su nombre: ")

opcion=input("Ingrese 1 para ver su nombre en mayúsculas, 2 en minúsculas, 3 primera letra en mayúsculas: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida. ")

#9 Programa de magnitud de un terremoto
magnitud=float(input("Ingrese la magnitud del terremoto: "))

if magnitud<3: 
    print("Muy leve (Imperceptible).")
elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible).")
elif magnitud>=4 and magnitud<5:
    print("Moderado(sentido por personas,pero generalmente no causa daños).")
elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras débiles.)")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#10 Programa sobre estaciones del año
hemisferio=input("Ingrese en qué hemisferio se encuentra(N/S): ").upper()
mes=int(input("Ingrese en qué mes del año se encuentra (del 1 al 12): "))
dia=int(input("Ingrese en qué día del mes se encuentra: "))

if (mes==12 and dia>=21) or (mes==1 or mes==2) or (mes==3 and dia<=20):
    if hemisferio=="N":
        print("Invierno")
    else:
        print("Verano")
        
elif (mes==3 and dia>=21) or (mes==4 or mes==5) or (mes==6 and dia<=20):
    if hemisferio=="N":
        print("Primavera")
    else:
        print("Otoño")
elif (mes==6 and dia>=21) or (mes==7 or mes==8) or (mes==9 and dia<=20):
    if hemisferio=="N":
        print("Verano")
    else:
        print("Invierno")
elif (mes==9 and dia>=21) or (mes==10 or mes==11) or (mes==12 and dia<=20):
    if hemisferio=="N":
        print("Otoño")
    else:
        print("Primavera")
else:
    print("Ingrese una fecha válida.")









