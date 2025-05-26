danh_sach_email = []

while True:
    username = input("Nhập username (nhập 'exit' để thoát): ")
    if username.lower() == "exit":
        break
    if not username.isalnum():
        print("Username chỉ được chứa chữ cái và số, không có dấu cách")
        continue
    email = username + "@companyname.com"
    danh_sach_email.append(email)
    print("Email đã thêm:", email)

print("Danh sách email:", danh_sach_email)