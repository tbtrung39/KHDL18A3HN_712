def tim_max(a, b):
    return a if a >= b else tim_max(b, a)

def tim_max_3_so(a, b, c):
    return tim_max(tim_max(a, b), c)

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

print("Số lớn nhất là:", tim_max_3_so(a, b, c))
