import math
def nhap_canh(ten):
    while True:
        try:
            n = float(input(f"Nhập {ten}: "))
            if n <= 0:
                raise ValueError
            return n
        except:
            print("Lỗi! Vui lòng nhập số > 0.")
a = nhap_canh('a')
b = nhap_canh('b')
c = nhap_canh('c')
ds = [a,b,c]
print("List:", ds)
if a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không tạo thành tam giác.")
else:
    p = sum(ds) / 2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print(f"Diện tích tam giác: {s:.2f}")
