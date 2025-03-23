s_in=input("Nhập vào chuỗi cần mã hóa:")
s_out=""
for char in s_in:
    char_code=ord(char)
    char_code=char_code+2
    char=chr(char_code)
    s_out+=char
print("Chuỗi sau khi mã hóa:",s_out)