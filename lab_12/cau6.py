def validate_username(username):
    if not username.isalnum():
        raise ValueError('username chi gom chu va so,khong dau cach')
    return username
emails=[]
while True:
    username=input('nhap username:')
    if username.lower()=='exit':
        break
    try:
        validated= validate_username(username)
        email = validated + '@companyname.com'
        emails.append(email)
        print('email da tao:',email)
    except ValueError as e:
        print('loi:',e)