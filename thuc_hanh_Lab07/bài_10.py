m=input("Nhập số m: ")
n=input("Nhập số n: ")
chu_so_m=set(m)
chu_so_n=set(n)
chu_so_chung=chu_so_m&chu_so_n
S=sum(int(chu) for chu in chu_so_chung)
print('Tổng các chữ số chung là:',S)
