numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida="Numeros proporcionados: {} y {}. {}."
if (numero1==numero2):
    #entra aqui si los numeros capturados son iguales.
    print(salida.format(numero1, numero2,"los numeros son iguales"))
else:
    #condicionales añadidas, if dentro de otro if.
    #si los numeros no son iguales
    if numero1>numero2:
        #reporta si el primer numero es mayor al segundo
        print(salida.format(numero1, numero2, "el mayor es el primero"))
    else:
        #o de lo contrario. si el primero no es mayor al segundo.
        print(salida.format(numero1, numero2, "el mayor es el segundo"))