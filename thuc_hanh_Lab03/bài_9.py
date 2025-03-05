#câu a
n = int(input("Nhập n: "))
S1 = 0
for i in range(1, n + 1):
    S1 += i ** 2
print("Tổng S =", S1)
#câu b
n = int(input("Nhập giá trị n: "))  
S2 = 0
for i in range(n):
    S2 += (2 * i + 1) ** 3  
print("Tổng S5 là:", S2)
#câu c
n = int(input("Nhập giá trị n: "))  
S3 = 0
for i in range(1, n + 1):  
    S3 += (2 * i) ** 4  
print("Tổng S3 là:", S3)

