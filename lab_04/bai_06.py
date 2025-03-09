so = int(input('Nhập vào một số nguyên: '))
while so <= 0:
    so = int(input('Nhập lại số nguyên dương: '))
chu = ""
while so > 0:
    so_cuoi = so % 10
    so = so // 10
    if so_cuoi == 0:
        chu = 'Khong ' + chu
    elif so_cuoi == 1:
        chu = 'Mot ' + chu
    elif so_cuoi == 2:
        chu = 'Hai ' + chu
    elif so_cuoi == 3:
        chu = 'Ba ' + chu
    elif so_cuoi == 4:
        chu = 'Bon ' + chu
    elif so_cuoi == 5:
        chu = 'Nam ' + chu
    elif so_cuoi == 6:
        chu = 'Sau ' + chu
    elif so_cuoi == 7:
        chu = 'Bay ' + chu
    elif so_cuoi == 8:
        chu = 'Tam ' + chu
    elif so_cuoi == 9:
        chu = 'Chin ' + chu
print(f'Ket qua: {chu}')
