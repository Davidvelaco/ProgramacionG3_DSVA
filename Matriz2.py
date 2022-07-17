import random

M=[]
rango=1000
while True:
    f=int(input('INGRESE FILAS:'))
    c=int(input('INGRESE COLUMNAS:'))
    if f>=4 and f<=30 and c>=4 and c<=30:
        break
    else:
        print('Incorrecto, no debe ser menor a 4 ni mayor a 30')
for i in range(f):
    M.append([0])
    for j in range(c-1):
        M[i].append(0)
for i in range (0,f):
    for j in range(0,c):
        n=random.randint(50, 1000)
        M[i][j]=n
        
for i in range (0,f):
    for j in range(0,c):
        print(M[i][j],end=' ')
    print(' ')
print("\n")    
l= len(M[0])
print("La diagonal principal es: ")
print([M[i][i] for i in range(l)]) 

print("La diagonal secundaria es: ")          
print([M[l-1-i][i] for i in range(l-1,-1,-1)])