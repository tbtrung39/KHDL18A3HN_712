n = int(input('Nhập số lần tung xúc sắc: '))
xac_suat_khong_ra = 215 / 216
xac_suat_ra = 1 - xac_suat_khong_ra**n
print(f'Xác suất 1 lần cả 3 xúc sắc ra mặt 6 trong {n} lần tung: {xac_suat_ra:.2f}')