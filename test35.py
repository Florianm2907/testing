while True:
    genau = input(r"Genauigkeit: ")
    genau = int(genau)
    s=0
    k=1
    for i in range(genau):
        if i % 2 == 0:
            s+=4/k
        else:
            s-=4/k
        k+=2
     
    print(s)