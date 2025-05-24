def kiem_tra_chuoi(chuoi):
    try:
        for i in range(len(chuoi)):
            ky_tu = chuoi[i]
            
            if not ky_tu.isalpha():
                raise Exception("Lỗi ký tự !!!")

            if i >= 1 and chuoi[i] == chuoi[i-1]:
                raise Exception("Lỗi nhập liền !!!")

            if i >= 3 and chuoi[i] == chuoi[i-1] == chuoi[i-2] == chuoi[i-3]:
                raise Exception("Lỗi nhập lặp lại !!!")

            if i >= 4 and chuoi[i] == chuoi[i-1] == chuoi[i-2] == chuoi[i-3] == chuoi[i-4]:
                raise Exception("Lỗi nhập trùng lặp !!!")
        
        print("Chuỗi hợp lệ:", chuoi)
    
    except Exception as loi:
        print(loi)

while True:
    chuoi_nhap = input("Nhập chuỗi ký tự (gõ 'exit' để thoát): ")
    if chuoi_nhap.lower() == "exit":
        break
    kiem_tra_chuoi(chuoi_nhap)
