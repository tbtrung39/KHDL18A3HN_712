ky_tu = input('Nhập vào một ký tự: ')
for i in ky_tu:
    if len(ky_tu) == 1:
        gia_tri_ascii = ord(i)
        print(f'Giá trị ASCII của {i} là {gia_tri_ascii}')
    else:
        print('Vui lòng nhập đúng một ký tự!')
    break