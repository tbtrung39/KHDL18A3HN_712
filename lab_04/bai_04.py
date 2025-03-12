tu_so = int(input('Nhập tử số: '))
mau_so = int(input('Nhập mẫu số: '))
while mau_so == 0:
    print('Mẫu số phải lớn hơn 0. Vui lòng nhập lại!')
    mau_so = int(input('Nhập mẫu số: '))

print(f'Phân số đã cho là: {tu_so}/{mau_so}')