#Bai4
ds_chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]
#a. Tính số lượng sinh viên
slg_sv = len(ds_chieu_cao)
print("Số lượng sinh viên:", slg_sv)
#b. Tính chiều cao trung bình của các sinh viên trong nhóm
chieu_cao_tb = sum(ds_chieu_cao) / slg_sv
print("Chiều cao trung bình:", chieu_cao_tb)
#c. Liệt kê các chiều cao khác nhau trong nhóm
chieu_cao_khac_nhau = list(set(ds_chieu_cao))
print("Các chiều cao khác nhau trong:", chieu_cao_khac_nhau)