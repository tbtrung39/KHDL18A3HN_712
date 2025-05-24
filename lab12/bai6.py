danh_sach_email = []

while True:
    username = input("nhap username: ")
    if username.lower() == "exit":
        break
    if not username.isalnum():
        print("usernam chi duoc chua chu va so")
        continue
    email = username + "@companyname.com"
    danh_sach_email.append(email)
    print("email da them", email)

print("danh sach email:", danh_sach_email)