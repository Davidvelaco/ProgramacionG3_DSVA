n=t=0
while n<=0:
    n=int(input("Tamaño del paquete: "))
while t<=0:
    t=int(input("tamaño maximo de ventana de envio: "))

print(" |",end="")
for i in range(1,t+1):
    print(f"\t(n*i)",end="")
print()

for i in range(1,t*10):
    print("-",end="")
print()

for i in range(1,11):
    print("\n",i*10,"|",end=" ")
    for j in range(1,t+1):
        print(round((j*n)/(i*10),1),end=" ") 