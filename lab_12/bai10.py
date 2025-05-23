# bai 10
import datetime

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

def nhap_ngay(thong_bao):
    while True:
        try:
            s = input(thong_bao)
            ngay = datetime.datetime.strptime(s, "%d-%m-%Y")
            return ngay
        except ValueError:
            print("sai dinh dang.")

def tinh_khoang_cach(ngay1, ngay2):
    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1

    nam = ngay2.year - ngay1.year
    thang = ngay2.month - ngay1.month
    ngay = ngay2.day - ngay1.day

    if ngay < 0:
        thang -= 1
        if ngay2.month == 1:
            thang_truoc = 12
            nam_truoc = ngay2.year - 1
        else:
            thang_truoc = ngay2.month - 1
            nam_truoc = ngay2.year
        ngay += so_ngay_trong_thang(thang_truoc, nam_truoc)

    if thang < 0:
        nam -= 1
        thang += 12

    return nam, thang, ngay

def main():
    ngay1 = nhap_ngay("nhap ngay thu nhat (dd-mm-yyyy): ")
    ngay2 = nhap_ngay("nhap ngay thu hai(dd-mm-yyyy): ")
    nam, thang, ngay = tinh_khoang_cach(ngay1, ngay2)
    print(f"hai ngày cách nhau: {nam} năm, {thang} tháng, {ngay} ngày.")
main()
