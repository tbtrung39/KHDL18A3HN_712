# bai 7
def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return 0  

def ngay_ke_tiep(ngay, thang, nam):
    max_ngay = so_ngay_trong_thang(thang, nam)
    if max_ngay == 0:
        raise ValueError("Thang khong hop le")
    if ngay < max_ngay:
        return ngay + 1, thang, nam
    else:
        if thang == 12:
            return 1, 1, nam + 1
        else:
            return 1, thang + 1, nam

def nhap_ngay():
    try:
        ngay = int(input("Nhap ngay tu ban phim: "))
        thang = int(input("Nhap thang tu ban phim: "))
        nam = int(input("Nhap nam tu ban phim: "))
        if thang < 1 or thang > 12:
            raise ValueError("thang phai tu 1 den 12.")
        max_ngay = so_ngay_trong_thang(thang, nam)
        if ngay < 1 or ngay > max_ngay:
            raise ValueError(f"ngay phai tu 1 den {max_ngay} trong thang {thang}.")
        return ngay, thang, nam
    except ValueError as e:
        raise ValueError(f"loi nhap dlieu: {e}")

def main():
    try:
        ngay, thang, nam = nhap_ngay()
        n_ngay, n_thang, n_nam = ngay_ke_tiep(ngay, thang, nam)
        print(f"ngay ke tiep cua {ngay}/{thang}/{nam} la: {n_ngay}/{n_thang}/{n_nam}")
    except Exception as e:
        print("loi:", e)

main()
