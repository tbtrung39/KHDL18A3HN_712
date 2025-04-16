#Bai7
def max_min(a, b, c):
    return max(a, b, c), min(a, b, c)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
so_lon_nhat, so_nho_nhat = max_min(a, b, c)
print("Số lớn nhất là:", so_lon_nhat)
print("Số nhỏ nhất là:", so_nho_nhat)