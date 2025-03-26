chuoi = input("Nhập chuỗi ký tự: ")  
result = ""  

for i in range(len(chuoi)):
    if i == 0 or chuoi[i] != chuoi[i - 1]:  
        result += chuoi[i]  

print(f"Chuỗi sau khi loại bỏ các ký tự con lặp lại liên tiếp: {result}")  
