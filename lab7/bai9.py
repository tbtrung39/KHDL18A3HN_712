# bai 9 
import Qlyhanghoa 

def main():
    mathangs = []
    n = int(input("Nhap so mat hang: "))
    
    for i in range(n):
        print(f"\nNhap thong tin mat hang thu {i+1}:")
        mathang = Qlyhanghoa.nhapthongtinmathang()
        mathangs.append(mathang)
    print("\nDanh sach mat hang truoc khi sap xep theo thue VAT:")
    Qlyhanghoa.hienthimathang(mathangs)
    
    mathangssapxep = Qlyhanghoa.sapxeptheothue(mathangs)
    
    print("\nDanh sach mat hang sau khi sap xep theo thue VAT giam dan:")
    Qlyhanghoa.hienthimathang(mathangssapxep)

if __name__ == "__main__":
    main()