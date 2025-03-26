#Bai6
str = input("Nhập chuỗi ký tự: ")
hex_digits = "0123456789ABCDEF"
is_hex = True
for char in str:
    if char not in hex_digits:
        is_hex = False
        break
if is_hex:
    decimal = int(str, 16) 
    print("Chuỗi", str, "thuộc hệ Hex và có giá trị thập phân là:", decimal)
else:
    print("Chuỗi", str, "không phải là hệ Hex!")