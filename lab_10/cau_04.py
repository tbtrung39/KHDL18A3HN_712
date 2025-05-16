import giai_pt

print("=== GIẢI PHƯƠNG TRÌNH ===")
print("1. Giải phương trình bậc nhất.")
print("2. Giải phương trình bậc hai.")
lua_chon = input("Nhập lựa chọn (1 hoặc 2): ")

if lua_chon == "1":
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    ket_qua = giai_pt.giai_pt_bac_nhat(a, b)
    print("Kết quả:", ket_qua)
elif lua_chon == "2":
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    ket_qua = giai_pt.giai_pt_bac_hai(a, b, c)
    print("Kết quả:", ket_qua)
else:
    print("Lựa chọn không hợp lệ.")