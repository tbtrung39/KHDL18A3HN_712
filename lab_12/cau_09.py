def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
def ngay_trong_nam(ngay, thang, nam):
    ngay_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    so_ngay = sum(ngay_thang[:thang - 1]) + ngay
    return so_ngay
def tinh_tuan(ngay, thang, nam):
    so_ngay = ngay_trong_nam(ngay, thang, nam)
    tuan = (so_ngay - 1) // 7 + 1
    return tuan
def nhap_ngay():
    while True:
        try:
            ngay = int(input("Nhập ngày: "))
            thang = int(input("Nhập tháng: "))
            nam = int(input("Nhập năm: "))
            if nam < 1:
                raise ValueError("Năm phải lớn hơn 0.")
            if thang < 1 or thang > 12:
                raise ValueError("Tháng phải từ 1 đến 12.")
            ngay_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if ngay < 1 or ngay > ngay_thang[thang - 1]:
                raise ValueError(f"Ngày không hợp lệ cho tháng {thang} năm {nam}.")
            return ngay, thang, nam
        except ValueError as e:
            print("Lỗi:", e, "Vui lòng nhập lại.")
ngay, thang, nam = nhap_ngay()
tuan = tinh_tuan(ngay, thang, nam)
print(f"Ngày {ngay}/{thang}/{nam} thuộc tuần thứ {tuan} trong năm.")
