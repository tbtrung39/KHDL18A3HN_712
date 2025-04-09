chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

#a
tong_sv = len(chieu_cao)

#b 
chieu_cao_tb = sum(chieu_cao)/tong_sv

#c 
chieu_cao_khac_nhau = sorted(set(chieu_cao))

print("So luong sinh vien:", tong_sv)
print("Chieu cao trung binh:", round(chieu_cao_tb, 2))
print("Cac chieu cao khac nhau:", chieu_cao_khac_nhau)

