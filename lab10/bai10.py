import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\Code\Thuc tap lap trinh\KHDL18A3HN_712\lab10'))
sys.path.append(parent_dir)

from bai1 import my_Triange
from bai2 import my_square

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
print("Tam giac: ")
if my_Triange.is_TamGiac(a, b, c):
    print("Chu vi:", my_Triange.ChuviTamGiac(a, b, c))
    print("Dien tich:", my_Triange.S_TamGiac(a, b, c))


print("Chu vi:", my_square.ChuviHinhVuong(6))
print("Dien tich:", my_square.Dien_tich_hinh_vuong(6))