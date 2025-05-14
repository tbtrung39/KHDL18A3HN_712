def nhapthongtinmathang():
    mahang = input("Nhap ma hang : ")
    tenhang = input("Nhap ten hang: ")
    donvi = input("Nhap don vi tinh: ")
    dongia = float(input("Nhap don gia: "))
    soluong = int(input("Nhap so luong: "))
    thanhtien = dongia * soluong
    thuevat = thanhtien * 0.1
    
    return {
        "mahang": mahang,
        "tenhang": tenhang,
        "donvi": donvi,
        "dongia": dongia,
        "soluong": soluong,
        "thanhtien": thanhtien,
        "thuevat": thuevat
    }

def sapxeptheothue(mathangs):
    return sorted(mathangs, key=lambda mh: mh["thuevat"], reverse=True)

def hienthimathang(mathangs):
    print(f"{'Ma hang':<10} {'Ten hang':<20} {'Don vi':<10} {'Don gia':<10} {'So luong':<10} {'Thanh tien':<15} {'Thue VAT':<10}")
    for mh in mathangs:
        print(f"{mh['mahang']:<10} {mh['tenhang']:<20} {mh['donvi']:<10} {mh['dongia']:<10} {mh['soluong']:<10} {mh['thanhtien']:<15} {mh['thuevat']:<10}")