heights = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
    152, 162, 180, 168, 169, 168, 167, 170
]


so_sv = len(heights)


tb = sum(heights) / so_sv

chieu_cao_khac_nhau = sorted(set(heights))

print("a. Số sinh viên trong nhóm:", so_sv)
print("b. Chiều cao trung bình:", round(tb, 2), "cm")
print("c. Các chiều cao khác nhau:", chieu_cao_khac_nhau)
