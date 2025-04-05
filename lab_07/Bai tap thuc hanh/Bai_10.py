n=int(input("Nhập số n:"))
m=int(input("Nhập số m:"))
chu_so_n=set(str(n))
chu_so_m=set(str(m))
chu_so_chung=chu_so_n&chu_so_m
tong=sum(int(c) for c in chu_so_chung)
print("Tổng các chữ số chung:",tong)