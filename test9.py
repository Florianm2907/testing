while 1:
    n=int(input("Faktor: "))
    p=1
    for i in range(2,n+1): p*=i
    # print(p)
    print("hier")
    datei = open("./faktorial.txt", "w")
    datei.write(str(p))
    print(p)