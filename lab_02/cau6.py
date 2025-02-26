n = int(input("Nhập số nguyên có ba chữ số: "))
so = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
tram = so[n // 100] + " trăm"
muoi = so[(n // 10) % 10] + " mươi"
dvi = so[n % 10]
print(f"Cách đọc: {tram} {muoi} {dvi}")