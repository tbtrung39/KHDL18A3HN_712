import sys
sys.path.append("D:/51_Pham_Thu_Trang/KHDL18A3HN_712/thuc_hanh_Lab10/hinhhoc")
import hinhhoc
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if hinhhoc.la_tam_giac(a, b, c):
    print("Là tam giác.")
    print("Chu vi:", hinhhoc.ChuviTamGiac(a, b, c))
    print("Diện tích:", hinhhoc.S_TamGiac(a, b, c))
else:
    print("Ba cạnh không tạo thành tam giác.")
canh = float(input("Nhập độ dài cạnh hình vuông: "))
print("Chu vi hình vuông:", hinhhoc.tinh_chu_vi_hv(canh))
print("Diện tích hình vuông:", hinhhoc.tinh_dien_tich_hv(canh))
