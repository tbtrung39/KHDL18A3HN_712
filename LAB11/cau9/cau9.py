def doc_du_lieu():
    duong_dan = input("Nhập đường dẫn file PASSENGER.IN: ").strip()
    with open(duong_dan, "r", encoding="utf-8") as f:
        so_khach = int(f.readline().strip())
        danh_sach_do = []
        while len(danh_sach_do) < so_khach:
            dong = f.readline()
            if not dong:
                break
            dong = dong.strip()
            if dong == "":
                continue
            do_xachtay = list(map(float, dong.split()))
            danh_sach_do.append(do_xachtay)
    return danh_sach_do


def ghi_file_va_in_thong_bao(danh_sach_do):
    tong_trong_luong = []
    khach_bi_huy = []

    for i, do_xachtay in enumerate(danh_sach_do, start=1):
        tong = sum(do_xachtay)
        tong_trong_luong.append(tong)
        ly_do = []
        if tong > 23:
            ly_do.append("quá cân > 23 kg")
        if len(do_xachtay) > 5:
            ly_do.append(f"quá nhiều đồ xách tay ({len(do_xachtay)} > 5)")
        if ly_do:
            khach_bi_huy.append((i, ly_do))

    duong_dan_out = input("Nhập đường dẫn file WEIGHT.OUT để lưu tổng trọng lượng: ").strip()
    with open(duong_dan_out, "w", encoding="utf-8") as f:
        for tong in tong_trong_luong:
            f.write(f"{tong:.2f}\n")

    duong_dan_cancel = input("Nhập đường dẫn file CANCELED.OUT để lưu số thứ tự hành khách bị hủy: ").strip()
    with open(duong_dan_cancel, "w", encoding="utf-8") as f:
        for stt, _ in khach_bi_huy:
            f.write(f"{stt}\n")

    if khach_bi_huy:
        print("\nDanh sách hành khách bị hủy chuyến và lý do:")
        for stt, ly_do in khach_bi_huy:
            print(f" - Hành khách thứ {stt}: {', '.join(ly_do)}")
    else:
        print("\nKhông có hành khách nào bị hủy chuyến.")

def main():
    danh_sach_do = doc_du_lieu()
    ghi_file_va_in_thong_bao(danh_sach_do)

if __name__ == "__main__":
    main()
