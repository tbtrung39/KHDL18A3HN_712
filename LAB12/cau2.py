class LKT(Exception): pass
class LNL(Exception): pass
class LLL(Exception): pass
class LTLP(Exception): pass

def ktra(s):
    if not s.isalpha(): raise LKT("Lỗi ký tự !!!")
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            if i+4<len(s) and s[i:i+5]==s[i]*5: raise LTLP("Lỗi nhập trùng lặp !!!")
            if i+3<len(s) and s[i:i+4]==s[i]*4: raise LLL("Lỗi nhập lặp lại !!!")
        raise LNL("Lỗi nhập liệu !!!")

while True:
    try:
        c=input("Nhập chuỗi: ")
        ktra(c)
        print("OK:",c)
    except (LKT,LNL,LLL,LTLP) as e: print(e)