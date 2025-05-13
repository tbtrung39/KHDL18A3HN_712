def tim_max(a, b):
    if a > b:
        return a
    else:
        return b

def tim_max_3_so(a, b, c):
    return tim_max(tim_max(a, b), c)

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

print("Số lớn nhất trong ba số là:", tim_max_3_so(a, b, c))
