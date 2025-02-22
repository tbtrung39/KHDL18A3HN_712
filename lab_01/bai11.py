n = int(input("Nhập số lần tung (n): "))

truong_hop_1 = (1/6)**3  # Xác suất để cả 3 xúc xắc đều ra 6 trong 1 lần tung
truong_hop_2 = (1 - truong_hop_1)**n  # Xác suất không lần nào cả 3 ra 6 trong n lần tung
truong_hop_3 = 1 - truong_hop_2  # Xác suất ít nhất 1 lần cả 3 ra 6

print(f"Xác suất có ít nhất 1 lần cả 3 xúc xắc ra 6 trong {n} lần tung là: {round(truong_hop_3, 2)}")
