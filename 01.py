from random import randint
acu=0
n=int(input('Ingrese el numero de filas: '))
m=int(input('Ingrese el numero de columnas: '))
if n<3 or m<3:
    print('Error, debe ser mayor a 4')
elif n>30 or m>30:
    print('Error, debe ser menor a 30')
elif n!=m:
    print('Error, debe ser una matriz cuadrada')
else:
    matriz=[[int()for i in range(n)]for j in range(m)]
    matriz1=[[int()for i in range(n)]for j in range(m)]
    
    for i in range(n):
        for j in range(m):    
            matriz1[i][j]=matriz[i][j]
        print(' ')
    print('\n')
    
    for i in range(n):
        for j in range(m):
            matriz[i][j]=randint(0,100)

    for i in range(n):
        for j in range(m):
            print('/',matriz[i][j],'/',end='')     
        print(' ')
    print('\n')
    
    print('Matriz original')
    for i in range(n):
        for j in range(m):
                print('/',matriz[i][j],'/',end='')
        print(' ')
    print('\n')
    
    print('Columna a sumar')
    num=int(input('Ingrese el numero de columna que desea sumar: '))
    print('\n')
    num=num-1
    for i in range (n):
        for j in range(m):
            if j==num:
                acu=acu+matriz[i][j]
                matriz1[i]=matriz[i][j]
                prom=acu/m
                print('La suma de la columna es:',acu,'y el promedio es:',prom)
                print(' \n')
                print('La columna utilizada es:',matriz1)



