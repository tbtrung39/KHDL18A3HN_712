m = input("Hay nhap so tu nhien m: ")
n = input("Hay nhap so tu nhien n: ")
tap_m = set()
for ky_tu in m:
    if ky_tu.isdigit():
        tap_m.add(ky_tu)

tap_n = set()
for ky_tu in n:
    if ky_tu.isdigit():
        tap_n.add(ky_tu)
chung = tap_m & tap_n

tong = 0
for so in chung:
    tong += int(so)

print("Cac chu so chung cua", m, "va", n, "la=", chung)
print("Tong cac chu so chung la =:", tong)