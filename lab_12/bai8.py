# bai 8
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

def ngay_truoc(ngay, thang, nam):
    if ngay > 1:
        return ngay - 1, thang, nam
    else:
        if thang == 1:
            nam_moi = nam - 1
            thang_moi = 12
            ngay_moi = so_ngay_trong_thang(thang_moi, nam_moi)
            return ngay_moi, thang_moi, nam_moi
        else:
            thang_moi = thang - 1
            ngay_moi = so_ngay_trong_thang(thang_moi, nam)
            return ngay_moi, thang_moi, nam

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
        n_ngay, n_thang, n_nam = ngay_truoc(ngay, thang, nam)
        print(f"ngay truoc cua {ngay}/{thang}/{nam} la: {n_ngay}/{n_thang}/{n_nam}")
    except Exception as e:
        print("loi:", e)

main()
