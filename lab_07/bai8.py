A = {1, 2.5, 'hello', 4, 'world', 3.14, '42', 100, 7.5}

so_nguyen = sum(isinstance(x, int) for x in A)
so_thuc = sum(isinstance(x, float) for x in A)
chuoi = sum(isinstance(x, str) for x in A)

print("Tập hợp A:", A)
print("Số phần tử là số nguyên:", so_nguyen)
print("Số phần tử là số thực:", so_thuc)
print("Số phần tử là chuỗi:", chuoi)