# bai 2
def kiem_tra_chuoi(s):
#1
    for ch in s:
        if not ch.isalpha() and not ch.isspace():
            raise Exception("loi ky tu !!!")
#2
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            raise Exception("Loi nhap lieu!!!")
# 3
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            raise Exception("Loi nhap lap lai !!!")
#4
    tu = s.split()
    for i in range(len(tu) - 4):
        if tu[i] == tu[i+1] == tu[i+2] == tu[i+3] == tu[i+4]:
            raise Exception("loi trung lap")

while True:
    try:
        s = input("hay nhap chuoi tu ban phim: ")
        kiem_tra_chuoi(s)
        print("vui long nhap hop le:", s)
    except Exception as e:
        print("loi", e)
