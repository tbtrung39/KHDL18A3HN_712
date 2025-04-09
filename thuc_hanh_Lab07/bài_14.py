d = {}
for i in range(1, 101):
    d[i] = bin(i)[2:]
for k in d:
    print(f"{k}: '{d[k]}'")
