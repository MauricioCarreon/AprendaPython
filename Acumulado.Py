#se declaranlas variables de trabajo,con tipo explicito
acumulado=int(0)
numero=str("")

#al colocar true como condicion de while se forma un
#ciclo infinito que nose rompera hasta que de forma
#explicita se utilice la instrruccion break.
while True:
    numero=input("dame un numero entero: ")
    if numero=="":
        #si el numero es vacio, reporta la situacion y sale
        print("Vacio. salida del programa. ")
        break
    else:
        #si se proporciono valor, acumulado = acumulado + numero
        #se realiza el calulo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="monto acumulado: {}"
        print(salida.format(acumulado))