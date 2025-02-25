thang_va_ngay = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
              8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if 1 <= thang <= 12 and 1 <= ngay <= thang_va_ngay[thang]:
    if ngay == thang_va_ngay[thang]:
        ngay_tiep_theo = 1
        thang_tiep_theo = thang + 1 if thang < 12 else 1
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
    
    print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
else:
    print("Ngày hoặc tháng không hợp lệ!")