class LKT(Exception): pass
class LNL(Exception): pass
class LLL(Exception): pass
class LTLP(Exception): pass

def ktra(s):
    if not all(c.isalpha() or c.isspace() for c in s):
        raise LKT("Lỗi ký tự !!!")
    ds_tu = s.split()
    for i in range(len(ds_tu)-4):
        if ds_tu[i]==ds_tu[i+1]==ds_tu[i+2]==ds_tu[i+3]==ds_tu[i+4]:
            raise LTLP("Lỗi nhập trùng lặp !!!")
    for i in range(len(s)-4):
        if s[i]==s[i+1]==s[i+2]==s[i+3]==s[i+4]:
            raise LTLP("Lỗi nhập trùng lặp !!!")
    for i in range(len(s)-3):
        if s[i]==s[i+1]==s[i+2]==s[i+3]:
            raise LLL("Lỗi nhập lặp lại !!!")
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            raise LNL("Lỗi nhập liệu !!!")

while True:
    try:
        c = input("Nhập chuỗi: ")
        if c == '':
            print("Kết thúc.")
            break
        ktra(c)
        print("OK:", c)
        break 
    except (LKT,LNL,LLL,LTLP) as e:
        print(e)
