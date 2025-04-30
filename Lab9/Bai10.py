#Bai10
def tinh_Xn(n):
    if n == 0:
        return 1
    s = 0
    for i in range(n):
        s += ((n - i)**2) * tinh_Xn(i)
    return s
n = int(input("Nhập n: "))
print("X",n,"=", tinh_Xn(n))