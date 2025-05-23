def kiem_tra_chuoi(chuoi):
    if not all(c.isalpha() for c in chuoi):
        raise ValueError("Lỗi ký tự !!!")
    
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")

    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i+1] == chuoi[i+2] == chuoi[i+3]:
            raise ValueError("Lỗi nhập lại !!!")
    tu = chuoi.split()
    for i in range(len(tu) - 4):
        if tu[i] == tu[i+1] == tu[i+2] == tu[i+3] == tu[i+4]:
            raise ValueError("Lỗi nhập trùng lặp !!!")

while True:
    try:
        chuoi = input("Nhập chuỗi ký tự: ")
        kiem_tra_chuoi(chuoi)
        print("Chuỗi hợp lệ.")
    except ValueError as e:
        print("Lỗi", e)
