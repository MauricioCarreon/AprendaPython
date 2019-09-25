entrada=input()
print(type(entrada))
#la variable booleana contiene el resultado de verificar
#si lo capturado es digito y si no se encuentra un punto
# en lo capturado lo que indicara se que trata de un
#numero con decimales es decir float. si find retorna -1
#quiere decir que lo buscado en este caso un punto decimal
#no se encontro. si esentero es True lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #lineas que se ejecutan si la condicion es verdadera (true)
    print("dato entero. ¡muy bien!")
else:
    #lineas que se ejecutarn si la condicion es falsa (false)
    print("dato no es entero. intentar nuevamente")