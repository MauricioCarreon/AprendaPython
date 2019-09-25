for i in range(1,11):
    encabezado="tabla del {}"
    print(encabezado.format(i))
    #print sin argumentos es un salto de linea.
    print()
    #dentro de un for, se pone otro for
    for j in range(1,11):
        #aqui, i contiene el numero base de la tabla
        #y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #al concluir con las interaciones indicadas
        #se ejecuta este codigo, que es un salto de
        #linea
        print()