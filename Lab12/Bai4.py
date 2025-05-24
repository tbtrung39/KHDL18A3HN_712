try:
    ten=input("Nhap ten tep can doc:")
    with open(ten,'r',encoding='utf-8') as f:
        ndung=f.read()
        print("Noi dung tep:")
        print(ndung)
except FileNotFoundError:
    print("Khong tim thay tep!")
except Exception as e:
    print("Loi:", e)
finally:
    print("Ket thuc chuong trinh!")