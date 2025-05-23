def kt_username(username):
    return username.isalnum()
email_list=[]

while True:
    try:
        username=input("nhap username nhan vien (hoac nhan 'q' de ket thuc): ")
        if username=="q":
            break
        if not kt_username(username):
            raise ValueError("loi: username khong chua khoang trang")
        email=username+"@company.com"
        email_list.append(email)
        print(f"da them: {email}")
    except ValueError as v:
        print(v)
print("danh sach email nhan vien: ")
for e in email_list:
    print(e)