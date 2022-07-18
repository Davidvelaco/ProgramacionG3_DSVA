suma=0 #Se asigna la variable "suma", con numero igual a 0
cont3=0 #Se asigna la variable "contador3", con numero igual a 0
cont5=0 #Se asigna la variable "contador5", con numero igual a 0
contpar=0 #Se asigna la variable "contadorpar", con numero igual a 0
contimpar=0 #Se asigna la variable "contadorimpar", con numero igual a 0
while True: #Se coloca while true para hacer un bucle"
    n1=int(input("Ingreses un número entre 1 y 15:")) #Ingresar numero por teclado en el rango solicitado
    if n1<1: #Ingresamos un funcion si que especifique que el numeor ingresado no puede ser menor que 1
        print('Vuelva a ingresar un número entre 1 y 15') #Si no se ingresa el numero solicitado
    elif n1>15: #Ingresamos  un elif para que no se ingrese un numero mayor a 15
        print('Vuelva a ingresar un número entre 1 y 15') #Si no se ingresa el numero solicitado
    else: #Si no se cumple las otras funciones
        break #Si else se cumple se rompe el bucle 
a=int(input("Ingrese el numero para la multiplicacion: ")) #Se ingresa por teclado el numero que se va a multiplicar 
print("\n") #Se ingresa un espacio para una mejor lectura al correr el programa
if a>=2 and a<=100: #Se asigna if con la condición a mayor o igual a 2 y menor o igual a 100
    for i in range(1,a+1): #Se asigna for con un rango i
        cont3=0 #Se asigna la variable "contador3", con numero igual a 0
        cont5=0 #Se asigna la variable "contador5", con numero igual a 0
        contpar=0 #Se asigna la variable "contadorpar", con numero igual a 0
        contimpar=0 #Se asigna la variable "contadorimpar", con numero igual a 0
        print("La tabla del numero",i,"es: ") #Se imprime la condicion del for
        print("\n") #Se ingresa un espacio para mejor lectura al correr el programa
        for j in range(1,16): #Se asigna for con un rango j
            resultado=j*i #Se asigna la variable "resultado", el valor de j multiplicado por i
            if (resultado%5)==0: #Se coloca un if con la condicion de resultado modulo de 5 igual a 0
                cont5+=1 #Se asigna la variable contador5 como contador5 más 1
            if (resultado%3)==0: #Se coloca un if con la condicion de resultado modulo de 3 igual a 0
                cont3+=1 #Se asigna la variable contador3 como contador3 más 1
            if (resultado%2)==0: #Se coloca un if con la condicion de resultado modulo de 2 igual a 0
                contpar+=1 #Se asigna la variable contadorpar como contador2 más 1
            else: #Si la condicion if no se cumple entonces
                contimpar+=1 #Se asigna la variable contadorimpar como contadorimpar más 1
            suma+=resultado #Se asigna la variable "suma", el valor de suma más resultado
            print(i,"x",j,"=",resultado) #Se imprime la condicion del if o else
        print("La suma de los numeros es: ",suma) #Con un texto se imprime la variable suma
        print("El promedio de los numeros es: ",suma/15) #Con un texto se imprime la variable suma/b
        print("Los multiplos de 3 son: ",cont3) #Con un texto se imprime la variable contador3
        print("Los multiplos de 5 son: ",cont5) #Con un texto se imprime la variable contador5
        print("Los numeros pares son: ",contpar) #Con un texto se imprime la variable contadorpar
        print("Los impares son: ",contimpar) #Con un texto se imprime la variable contadorimpar
        print("\n") #Se ingresa un espacio para mejor lectura al correr el programa
        
        
        
        
        
        
        
        