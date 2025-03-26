#Bai13
a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")
found = False
for i in range(1, len(a)):
    for j in range(1, len(b)):
        c = a[:i]
        d = a[i:]
        e = b[:j]
        f = b[j:]
        if int(c) + int(d) == int(e) + int(f):
            if not found:
                print("Tìm được cách đặt:")
                found = True
            print(c,"+",d,"=",e,"+",f)
if not found:
    print("Không tồn tại cách đặt!")