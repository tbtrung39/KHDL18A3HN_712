#Bai11
n = int(input("Nhập số hàng của tam giác: "))
#Tam giác a
print("\nTam giác a:")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=' ') 
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print("*", end=' ') 
        else:
            print(" ", end=' ') 
    print()
#Tam giác b
print("\nTam giác b:")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=' ') 
    for j in range(i+1):
        if j==0 or j==i or i==n-1:
            print("*", end=' ') 
        else:
            print("  ", end=' ') 
    print()
#Tam giác c
print("\nTam giác c:")
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=' ') 
    for j in range(i+1):
        print("* ", end="")
    print()