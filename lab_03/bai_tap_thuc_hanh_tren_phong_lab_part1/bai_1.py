n = int(input("Nhập n: "))
ket_qua = 1
for i in range(1, n + 1):
    bieu_thuc = (2 * i + 1) / (2 * i + 3)
    ket_qua += (2 / 3) * bieu_thuc
print("Kết quả:", round(bieu_thuc, 3))
