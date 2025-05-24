import os
ten=input("Nhap ten tep can doc:")
if not os.path.isfile(ten):
    print("Khong tim thay tep!")
else:
    try:
        with open(ten,'r',encoding='utf-8') as f:
            ndung=f.read()
        with open('copy.dat','w',encoding='utf-8') as file:
            file.write(ndung)
        print("Da sao chep noi dung sang file copy.dat")
    except Exception as e:
        print("Loi:", e)