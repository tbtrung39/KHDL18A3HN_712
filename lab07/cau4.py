chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
    152, 162, 180, 168, 169, 168, 167, 170
]

# a: trong nhom co so sinh vien la
so_sinh_vien = len(chieu_cao)

# b.  chieu cao trung binh cua cac sinh vien trong nhom
tong = 0
for x in chieu_cao:
    tong += x
trung_binh = round(tong / so_sinh_vien, 2)

# c. cac chieu cao khac nhau cua sinh vien trong nhom
chieu_cao_khac_nhau = set(chieu_cao)
chieu_cao_khac_nhau_sap_xep = sorted(chieu_cao_khac_nhau)

print("Nhom co so sinh vien la=:", so_sinh_vien)
print("Chieu cao trung binh cua cac sinh vien trong nhom la", trung_binh, "cm")
print("Cac chieu cao khac nhau cua sinh vien trong nhom la=:")
print(chieu_cao_khac_nhau_sap_xep)
print("Chiều cao trung bình:", trung_binh, "cm")