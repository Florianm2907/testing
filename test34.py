while True:
    acc = input(r"Accuracy: ")
    acc = int(acc)
    pi = 1
    i = 3
    while i < acc:
        pi = pi - (1/(i))
        i+=2
        pi = pi + (1/(i))
        i+=2
    print(pi*4)