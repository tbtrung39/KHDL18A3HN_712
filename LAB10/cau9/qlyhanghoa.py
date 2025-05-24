def nhap_danh_sach():
    n=int(input("Số mặt hàng: "))
    ds=[]
    for _ in range(n):
        mh=input("Mã hàng: ")
        ten=input("Tên hàng: ")
        dv=input("Đơn vị tính: ")
        dg=int(input("Đơn giá: "))
        sl=int(input("Số lượng: "))
        ds.append([mh,ten,dv,dg,sl])
    return ds

def tinh_thanh_tien(ds):
    for sp in ds:
        sp.append(sp[3]*sp[4])

def tinh_thue(ds):
    for sp in ds:
        sp.append(sp[5]*0.1)

def in_danh_sach(ds):
    print(f"{'Mã':<6}{'Tên':<10}{'ĐVT':<6}{'ĐG':<6}{'SL':<6}{'Thành tiền':<12}{'Thuế':<10}")
    for sp in ds:
        print(f"{sp[0]:<6}{sp[1]:<10}{sp[2]:<6}{sp[3]:<6}{sp[4]:<6}{sp[5]:<12}{sp[6]:<10.2f}")


def sap_xep_thue(ds):
    ds.sort(key=lambda x:x[6],reverse=True)
