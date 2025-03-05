n = int(input('Nhap vao so n: '))
tong = 1
for i in range(1, n+1):
    phan_so = 1
    phan_so *= 2*(i + 1) / (2 * i + 3)
    tong += phan_so
print(f'Tong la: {tong:.3f}')