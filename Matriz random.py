import random
n = int(input('Ingresar un numero:'))
m = int(input('Ingresar el segundo numero:'))
#a = n*m
matriz = []

for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(random.randint(4, 30))

print(matriz)
