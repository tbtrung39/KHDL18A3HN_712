# bai 9
def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
def so_ngay_trong_thang(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0

def tinh_ngay_trong_nam(ngay, thang, nam):
    tong_ngay = 0
    for m in range(1, thang):
        tong_ngay += so_ngay_trong_thang(m, nam)
    tong_ngay += ngay
    return tong_ngay

def nhap_ngay():
    try:
        ngay = int(input("Nhap ngay tu ban phim: "))
        thang = int(input("Nhap thang tu ban phim: "))
        nam = int(input("Nhap nam tu ban phim: "))
        if thang < 1 or thang > 12:
            raise ValueError("Thang phai tu 1 den 12.")
        max_ngay = so_ngay_trong_thang(thang, nam)
        if ngay < 1 or ngay > max_ngay:
            raise ValueError(f"Ngay phai tu 1 den {max_ngay} trong thang {thang}.")
        return ngay, thang, nam
    except ValueError as e:
        raise ValueError(f"Loi nhap dlieu: {e}")

def main():
    try:
        ngay, thang, nam = nhap_ngay()
        so_ngay = tinh_ngay_trong_nam(ngay, thang, nam)
        
        tuan = (so_ngay - 1) // 7 + 1
        print(f"ngay {ngay}/{thang}/{nam} thuoc tuan thu {tuan} trong nam.")
    except Exception as e:
        print("loi:", e)
main()
