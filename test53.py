a = 4
b = 2000

for i in range(120):
    b+=b*a/100
    a+=0.05
    print("Monate: " + str(i) + ", Zinssatz: " + str(round(a,2)) + ", Geld: " + str(round(b,2)))