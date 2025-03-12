so = input('Nhập một số từ bàn phím: ')
chu = " "
i = 0
while i<len(so):
    chu_so = so[i]
    if chu_so == '0':
        chu += 'không '
    elif chu_so == '1':
        chu += 'một '
    elif chu_so == '2':
        chu += 'hai '
    elif chu_so == '3':
        chu += 'ba '
    elif chu_so == '4':
        chu += 'bốn '
    elif chu_so == '5':
        chu += 'năm '
    elif chu_so == '6':
        chu += 'sáu '
    elif chu_so == '7':
        chu += 'bảy '
    elif chu_so == '8':
        chu += 'tám '
    elif chu_so == '9':
        chu += 'chín '
    i += 1
print(chu)


    