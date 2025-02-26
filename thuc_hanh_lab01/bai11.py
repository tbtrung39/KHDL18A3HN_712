# Nhập số lần tung
n = int(input("Nhập số lần tung: "))

# Tính xác suất để cả 3 xúc sắc đều ra 6 trong 1 lần tung
xac_suat_1_lan = (1/6)**3

# Tính xác suất để ít nhất 1 lần cả 3 xúc sắc đều ra 6 trong n lần tung
xac_suat_n_lan = 1 - (1 - xac_suat_1_lan)**n

# In kết quả (làm tròn đến 2 chữ số thập phân)
print("Xác suất để ít nhất 1 lần cả 3 xúc sắc đều ra 6 trong {} lần tung là: {:.2f}".format(n, xac_suat_n_lan))
