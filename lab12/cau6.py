def tao_email(username):
    if ' ' in username:
        raise ValueError("Tên không được chứa dấu cách.")
    if not username.isalnum():
        raise ValueError("Tên chỉ được chứa chữ cái và số.")
    return username + "@companyname.com"

ds_email = []
while True:
    try:
        user = input("Nhập username (hoặc nhập 'stop' để kết thúc): ")
        if user.lower() == "stop":
            break
        email = tao_email(user)
        ds_email.append(email)
    except ValueError as ve:
        print("Lỗi:", ve)

print("Danh sách email:", ds_email)