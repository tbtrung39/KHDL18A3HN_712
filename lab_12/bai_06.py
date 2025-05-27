danh_sach_email = []

while True:
    username = input("Nhap username: ")
    if username.lower() == "Exit":
        break
    if not username.isalnum():
        print("Usernam chi duoc chua chu va so")
        continue
    email = username + "@companyname.com"
    danh_sach_email.append(email)
    print("Email da them", email)

print("Danh sach email:", danh_sach_email)