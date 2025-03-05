h = int(input())
k = 2 * h - 2
for dong in range(1, h + 1):  
    print(" " * k, end="")
    if dong == 1 or dong == h:
        print("* " * dong)
    else:
        print("*" + "  " * (dong - 2) + " *")
    k -= 1