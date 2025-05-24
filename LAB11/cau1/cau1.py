duong_dan=input("Nhap duong dan tep:")
with open(duong_dan,"r",encoding="utf-8")as tep:
    print(sum(int(so)for dong in tep for so in dong.split()if int(so)%2))
