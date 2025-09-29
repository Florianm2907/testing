while 1:
    n=int(input("Basis: "))
    a=n
    p=int(input("Potenz: "))
    for i in range(p-1): a = a*n
    
    print(a)