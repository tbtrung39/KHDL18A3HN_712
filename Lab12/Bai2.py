def ktra_chuoi(s):
    for i in s:
        if not i.isalpha():
            raise Exception("Loi ky tu!")
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            raise Exception("Loi nhap lieu!")
    for j in range(len(s)-3):
        if s[j]==s[j+1]==s[j+2]==s[j+3]:
            raise Exception("Loi nhap lap lai!")
    for j in range(len(s)-4):
        if len(set(s[j:j+5]))==1:
            raise Exception("Loi nhap trung lap!")
while True:
    try:
        nhap_chuoi=input("Nhap chuoi ky tu:")
        ktra_chuoi(nhap_chuoi)
        print("Du lieu hop le!")
        break
    except Exception as e:
        print("Loi:", e)