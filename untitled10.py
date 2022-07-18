def isPrime(n):
    for i in range (2,n):
        if n % i == 0:
            return False
        else: 
            return True
    
for i in range (1,20):
    if isPrime(i+1):
        print (i+1)    
print()