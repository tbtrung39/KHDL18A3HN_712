def is_valid_username(username):
    if not username.isalnum():
        raise ValueError("Ten nguoi dung khong hop le. Chi bao gom chu va so.")
    return True

try:
    ds = []
    while True:
        nhap = input("Nhap username (Enter de ket thuc): ")
        if nhap == "":
            break
        if is_valid_username(nhap):
            email = nhap + "@companyname.com"
            ds.append(email)
    print("Danh sach email: ")
    for email in ds:
        print(email)
except ValueError as e:
    print("Loi:", e)
