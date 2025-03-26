#Bai11
binary_str = input("Nhập chuỗi nhị phân: ")
for i in binary_str:
    if i != '0' and i != '1':
        print("Nhập sai, vui lòng nhập chuỗi chỉ gồm 0 và 1.")
        break
else:
    decimal = int(binary_str, 2)
    print("Chuỗi nhị phân:", binary_str)
    print("Giá trị thập phân:", decimal)