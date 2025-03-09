so = int(input("Nhập số bạn muốn đọc là: "))
chu_so = {
    '0': 'khong',
    '1': 'mot',
    '2': 'hai',
    '3': 'ba',
    '4': 'bon',
    '5': 'nam',
    '6': 'sau',
    '7': 'bay',
    '8': 'tam',
    '9': 'chinin'
}
if so < 0 :
    print ("âm",end = " ")
    so = abs(so)
so_str = str(so)
i = 0
while i < len(so_str):
    print(chu_so[so_str[i]], end=" ")
    i += 1