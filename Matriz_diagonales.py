import random 
while True:
    f=int(input('Ingrese las filas: '))
    c=int(input('Ingrese las columnas: '))
    if f<4 or c<4:
        print('Error no puede ser menor a 4')
    if f>30 or c>30:
        print('Error no puede ser mayor a 30')
    else:
        break
    
m=[[int()for i in range(f)] for j in range(c)]
for i in range(f):
    for j in range(c):
        m[i][j]=random.randint(50, 1000)

for i in range (f):
    for j in range (c):
        print('|', m[i][j], '|', end=' ')
    print('   ')

if f==c:
 print("La diagonal principal es: ")
 print()
    
for i in range (f):
     for j in range (c):
         if i==j:
             print("/",m[i][j],"/", end=" ")
         else:
          print("/","- ","/",end=" ")
     print("")
    
         
if f==c:
 print("La diagonal secundaria es: ")
 print()
 
for i in range (f):
     for j in range (c):
      if i+j==f-1:
       print("/",m[i][j],"/",end=" ")
      else:
       print("/","- ","/",end=" ")
     print("")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    