print('cách 1\n')
Str = input("Nhập chuỗi: ")
S= 0
for ky_tu in Str:
    if ky_tu.isdigit():
        S =S+ 1
print("Số lượng ký tự là số:", S)
print('cách 2\n')
Str = input("Nhập chuỗi: ")
S = sum(1 for ky_tu in Str if ky_tu.isdigit())
print("Số lượng ký tự là số:", S)

