#Bai7
a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
a_goc = a
b_goc = b
while b != 0:
    tam_thoi = b
    b = a % b
    a = tam_thoi
bcnn = int((a_goc * b_goc) / a)
print("Bội chung nhỏ nhất của",a_goc,"và",b_goc,"là:",bcnn)