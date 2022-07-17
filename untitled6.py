a=int(input("Ingrese el tamaño del vector: "))
vec=[]
sum=0
for i in range(a):
    vec.append([0])
for i in range(a):
    vec[i]=int(input("Elemento {}".format(i+1)))
    sum=sum+vec[i]
print("La suma es: ",sum)
