duong_dan=input("Nhap duong dan tep Inp.txt:")
with open(duong_dan,"r",encoding="utf-8") as f:
    a=sorted(map(int,f.readline().split()))
with open("out.dat","w",encoding="utf-8") as f:
    f.write(" ".join(map(str,a)))
print("Da sap xep va luu vao out.dat")
