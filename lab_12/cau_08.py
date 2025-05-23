def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
def ngay_truoc(ngay, thang, nam):
    ngay_trong_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ngay -= 1
    if ngay < 1:
        thang -= 1
        if thang < 1:
            thang = 12
            nam -= 1
            if nam < 1:
                raise ValueError("Không tồn tại ngày trước năm 1")
        ngay = ngay_trong_thang[thang - 1]
    return ngay, thang, nam
def nhap_ngay():
    while True:
        try:
            ngay_str = input("Nhập ngày: ")
            thang_str = input("Nhập tháng: ")
            nam_str = input("Nhập năm: ")

            ngay = int(ngay_str)
            thang = int(thang_str)
            nam = int(nam_str)
            if nam < 1:
                raise ValueError("Năm phải lớn hơn 0.")
            if thang < 1 or thang > 12:
                raise ValueError("Tháng phải từ 1 đến 12.")
            ngay_trong_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if ngay < 1 or ngay > ngay_trong_thang[thang - 1]:
                raise ValueError(f"Ngày không hợp lệ cho tháng {thang} năm {nam}.")
            return ngay, thang, nam
        except ValueError as e:
            print("Lỗi:", e, "Vui lòng nhập lại.")
try:
    ngay, thang, nam = nhap_ngay()
    nt, tt, nt_nam = ngay_truoc(ngay, thang, nam)
    print(f"Ngày trước của {ngay}/{thang}/{nam} là {nt}/{tt}/{nt_nam}")
except ValueError as e:
    print("Lỗi:", e)
