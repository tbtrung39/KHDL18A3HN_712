#Bai9
n = int(input("Nhập số n: "))
tong_n = 0
while n>0:
    tong_n += n%10 
    n //= 10
print("Tổng các chữ số của số",n,"là:", tong_n)