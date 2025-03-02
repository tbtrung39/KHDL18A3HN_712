# bài 11
h = int(input("Nhập số hàng của tam giác: "))
# (a) Tam giác bé
print("\nTam giác bé")
k = 2 * h - 2  
for i in range(1, h + 1):
    print(" " * k, end="")  
    for j in range(1, i + 1):
        print("* ", end="")  
    print()
    k -= 1  
# (b) Tam giác cân rỗng
print("\nTam giác cân rỗng")
k = 2 * h - 2
for i in range(1, h + 1):
    print(" " * k, end="")  
    for j in range(1, 2 * i):
        if j == 1: 
            print("*", end="")
        elif j == 2 * i - 1:  
            print("*", end="")
        elif i == h:  
            print("*", end="")
        else:
            print(" ", end="")  
    print()
    k -= 1  
# (c) Tam giác cân
print("\nTam giác cân")
k = h - 1  
for i in range(1, h + 1):
    print(" " * k, end="")  
    for j in range(1, 2 * i):
        if j == 1:  
            print("*", end="")
        elif j == 2 * i - 1:
            print("*", end="")
        elif i == h:  
            print("*", end="")
        else:
            print(" ", end="")  
    print()
    k -= 1  
