def luy_thua(a,n):
    if n==0: return 1
    return a*luy_thua(a,n-1)

a=float(input("Nhập cơ số a: "))
n=int(input("Nhập số mũ n (nguyên không âm): "))
if n<0: print("Vui lòng nhập số mũ nguyên không âm!")
else: print(f"{a}^{n} = {luy_thua(a,n)}")
