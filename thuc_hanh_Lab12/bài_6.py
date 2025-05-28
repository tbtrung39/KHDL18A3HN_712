import re
danh_sach_email = []
def tao_email(username):
    if not re.fullmatch(r'[A-Za-z0-9]+', username):
        raise ValueError("Tên username không hợp lệ. Chỉ được chứa chữ cái và chữ số, không có khoảng trắng hoặc ký tự đặc biệt.")
    email = username + "@companyname.com"
    return email
def main():
    while True:
        try:
            username = input("Nhập username (hoặc nhập 'exit' để thoát): ")
            if username.lower() == 'exit':
                break
            email = tao_email(username)
            danh_sach_email.append(email)
            print(f"Địa chỉ email đã tạo: {email}")
        except ValueError as loi:
            print(f"Lỗi: {loi}")
    print("\nDanh sách email hợp lệ:")
    for e in danh_sach_email:
        print("-", e)
if __name__ == "__main__":
    main()
