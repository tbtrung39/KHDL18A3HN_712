import sys
sys.path.append("D:/51_Pham_Thu_Trang/KHDL118A3HN_712/thuc_hanh_Lab10/doicoso")
import doicoso
n = int(input("Nhập số nguyên hệ 0: "))
print("Đổi sang nhị phân:", doicoso.doi_sang_nhi_phan(n))
print("Đổi sang bát phân:", doicoso.doi_sang_bat_phan(n))
print("Đổi sang thập lục phân:", doicoso.doi_sang_thap_luc_phan(n))
s = input("Nhập chuỗi ký tự bất kỳ: ")
hop_le = doicoso.loc_ky_tu_hop_le(s)
print("Chuỗi sau khi lọc ký tự hợp lệ (0-9, A-F):", hop_le)
co_so = doicoso.xac_dinh_co_so(hop_le)
print(f"Chuỗi có thể biểu diễn từ hệ cơ số {co_so} trở lên.")
print("\n=> Đổi từ hệ 2:", doicoso.chuyen_sang_thap_phan(hop_le, 2))
# Đổi từ hệ 8
print("=> Đổi từ hệ 8:", doicoso.chuyen_sang_thap_phan(hop_le, 8))
# Đổi từ hệ 16
print("=> Đổi từ hệ 16:", doicoso.chuyen_sang_thap_phan(hop_le, 16))