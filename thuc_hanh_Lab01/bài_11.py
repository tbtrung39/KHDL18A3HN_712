
n = int(input("Nhập số lần tung xúc xắc: "))
P_A = (1/6)*(1/6)*(1/6)
print(f"Xác suất để cả 3 xúc xắc ra số 6 trong một lần tung: {P_A:.5f}")
P_not_A = (215/216) ** n
print(f"Xác suất không có lần nào cả 3 xúc xắc ra số 6 sau {n} lần tung: {P_not_A:.5f}")
P_khong_ra_6 = 1 - P_not_A
print(f"Xác suất có ít nhất 1 lần cả 3 xúc xắc ra 6: {P_khong_ra_6:.2f}")
