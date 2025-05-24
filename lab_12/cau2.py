def validate_input(s):
    if not all(c.isalnum() for c in s):
        raise ValueError('loi ky tu')
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            current+=1
            if current ==4:
                raise ValueError('loi nhap trung lap')
            else:
                current=1
while True:
    s=input('nhap chuoi')
    if s.lower()=='exit':
        break
    try:
        validate_input(s)
        print('chuoi hop le')
    except ValueError as e:
        print('ngoai le:',e)