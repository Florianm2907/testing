import sys

if len(sys.argv) != 2:
    print("Missing argument <path>")
    exit(1)

data = []

with open(sys.argv[1], "r") as f:
    data = f.readlines()

data = bytes([int(x) for x in data])

with open("./image.png", "wb") as f:
    f.write(data)