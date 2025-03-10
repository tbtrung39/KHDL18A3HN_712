print('Nhập số ban đầu :',end=' ')
soBanDau = int(input())
temp=soBanDau
if soBanDau < 0:
    print("Xin mời nhập số tự nhiên!")
else:
    soDaoNguoc = 0
    while soBanDau > 0:
        chuSoCuoi = soBanDau % 10
        soDaoNguoc = soDaoNguoc * 10 + chuSoCuoi
        soBanDau //= 10
print('Số đảo ngược của số',temp, 'là:',soDaoNguoc)