s_in=input("Nhập vào chuỗi cần giải mã:")
s_out=""
for char in s_in:
    char_code=ord(char)
    char_code-=2
    s_out+=chr(char_code)
print("Chuỗi sau khi giải mã:",s_out)