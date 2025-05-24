m=input("Nhap duong dan file m_nums.txt:")
n=input("Nhap duong dan file n_num.txt:")
with open(m) as f1,open(n) as f2:
  a=set(map(int,f1.read().split()))
  b=set(map(int,f2.read().split()))
c=sorted(a&b)
with open("so_chung.txt","w") as f:f.write(" ".join(map(str,c)))
print(open("so_chung.txt").read())
