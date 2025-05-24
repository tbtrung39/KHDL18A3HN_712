def tim_max_dequy(a,b,c):
    if b>a:
        return tim_max_dequy(b,c,a)
    if c>a:
        return tim_max_dequy(c,b,a)
    return a

so1,so2,so3=map(float,input("Nhập 3 số cách nhau bằng dấu cách: ").split())
print(f"Số lớn nhất là: {int(tim_max_dequy(so1,so2,so3))}")
