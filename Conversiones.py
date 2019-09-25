#se declara una variable str, con una cadena de digitos
numero="1234"
#se muestra el tipo     ue tiene la variable. la salida de type()
#no es un str es un dato type
print(type(numero))
#se convierte la cadena a su equivalencia int
numero=int(numero)
#se muestra como el tipo ha cambiado, auqnue se usa la misma
#variabe
print(type(numero))
#se declara un str con meta sustitucion (posiciones donde iran
# valores proporcionados usando format.)
salida="El numero utilizado es{}"
#se muestra el resultado. la meta sustitucion hara que donde esta 
#{} se coloque el valor del numero.
print(salida.format(numero))
