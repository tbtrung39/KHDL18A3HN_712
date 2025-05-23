def la_nam_nhuan(nam):
    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
def ngay_ke_tiep(ngay, thang, nam):
    ngay_trong_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ngay += 1
    if ngay > ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
            nam += 1
    return ngay, thang, nam
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
            ngay_trong_thang = [31, 29 if la_nam_nhuan(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if ngay < 1 or ngay > ngay_trong_thang[thang - 1]:
                raise ValueError(f"Ngày không hợp lệ cho tháng {thang} năm {nam}.")
            return ngay, thang, nam
        except ValueError as e:
            print("Lỗi:", e, "Vui lòng nhập lại.")
ngay, thang, nam = nhap_ngay()
nkt, tkt, nkt_nam = ngay_ke_tiep(ngay, thang, nam)
print(f"Ngày kế tiếp của {ngay}/{thang}/{nam} là {nkt}/{tkt}/{nkt_nam}")
