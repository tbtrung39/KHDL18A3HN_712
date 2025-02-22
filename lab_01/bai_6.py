hieu_dien_the = 220
cuong_do_dong_dien = 2.7
gia_dien = 7000

def tinh_tien_dien(thoi_gian_s):
    cong_suat = hieu_dien_the*cuong_do_dong_dien 
    nang_luong_kWh = (cong_suat*thoi_gian_s)/(1000*3600)
    tien_dien = nang_luong_kWh*gia_dien
    return round(tien_dien, 2)

thoi_gian_s = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
print(f"Tiền điện phải trả: {tinh_tien_dien(thoi_gian_s)} VNĐ")
