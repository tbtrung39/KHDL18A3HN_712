def nhap_username():
    while True:
        try:
            username = input("Nhập username (chỉ gồm chữ và số, không dấu): ")
            if not username.isalnum():
                raise ValueError("Username chỉ được chứa chữ và số, không dấu.")
            return username
        except ValueError as e:
            print("Lỗi:", e)

emails = []
username = nhap_username()
email = username + "@companyname.com"
emails.append(email)
print("Danh sách email:", emails)
