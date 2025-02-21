n = int(input('Nhập số lần tung xúc sắc: '))
doi = 1 - (1 / 216)
xac_suat = 1 - doi**n
print(f'Xác suất 1 lần cả 3 xúc sắc ra mặt 6 trong {n} lần tung: {xac_suat:.2f}')