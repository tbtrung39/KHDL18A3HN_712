chuoi = input("Nhập chuỗi ký tự: ")  
ket_qua = ""  

for c in chuoi:
    if c.isdigit():  
        ket_qua += c  

print(f"Chuỗi sau khi loại bỏ ký tự không phải số: {ket_qua}")  

if ket_qua:
    print("Chuỗi vẫn còn số.")  
else:
    print("Chuỗi không có số.")