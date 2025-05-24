def kiem_tra_ky_tu(s):
    if not s.isalpha():
        return "loi ky tu"
    return None

def kiem_tra_lien_tiep(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return "loi nhap"
    for i in range(len(s) - 3):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3]:
            return "loi nhap"
    for i in range(len(s) - 4):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4]:
            return "loi nhap"
    return None

while True:
    s = input("nhap chuoi: ")
    if s.lower() == "exit":
        break
    loi = kiem_tra_ky_tu(s)
    if loi:
        print(loi)
        continue
    loi = kiem_tra_lien_tiep(s)
    if loi:
        print(loi)
    else:
        print("chuoi hop le")