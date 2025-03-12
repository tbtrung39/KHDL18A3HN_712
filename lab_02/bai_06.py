chu_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

n = int(input("Nhập vào số nguyên có ba chữ số: "))
if 100 <= abs(n) <= 999:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10
    print(f"{chu_so[hang_tram]} trăm {chu_so[hang_chuc]} mươi {chu_so[hang_don_vi]}")
else:
    print("Số không hợp lệ!")
