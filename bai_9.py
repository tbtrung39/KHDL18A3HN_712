import qlyhanghoa

def main():
    mathangs = []
    n = int(input("Nhap so mat hang: "))
    
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        mathang = qlyhanghoa.nhapthongtinmathang()
        mathangs.append(mathang)
    print("\nDanh sach mat hang truoc khi sap xep theo thue VAT:")
    qlyhanghoa.hienthimathang(mathangs)
    
    mathangssapxep = qlyhanghoa.sapxeptheothue(mathangs)
    
    print("\nDanh sach mat hang sau khi sap xep theo thue VAT giam dan:")
    qlyhanghoa.hienthimathang(mathangssapxep)

if __name__ == "__main__":
    main()