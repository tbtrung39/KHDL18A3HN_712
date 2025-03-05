n = int(input('Nhap vao so n: '))
tong = 0
for i in range(1, n + 1):
    tong += 1 / i
print(f'Tong nghich dao cua {n} so nguyen dau tien la: {tong:.2f}')