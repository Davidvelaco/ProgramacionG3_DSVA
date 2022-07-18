suma=0 #Se asigna la variable "suma", con numero igual a 0
contador3=0 #Se asigna la variable "contador3", con numero igual a 0
contador5=0 #Se asigna la variable "contador5", con numero igual a 0
contadorpar=0 #Se asigna la variable "contadorpar", con numero igual a 0
contadorimpar=0 #Se asigna la variable "contadorimpar", con numero igual a 0
a=int(input("Ingrese el numero para la multiplicacion: ")) #Se ingresa por teclado el primer numero
print("\n") #Se ingresa un espacio para mejor lectura al correr el programa
if a>=2 and a<=100: #Se asigna if con la condición a mayor o igual a 2 y menor o igual a 100
    for i in range(1,a+1): #Se asigna for con un rango i
        contador3=0 #Se asigna la variable "contador3", con numero igual a 0
        contador5=0 #Se asigna la variable "contador5", con numero igual a 0
        contadorpar=0 #Se asigna la variable "contadorpar", con numero igual a 0
        contadorimpar=0 #Se asigna la variable "contadorimpar", con numero igual a 0
        print("La tabla del numero",i,"es: ") #Se imprime la condicion del for
        print("\n") #Se ingresa un espacio para mejor lectura al correr el programa
        for j in range(1,16): #Se asigna for con un rango j
            resultado=j*i #Se asigna la variable "resultado", el valor de j multiplicado por i
            if (resultado%5)==0: #Se coloca un if con la condicion de resultado modulo de 5 igual a 0
                contador5+=1 #Se asigna la variable contador5 como contador5 más 1
            if (resultado%3)==0: #Se coloca un if con la condicion de resultado modulo de 3 igual a 0
                contador3+=1 #Se asigna la variable contador3 como contador3 más 1
            if (resultado%2)==0: #Se coloca un if con la condicion de resultado modulo de 2 igual a 0
                contadorpar+=1 #Se asigna la variable contadorpar como contador2 más 1
            else: #Si la condicion if no se cumple entonces
                contadorimpar+=1 #Se asigna la variable contadorimpar como contadorimpar más 1
            suma+=resultado #Se asigna la variable "suma", el valor de suma más resultado
            print(i,"x",j,"=",resultado) #Se imprime la condicion del if o else
        print("La suma de los numeros es: ",suma) #Con un texto se imprime la variable suma
        print("El promedio de los numeros es: ",suma/15) #Con un texto se imprime la variable suma/b
        print("Los multiplos de 3 son: ",contador3) #Con un texto se imprime la variable contador3
        print("Los multiplos de 5 son: ",contador5) #Con un texto se imprime la variable contador5
        print("Los numeros pares son: ",contadorpar) #Con un texto se imprime la variable contadorpar
        print("Los impares son: ",contadorimpar) #Con un texto se imprime la variable contadorimpar
        print("\n") #Se ingresa un espacio para mejor lectura al correr el programa
else: #Si la condicion if no se cumple entonces
    print("Error el numero debe ser mayor o igual a 2 o menor o igual a 100") #Con un texto se imprime dicho mensaje
    
    
    
    
    
    
    
    
    

        
        
        
        
        
        