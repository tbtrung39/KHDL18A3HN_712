def validate_string(s):
    if not s.isalpha():
        raise ValueError("Loi ky tu!!!")
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            raise ValueError("Loi nhap lap lai!!!")
        
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i+1]:
            count += 1
            if count == 5:
                raise ValueError("Loi nhap trung lap!!!")
            else:
                count = 1

try:
    chuoi = input("Nhap chuoi ky tu: ")
    validate_string(chuoi)
    print("Chuoi hop le:", chuoi)
except ValueError as e:
    print("Loi:", e)
            