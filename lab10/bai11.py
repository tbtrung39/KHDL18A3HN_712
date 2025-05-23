import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\Code\Thuc_hanh_git\KHDL18A3HN_712\lab_10'))
sys.path.append(parent_dir)

from bai5 import doicoso1
from bai6 import doicoso2


n = int(input("Nhap n: "))
print("Nhi phan:", doicoso1.nhi_phan(n))
print("Bat phan:", doicoso1.bat_phan(n))
print("Hex:", doicoso1.thap_luc_phan(n))

s = input("Nhap s: ")
print("Chuoi sau khi loc:", doicoso2.loc_ky_tu_hop_le(s))
print("Chuoi thuoc he:", doicoso2.xac_dinh_he_co_so(s))
he_co_so = doicoso2.xac_dinh_he_co_so(s)
print(f"Chuoi bieu dien theo he co so {he_co_so}")
gia_tri_thap_phan = doicoso2.chuyen_sang_thap_phan(s, he_co_so)
print(f"Gia tri thap phan tuong ung: {gia_tri_thap_phan}")