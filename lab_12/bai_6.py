def kiem_tra_username_hop_le(tên_người_dùng):
    return tên_người_dùng.isalnum()

def main():
    danh_sách_email = []
    tên_miền_công_ty = "@companyname.com"
    
    while True:
        try:
            tên_người_dùng = input("Nhập tên người dùng (nhập 'exit' để kết thúc): ")
            if tên_người_dùng.lower() == 'exit':
                break

            if not kiem_tra_username_hop_le(tên_người_dùng):
                raise ValueError("Lỗi: Tên người dùng không hợp lệ. Chỉ được chứa chữ cái và số, không có dấu cách hoặc ký tự đặc biệt.")

            email = tên_người_dùng + tên_miền_công_ty
            danh_sách_email.append(email)
            print(f"Đã thêm email: {email}")
        except ValueError as lỗi:
            print(lỗi)

    print("\nDanh sách email đã nhập:")
    for email in danh_sách_email:
        print(email)

if __name__ == "__main__":
    main()
