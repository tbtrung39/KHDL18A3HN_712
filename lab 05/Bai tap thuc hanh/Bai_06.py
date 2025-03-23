hex_str=input('Nhập chuỗi hệ 16:')
hex_digit="0123456789ABCDeFabcdef"
is_valid=True
for char in hex_str:
    if char not in hex_digit:
        is_valid=False
        break
if is_valid:
    decimal=0
    power=0
    for i in range(len(hex_str)-1,-1,-1):
        char=hex_str[i]
        if '0'<=char<='9':
            gia_tri=ord(char)-ord('0')
        else:
            gia_tri=ord(char.upper())-ord('A')+10
        decimal+=gia_tri*(16**power)
        power+=1
    print("Giá trị thập phân tương ứng là:",decimal)
else:
    print("Chuỗi nhập vào không phải số hệ 16 hợp lệ")