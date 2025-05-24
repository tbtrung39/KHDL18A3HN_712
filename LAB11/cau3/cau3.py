duong_dan=input("Nhap duong dan tep f_in.dat:")
with open(duong_dan,"r",encoding="utf-8")as f:
    ds=list(map(int,f.readline().split()))
ct=[ds[i]for i in range(1,len(ds)-1)if(ds[i]>ds[i-1]and ds[i]>ds[i+1])or(ds[i]<ds[i-1]and ds[i]<ds[i+1])]
with open("f_out.dat","w",encoding="utf-8")as f:
    f.write(str(len(ct))+"\n"+" ".join(map(str,ct)))
