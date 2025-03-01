#a
n = int(input("Nhập số hàng của tam giác: "))
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        if j == 0 or j == 2*i or i == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

#ý b
n = int(input("Nhập số hàng của tam giác: "))
for i in range(1, n + 1):
    j = " " * (n - i)  
    if i == 1:  
        print(j + "*")
    elif i == n:  
        print("* " * n)  
    else:  
        k = " " * (2 * i - 3)
        print(j + "*" + k + "*")

#ý c
h=int(input("Nhập số hàng tam giác: ")) 
k = 2*h -2  
for dong in range(1, h+1):  
    for cot in range(1, k+1):  
        print(end=" ")  
    for cot in range(1, dong+1):        
        print("*", end=" ")   
    k=k-1   
    print("\r") 
