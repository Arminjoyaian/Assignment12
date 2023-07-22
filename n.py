def add(x):
    o  = []
    for m in range (1, 4):
        o.append(str(x * m))
    x = " ".join(o)
    x = x.replace(" ", "")
    return x

p = int(input("enter number: "))
print(add(p))