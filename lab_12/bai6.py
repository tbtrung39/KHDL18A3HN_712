# bai 6
def kiem_tra_username(username):
    if " " in username:
        raise ValueError("Username khong duoc chua dau cach")
    if not username.isalnum():
        raise ValueError("Username chi duoc chua chu cai va chu so")

def nhap_email():
    danh_sach_email = []
    while True:
        try:
            username = input("Nhap username tu ban phim: ")
            if username == "":
                print("Ket thuc nhap lieu")
                break
            kiem_tra_username(username)
            email = username + "@companyname.com"
            danh_sach_email.append(email)
            print("Da them email:", email)
        except ValueError as e:
            print("Loi:", e)
    return danh_sach_email

ds = nhap_email()
print("\nDanh sach email da nhap la:")
for e in ds:
    print(e)
