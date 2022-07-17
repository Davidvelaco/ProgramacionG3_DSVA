suma=0
contador3=0
contador5=0
contador_par=0
contador_impar=0
for i in range(1,16):
    contador3=0
    contador5=0
    contador_par=0
    contador_impar=0
    print("La tabla del",i,"es:")
    print("\n")
    for j in range(1,16):
        resultado=j*i
        if resultado % 3==0:
            contador3+=1
        if resultado % 5==0:
            contador5+=1
        if resultado % 2==0:
            contador_par+=1
        else:
            contador_impar+=1
        suma+=resultado
        print(i,"*",j,"=",resultado)
    print("La suma de los numeros es: ",suma)
    print("El promedio de los numeros es",suma/15)
    print("El multiplo de 3 son:", contador3)
    print("El multiplo de 5 son:", contador5)
    print("Los numeros pares son:", contador_par)
    print("Los numeros impares son:", contador_impar)
    print("\n")