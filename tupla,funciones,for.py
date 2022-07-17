def suma(*a):
    print("\nTipo de datos del argumento",
        type(a))
    sum=0
    for n in a:
        sum +=n
    
    print("suma:",sum)

suma(3)
suma(1)
suma(3,5)