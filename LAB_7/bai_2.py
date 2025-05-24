import math

def rut_gon(a, b):
    ucln = math.gcd(a, b)
    return a // ucln, b // ucln

a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))
a_rutgon, b_rutgon = rut_gon(a, b)
print(f"Phân số rút gọn: {a_rutgon}/{b_rutgon}")