#Bai9
def so_dao_nguoc(n,kq):
    if n==0:
        return kq
    return so_dao_nguoc (n//10, kq*10+n%10)
so=int(input("Nhập số:"))
print("Số đảo ngược là:", so_dao_nguoc(so,0))