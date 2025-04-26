def so_dao_nguoc(n,kq):
    if n==0:
        return kq
    return so_dao_nguoc (n//10, kq*10+n%10)
so=int(input("nhap so:"))
print("so dao nguoc la:", so_dao_nguoc(so,0))