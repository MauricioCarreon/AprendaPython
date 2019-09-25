#python posee muchas librerias listas para utilizarse.
#a dichas librerias les da el nombre de modules(modue)
#para utilizar in modulo en un programa, primero debe
#importarse, usando la instruccion import
import random

#se define una variable float, y se le asigna un valor.
numero1=float(10.5)

#en python, una funcion es un conjunto de insturcciones que
#procesan una tarea especifica, como una unidad de ejecucion.
#se declara con def. todo el codigo posicionado a la derecha
#en la definicion, forma oarte de la funion.
def miFuncion():
    #se convierte a float el numero aleatorio enerando por
    #random.randrage() (solo estando disponible si se importa
    #el modulo random)
    numero2=float(random.randrange(1,10))
    #se utiliza meta sustituciones para mostrarresultados.
    mensaje="la suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

#se ejecuta la funcion definida en el codigo
miFuncion()
