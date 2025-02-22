#Bai11
n = int(input("Nhập số lần tung n:  "))
P = (1/6) ** 3
Q = 1 - P
to_hop = n
xac_suat = to_hop * (P ** 1) * (Q ** (n - 1))
xac_suat = int(xac_suat * 100) / 100
print("Với", n, "lần tung, xác suất có đúng 1 lần cả 3 đều ra 6 là:", xac_suat)