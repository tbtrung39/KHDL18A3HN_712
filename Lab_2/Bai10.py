#Bai10
gio_bat_dau=int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc=int(input("Nhập giờ kết thúc: "))
if gio_bat_dau<5 or gio_ket_thuc>22 or gio_bat_dau>=gio_ket_thuc:
    print("Nhập sai, vui lòng nhập lại!")
else:
    tong_tien_thue=0
    for gio in range(gio_bat_dau, gio_ket_thuc):
        if gio<gio_bat_dau + 3:
            tien_moi_gio=1000000
        else:
            tien_moi_gio=1000000*0.75
        if gio>=11 and gio<15:
            tien_moi_gio*=0.9
        tong_tien_thue+=tien_moi_gio
    print("Tổng tiền thuê sân tập là:", int(tong_tien_thue), "đồng.")
