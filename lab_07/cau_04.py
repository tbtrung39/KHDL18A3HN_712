chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142,
    148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165,
    170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170
]
so_sinh_vien = len(chieu_cao)
chieu_cao_tb = sum(chieu_cao) / so_sinh_vien
chieu_cao_khac_nhau = set(chieu_cao)
tb_chieu_cao_khac_nhau = sum(chieu_cao_khac_nhau) / len(chieu_cao_khac_nhau)
print("Số lượng sinh viên là:", so_sinh_vien) 
print("Chiều cao trung bình của sinh viên là:", chieu_cao_tb)
print("Chiều cao trung bình khác nhau của sinh viên là:", tb_chieu_cao_khac_nhau)
