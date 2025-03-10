num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
sign = -1 if ((num1 < 0) ^ (num2 < 0)) else 1
num1 = abs(num1)
num2 = abs(num2)
result = 0
while num2:
    if num2 & 1:
       result += num1
    num1 <<= 1
    num2 >>= 1 
    kq= sign * result
print("Kết quả:", kq)