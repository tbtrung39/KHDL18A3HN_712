n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Số nhập bị lỗi. Vui long nhập lại!!!")
    n = int(input("Nhập lại số nguyên dương n : "))

# Tính tổng a
tong_a = 0
i = 1
while i <= n:
    if i % 2 == 0:
        tong_a -= 1 / i 
    else:
        tong_a += 1 / i  
    i += 1
print("Gia tri can tim la: ", tong_a)

# Tính tổng b
tong_b = 0
i = 2
while i <= n:
    tong_b += 1 / (i * (i + 1))
    i += 1
print("Gia tri can tim la : ", tong_b)

# Tính tổng c
tong_c = 0
i = 2
while i <= n:
    tong_c += 1 / (i ** 0.5)  
    i += 1
print("Gia tri can tim la: ",tong_c)