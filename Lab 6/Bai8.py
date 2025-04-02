#Bai8
n = int(input("Nhập n: "))
a, b = 0, 1
print(a, end=' ')
for i in range(n - 1):
    print(b, end=' ')
    a, b = b, a + b