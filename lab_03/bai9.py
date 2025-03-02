# Bài 9
n = int(input("Nhập vào số nguyên dương n: "))
if n <= 0:
   print("Giá trị không hợp lệ! Vui lòng nhập lại.")
else:
    S4 = 0  
    S5 = 0  
    S6 = 0
    for i in range(1, n + 1):
     S4 += i**2          
     S5 += (2*i - 1)**3  
     S6 += (2*i)**4      
    print("Tổng S4 của", n, S4)
    print("Tổng S5 của", n, S5)
    print("Tổng S6 của", n, S6)