def tim_max(a,b):
    if a>b:
        return a
    else:
        return b
def max_3_so(a,b,c):
    return tim_max(tim_max(a,b),c)
a=int(input("Nhập số thứ nhất:"))
b=int(input("Nhập số thứ hai:"))
c=int(input("Nhập số thứ ba: "))
print("Số lớn nhát là:",max_3_so(a,b,c))
