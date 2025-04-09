chieu_cao=[161,182,161,154,176,170,167,171,170,174,150,142,148,165,170,178,156,145,149,163,162,159,165,165,170,180,155,159,155,153,152,162,180,168,169,168,167,170]
so_luong_sv=len(chieu_cao)
print("Số lượng sinh viên:",so_luong_sv)
chieu_cao_tb=sum(chieu_cao)/so_luong_sv
print("Chiều cao trung bình: ",round(chieu_cao_tb,2))
print("Các chiều cao khác nhau: ")
chieu_cao_khac_nhau=set(chieu_cao)
for chieu_cao in sorted(chieu_cao_khac_nhau):
    print(chieu_cao)