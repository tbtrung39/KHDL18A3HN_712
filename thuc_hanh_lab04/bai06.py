so = int(input("Nhập số bạn muốn đọc là: "))
chu_so = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín'
}
if so < 0 :
    print ("âm",end = " ")
    so = abs(so)
so_str = str(so)
i = 0
while i < len(so_str):
    print(chu_so[so_str[i]], end=" ")
    i += 1