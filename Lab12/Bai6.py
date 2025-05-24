def ktra_ten_dang_nhap(ten):
    return ten.isalnum()
def tao_ds_email():
    ds_email=[]
    while True:
        ten=input("Nhap username:")
        if ktra_ten_dang_nhap(ten):
            email=ten+"@companyname.com"
            ds_email.append(email)
        else:
            print("username khong hop le!")
    return ds_email
danh_sach=tao_ds_email
print("Danh sach email:, danh_sach")