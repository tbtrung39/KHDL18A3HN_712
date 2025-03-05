n = int(input("Nhập số hàng của tam giác: "))

# a) Vẽ tam giác rỗng chính giữa
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

print("\n")
 
# b) Vẽ hai tam giác đối xứng tạo thành hình thoi rỗng
print("\nTam giác cân rỗng")
k = n - 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")  
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")  
    print()
    k -= 1  

print("\n")

# c) Tam giác bé
print("\nTam giác bé")
k = 2 * n - 2  
for i in range(1, n + 1):
    print(" " * k, end="")  
    for j in range(1, i + 1):
        print("* ", end="")  
    print()
    k -= 1  