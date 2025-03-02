n = int(input("Nhập n: "))
tong_ket_qua = 1.0
for i in range(n):
    tich = 1
    for j in range(1, i + 2):
        tich *= (2 * j + 1) / (2 * j - 1)
    tong_ket_qua += tich
print(f"Kết quả: {round(tong_ket_qua, 3)}")