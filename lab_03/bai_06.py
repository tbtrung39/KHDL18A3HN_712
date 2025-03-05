n = int(input('Nhap vao so n: '))
tong = 0
for i in range(1, n + 1):
    tong += i ** 3
print(f'Tong bac 3 cua {n} so nguyen dau tien la: {tong}')