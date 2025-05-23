def kt_kytu(c):
    return c.isalpha()
def kt_loi(s,history):
    for c in s:
        if not kt_kytu(c):
            raise Exception("loi ky tu")
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            raise Exception("loi nhap lieu")
    for i in range(len(s)-3):
        if s[i]==s[i+1]==s[i+2]==s[i+3]:
            raise Exception("loi nhap lap lai")
        
history=[]
while True:
    try:
        s=input("nhap chuoi ky tu: ")
        if s=="ab" or s=="A.CZ":
            print("ket thuc chuong trinh")
            break
        kt_loi(s,history)
        history.append(s)
        print("chuoi hop le: ",s)
    except Exception as e:
        print(e)