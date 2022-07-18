res=0
aux=1
n=0
while n<=0:
    n = int(input("Ingrese un entero:"))
for i in range(1,n+1): 
    res=0
    aux=1
    for j in range(1,i+1):
            res+=aux
            aux+=2;        
    #endfor
    print (f"{i}^2 = {res}")
#endfor