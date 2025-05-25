import re
danh_sach_email1=[]
while True:
    try:
        u=input("nhap username(nhap rong ket thuc): ")
        if u=="":
            break
        if not re.match(r"^[A-Za-z0-9]+$",u):
            raise ValueError("username khong hop le chi duoc dung chu cai")
        e=u="@companyname.com"
        danh_sach_email1.append(e)
        print(f"email da tao:{e}")
    except ValueError as e:
        print("loi:",e)
        print("danh sach email da tao:")
        for email in danh_sach_email1:
            print(e)