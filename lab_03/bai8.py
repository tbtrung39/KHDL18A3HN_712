# Bài 8:
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    S1 = 0  
    S2 = 0  
    S3 = 0  
for i in range(1, n + 1):
    S1 += i         
    S2 += 2 * i - 1 
    S3 += 2 * i     
    print("Tổng S1 của", n, "số nguyên đầu tiên là:", S1)
    print("Tổng S2 của", n, "số lẻ đầu tiên là:", S2)
    print("Tổng S3 của", n, "số chẵn đầu tiên là:", S3)
else:
      print("Giá trị n không hợp lệ, vui lòng nhập lại")