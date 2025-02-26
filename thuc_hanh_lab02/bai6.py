num = int(input("Nhập số nguyên có ba chữ số: "))
if num < 100 or num > 999:
    print("Số không hợp lệ!")
else:
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_tram = num // 100
    hang_chuc = (num % 100) // 10
    hang_bei = num % 10
    print(f"Cách đọc của số {num} là: {don_vi[hang_tram]} trăm {don_vi[hang_chuc]} mươi {don_vi[hang_bei]}")
