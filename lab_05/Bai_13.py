A = input("Nhập chuỗi số A: ")  
B = input("Nhập chuỗi số B: ")  

if A.isdigit() and B.isdigit():  
    bieu_thuc = '+'.join(A) + '=' + B  
    if eval('+'.join(A)) == int(B):  
        print(f"Đẳng thức đúng: {bieu_thuc}")  
    else:
        print(f"Đẳng thức sai: {bieu_thuc}")  
else:
    print("Không tồn tại cách đặt!")  