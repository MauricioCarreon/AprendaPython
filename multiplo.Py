#se captura un numero y se almacena una vez que es
#convertido a int
numero=int(input("dame un numero: "))
#se almacena en valores booleanos la evaluacion
#de residuales. si el residual es cero, quiere decir
#que el numero es multiplo.
esmultiplo3=((numero%3)==0)
esmultiplo5=((numero%5)==0)
esmultiplo7=((numero%7)==0)
#cuando se usa and, se resuelve por verdadero si todas
#las condiciones son verdaderas si al menos una condicion es
#verdadera. los parentesis le dice a python que
#las primeras dos condiciones son juntas y la tercera
#es indispensable
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("correcto")
else:
    print("incorrecto")