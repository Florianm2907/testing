from cmath import isnan
import math

liste = ["+","-","*","/","^","!","v"]
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mal(a,b):
    return a*b
def geteilt(a,b):
    return a/b
def wurzel(a):
    return math.sqrt(int(a))
def potenz(a,b):
    c=a
    for i in range(b-1): c*=a
    return c
def faktorial(a):
    return math.factorial(int(a))
def zusammenrechnen(m):
    sum=""
    for i in range(len(m)):
        sum+=m[i]
    return sum
while True:
    argumente=[]
    rechenzeichen=[]
    asd=[]
    a=""
    b=""
    f="" # zeichen
    d=0 # temp zum checken ob es eine zahl ist
    e = False # boolean ob es ein rechenzeichen gibt
    zwischenergebnis=0
    x=input("Gib deine Rechnung ein: ")
    if x=="pi": 
        print(math.pi)
    for i in range(len(liste)):
        if liste[i] in x: asd.append(x.split(liste[i]))
        print(liste[i])
        print(asd)
    # print(x)
    # for i in range(len(liste)):
    #     f = x.find(liste[i])
    #     if not f == -1: rechenzeichen.append(liste[i])
    
    # for i in range(len(liste)):
    #     if liste[i] in x:
            
    # for h in range(len(x)):
    #     if x[h]=="+" or x[h]=="-" or x[h]=="*" or x[h]=="/" or x[h]=="!" or x[h]=="^" or x[h]=="v":
    #         rechenzeichen.append(x[h])
    #     else:
    #         argumente.append(x[h])
    # for i in range(len(x)):
        
    print(argumente)
    print(rechenzeichen)
    
    # for l in range(len(argumente)):
    #     for m in range(len(liste)):
    #         if argumente[l]==liste[m]:
    #             argumente.remove(liste[m])
    #             print("hier")
    #             print(argumente)
    if len(argumente)==1: a=int(argumente[0])
    else: b=int(argumente[1])
    
    for j in range(len(rechenzeichen)):
        k=0
        if rechenzeichen[j]=="+": 
            zwischenergebnis=plus(int(zwischenergebnis), int(argumente[k]))
            zwischenergebnis=plus(int(zwischenergebnis), int(argumente[k+1]))
            print(zwischenergebnis)
            # print(argumente[k])

        if rechenzeichen[j]=="-": 
            print(minus(int(argumente[k]),int(argumente[k+1])))

        if rechenzeichen[j]=="*": 
            print(mal(int(argumente[k]),int(argumente[k+1])))

        if rechenzeichen[j]=="/": 
            print(geteilt(int(argumente[k]),int(argumente[k+1])))

        k+=1
    if rechenzeichen[0]=="^": print(potenz(a,b))
    if rechenzeichen[0]=="!": print(faktorial(zusammenrechnen(argumente)))
    if rechenzeichen[0]=="v": print(wurzel(zusammenrechnen(argumente)))